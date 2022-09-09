
from masced_bandits.bandits.Bandit import Bandit
from masced_bandits.utilities import convert_conf, RT_THRESH, calculate_utility, save_to_pickle
from masced_bandits.bandit_options import bandit_args
from masced_bandits.bandits import init_bandit
from masced_bandits.bandits.UCB import CUM_REWARD, UCB
from masced_bandits.bandits.EXP3 import EXP3
from masced_bandits.bandits.EwS import EwS


class Cleaner():
    def __init__(self):
        pass

    def clean(self, servers, dimmer):
        return convert_conf((3,0.0), (servers,dimmer))

def print_bounds():
    print("bounds are \n")
    print(bandit_args["bounds"])
    print("bounds done\n")

def print_rounds():
    print("\n-----Rounds so far-----")
    print("Cleaning rounds: " + str(bandit_args['round_counter'][0]))
    print("Bandit rounds  : " + str(bandit_args['round_counter'][1]))
    print("-----    End      -----\n")

experiments = { #This is a dict of configurations for an experiment. This should match what is in bandits_sa.ini
    "E1": {"arms": [(1,1.0), (2,1.0), (3,1.0)], "initial_configuration": (1,1.0), "bounds": (-500,500)} #Here the arms are the (servers,dimmer) adaptation options
}

def activate_experiment(experiment_dict):
    for key in experiment_dict.keys():
        bandit_args[key] = experiment_dict[key]


#We take control over if the bandit is actually called by SWIM or if we clean
def start(bandit_name,  dimmer, response_time, activeServers, servers, max_servers, total_util, arrival_rate, basic_throughput, opt_throughput, basic_response, opt_response, service_time, formula, experimentID, elapsedTime):
    activate_experiment(experiments[experimentID])

    if(bandit_args["bandit_instance"]):
        bandit = bandit_args["bandit_instance"]

        if(isinstance(bandit, Bandit)):
            print_rounds()
           
            if(bandit_args['cleaning']):
                
                if(response_time > RT_THRESH): 
                    bandit_args['round_counter'][0]+=1
                    return "" #continue cleaning
                else:
                    #print("Cleaning is done -----\n")
                    bandit_args['cleaning'] = False
                    bandit_args['round_counter'][1]+=1
                    x = convert_conf(bandit_args["stored_choice"],(3,0.0)) 
                    #print("Store choice: " + str(x))

                    return x
            else:
                reward, is_bound_diff, bound_delta = calculate_utility(arrival_rate, dimmer, response_time, max_servers, servers)

                if(is_bound_diff and isinstance(bandit, UCB) and bandit_args["dynamic_bounds"]):
                    print("\n\n\n\nAdjusted the rewards\n\n\n\n")

                    for arm in bandit.arms: bandit.arm_reward_pairs[arm][CUM_REWARD] = bandit.arm_reward_pairs[arm][CUM_REWARD] * bound_delta
                    print(bandit.arm_reward_pairs)

                if(bandit.last_action != (servers, dimmer)): 
                    raise RuntimeError("Previously chosen configuration " + str(bandit.last_action) + " is not reflected in SWIM's" + str((servers,dimmer)))
               
                new_choice = bandit.get_next_arm(reward[0])
                print("returned arm " + str(new_choice))

                if(response_time > RT_THRESH): #is there a backlog to clean/clear
                    #clean
                    janitor = Cleaner()

                    bandit_args['cleaning'] = True

                    bandit_args["stored_choice"] = new_choice
                    bandit_args['round_counter'][0]+=1
                    return janitor.clean(servers,dimmer)
                else: #dont need to clean
                    bandit_args['round_counter'][1]+=1
                    if(bandit_args["record_decisions"]): 
                        save_to_pickle(bandit, bandit.name + str(formula) + "_" + str(bandit_args["start_time"]))
                    converted =  convert_conf(new_choice, (servers,dimmer))
                    return converted
    else:
        formula_args = {}
        for formula_para in formula.split(","): 
            par_name, par_val = [x.strip() for x in formula_para.split(":")] 
            formula_args[par_name] = par_val 
        formula_args["name"] = bandit_name
        bandit_args["bandit_instance"] = init_bandit(**formula_args)
        return start(bandit_name,  dimmer, response_time, activeServers, servers, max_servers, total_util, arrival_rate, basic_throughput, opt_throughput, basic_response, opt_response, service_time, formula, experimentID, elapsedTime)

def unconvert_conf(swim_commands, previous_config):
    new_arm = previous_config
    for command in swim_commands:
        if command == 'add_server':
            new_arm[0]+=1
        elif(command == 'remove_server'):
            new_arm[0]-=1
        elif('set_dimmer' in command ):
            new_arm[1] = float(command.split()[-1])

    return tuple(new_arm)
