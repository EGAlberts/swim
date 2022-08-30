
from some_bandits.bandits.Bandit import Bandit
from some_bandits.utilities import convert_conf, RT_THRESH, calculate_utility, save_to_pickle
from some_bandits.bandit_options import bandit_args
from some_bandits.bandits import init_bandit
from some_bandits.bandits.UCB import CUM_REWARD, UCB
from some_bandits.bandits.EXP3 import EXP3
from some_bandits.bandits.EwS import EwS


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



trace_60 = {
    'random_performer' :
    {EXP3 : [79.4794112527964, 62.18792555434983, 34.306525360073756]}
#     objects[-1].distribution
# [0.7880331088697141, 0.19220971682501659, 0.019757174305269326]

}

trace_80 = {
    'random_performer' :
    {EXP3  : [42.93981947839889, 95.89160250491217, 66.3266698199722]}
    
}

trace_140 = {
    'worst_performer' : 
    {EwS : ([0.9938546892901092, 0.9938546892901092, 0.0],{(5, 1.0): [0.0, 8.0], (4, 1.0): [0.0, 11.0], (10, 1.0): [275.29774893336025, 277.0]}), EXP3: [192.93433088676653, -99472.35659145738, 287.96944454409913]},
    'median_performer': 
    {EwS: ([0.9951042992968598, 0.9951042992968598, 0.0], {(5, 1.0): [0.0, 4.0], (4, 1.0): [0.0, 4.0], (10, 1.0): [303.50681128554226, 305.0]}), EXP3: [200.7848367763289, -404.68784069992887, 295.89374718099396]},
    'best_performer': 
    {EwS: ([0.9947425026876044, 0.9947425026876044, 0.0],{(5, 1.0): [0.0, 3.0], (4, 1.0): [0.0, 3.0], (10, 1.0): [310.3596608385326, 312.0]}), EXP3: [141.12866685514246, 142.72094256613448, 298.91091259919637]}
}

trace_110 = {
  'worst_performer' : 
    {EwS : ([0.5719001467537402, 0.0, 0.24139487069662557],{(5, 1.0): [154.41303962350986, 270.0], (4, 1.0): [0.0, 11.0], (10, 1.0): [10.245663557770554, 31.0]}), EXP3: [104.4777383034042, 148.91444746303324, 117.46744617854078]},
    'median_performer': 
    {EwS: ([0.5734510772468258, 0.0, 0.24313579475256947],{(5, 1.0): [158.2724973201239, 276.0], (4, 1.0): [0.0, 9.0], (10, 1.0): [10.239773757321945, 31.0]}), EXP3: [-2.406616541936046, 179.0646987361334, 147.075162476988]},
    'best_performer': 
    {EwS: ([0.5811608128056863, 0.0, 0.2580101708141934],{(5, 1.0): [164.46851002400922, 283.0], (4, 1.0): [0.0, 8.0], (10, 1.0): [9.048217975761801, 28.0]}), EXP3: [59.97015066462592, 179.21913333724783, 156.16348920722575]}
}

#302 110 {(5, 1.0): [158.2724973201239, 276.0], (4, 1.0): [0.0, 9.0], (10, 1.0): [10.239773757321945, 31.0]}


knldg = {
    'results/c301/pyEwS/': 
    {'median_performer': [0.9951042992968598, 0.9951042992968598, 0.0], 'worst_performer': [0.9938546892901092, 0.9938546892901092, 0.0], 'best_performer': [0.9947425026876044, 0.9947425026876044, 0.0]},
    'results/c301/pyEXP3FH/': 
    {'median_performer': [200.7848367763289, -404.68784069992887, 295.89374718099396], 'best_performer': [141.12866685514246, 142.72094256613448, 298.91091259919637], 'worst_performer': [192.93433088676653, -99472.35659145738, 287.96944454409913]},
    'results/c302/pyEwS/': 
    {'best_performer': [0.5811608128056863, 0.0, 0.2580101708141934], 'worst_performer': [0.5719001467537402, 0.0, 0.24139487069662557], 'median_performer': [0.5734510772468258, 0.0, 0.24313579475256947]},
    'results/c302/pyEXP3FH/': 
    {'worst_performer': [104.4777383034042, 148.91444746303324, 117.46744617854078], 'best_performer': [59.97015066462592, 179.21913333724783, 156.16348920722575], 'median_performer': [-2.406616541936046, 179.0646987361334, 147.075162476988]}
}

experimentsThesis = {
    "R01": {"arms": [(1,1.0), (2,1.0), (3,1.0)], "initial_configuration": (1,1.0), "bounds": (-500,500)},
    "R00": {"arms": [(1,1.0), (2,1.0), (3,1.0)], "initial_configuration": (1,1.0)},
    "R110": {"arms": [(1,1.0)], "initial_configuration": (1,1.0)},
    "R111": {"arms": [(2,1.0)], "initial_configuration": (2,1.0)},
    "R112": {"arms": [(3,1.0)], "initial_configuration": (3,1.0)},
    "R120": {"arms": [(4,1.0)], "initial_configuration": (4,1.0)},
    "R121": {"arms": [(5,1.0)], "initial_configuration": (5,1.0)},
    "R122": {"arms": [(10,1.0)], "initial_configuration": (10,1.0)},
    "R11": {"arms": [(1,1.0), (2,1.0), (3,1.0)], "initial_configuration": (1,1.0)},
    "R12": {"arms": [(4,1.0), (5,1.0), (10,1.0)], "initial_configuration": (4,1.0)},
    "C01": {"arms": [(4,1.0), (5,1.0), (10,1.0)], "initial_configuration": (4,1.0), "bounds": (300,380)},
    "C02": {"arms": [(4,1.0), (5,1.0), (10,1.0)], "initial_configuration": (4,1.0), "bounds": (120,240)},
    "C110": {"arms": [(4,1.0)], "initial_configuration": (4,1.0)},
    "C111": {"arms": [(5,1.0)], "initial_configuration": (5,1.0)},
    "C112": {"arms": [(10,1.0)], "initial_configuration": (10,1.0)},
    "C30": {"arms": [(4,1.0), (5,1.0), (10,1.0)], "initial_configuration": (4,1.0), "bounds": (300,380), "record_decisions": True},
    "C310": {"arms": [(4,1.0), (5,1.0), (10,1.0)], "initial_configuration": (4,1.0), "bounds": (300,380), "preload_knowledge": True, "expert_preknowledge": [trace_140["worst_performer"][EwS], trace_110["worst_performer"][EwS]], "expert": "EwS"},
    "C311": {"arms": [(4,1.0), (5,1.0), (10,1.0)], "initial_configuration": (4,1.0), "bounds": (300,380), "preload_knowledge": True, "expert_preknowledge": [trace_140["worst_performer"][EXP3], trace_110["worst_performer"][EXP3]], "expert": "EXP3"},
    "C312": {"arms": [(4,1.0), (5,1.0), (10,1.0)], "initial_configuration": (4,1.0), "bounds": (300,380), "preload_knowledge": True, "expert_preknowledge": [trace_140["median_performer"][EwS], trace_110["median_performer"][EwS]], "expert": "EwS"},
    "C313": {"arms": [(4,1.0), (5,1.0), (10,1.0)], "initial_configuration": (4,1.0), "bounds": (300,380), "preload_knowledge": True, "expert_preknowledge": [trace_140["median_performer"][EXP3], trace_110["median_performer"][EXP3]], "expert": "EXP3"},
    "C314": {"arms": [(4,1.0), (5,1.0), (10,1.0)], "initial_configuration": (4,1.0), "bounds": (300,380), "preload_knowledge": True, "expert_preknowledge": [trace_140["best_performer"][EwS], trace_110["best_performer"][EwS]], "expert": "EwS"},
    "C315": {"arms": [(4,1.0), (5,1.0), (10,1.0)], "initial_configuration": (4,1.0), "bounds": (300,380), "preload_knowledge": True, "expert_preknowledge": [trace_140["best_performer"][EXP3], trace_110["best_performer"][EXP3]], "expert": "EXP3"},
    "H1": {"arms": [(4,1.0), (5,1.0), (10,1.0)], "initial_configuration": (4,1.0), "bounds": (175,230)},
    "E0": {"arms": [(3, 1.0), (3, 0.75), (3, 0.5), (3, 0.25), (2, 0.25), (2, 0.5), (2, 0.75), (2, 1.0), (1, 1.0), (1, 0.75), (1, 0.5), (1, 0.25)], "initial_configuration": (1,1.0), "bounds": (0,180)},
    "E01": {"arms": [(3,1.0)], "initial_configuration": (3,1.0)},
    "E02": {"arms": [(3,0.75)], "initial_configuration": (3,0.75)},
    "E03": {"arms": [(3,0.5)], "initial_configuration": (3,0.5)},
    "E04": {"arms": [(3,0.25)], "initial_configuration": (3,0.25)},
    "E05": {"arms": [(2,0.25)], "initial_configuration": (2,0.25)},
    "E06": {"arms": [(2,0.5)], "initial_configuration": (2,0.5)},
    "E07": {"arms": [(2,0.75)],"initial_configuration": (2,0.75)},
    "E08": {"arms": [(2,1.0)],"initial_configuration": (2,1.0)},
    "E09": {"arms": [(1,1.0)],"initial_configuration": (1,1.0)},
    "E10": {"arms": [(1,0.75)],"initial_configuration": (1,0.75)},
    "E11": {"arms": [(1,0.5)],"initial_configuration": (1,0.5)},
    "E12": {"arms": [(1,0.25)],"initial_configuration": (1,0.25)}
}

experimentsISOLA = {
    "E001": {"arms": [(3,1.0)], "initial_configuration": (3,1.0)},
    "E002": {"arms": [(6,1.0)], "initial_configuration": (6,1.0)},
    "E003": {"arms": [(8,1.0)], "initial_configuration": (8,1.0)},
    "E004": {"arms": [(11,1.0)], "initial_configuration": (11,1.0)},
    "E005": {"arms": [(13,1.0)], "initial_configuration": (13,1.0)},
    "E01": {"arms": [(3,1.0), (8,1.0), (13,1.0)], "initial_configuration": (3,1.0), "bounds": (140,300), "preload_knowledge": True, "expert_preknowledge": [trace_60["random_performer"][EXP3], trace_80["random_performer"][EXP3]], "expert": "EXP3"},
    
    "TEST": {"arms": [(1,1.0)], "initial_configuration": (1,1.0)}
}

experimentsECSA = {
    "E001": {"arms": [(3,1.0)], "initial_configuration": (3,1.0)},
    "E002": {"arms": [(6,1.0)], "initial_configuration": (6,1.0)},
    "E003": {"arms": [(8,1.0)], "initial_configuration": (8,1.0)},
    "E004": {"arms": [(11,1.0)], "initial_configuration": (11,1.0)},
    "E005": {"arms": [(13,1.0)], "initial_configuration": (13,1.0)},
    "E01": {"arms": [(3,1.0), (6,1.0), (8,1.0), (11,1.0), (13,1.0)], "initial_configuration": (3,1.0), "bounds": (140,300)}
}

def activate_experiment(experiment_dict):
    for key in experiment_dict.keys():
        bandit_args[key] = experiment_dict[key]


#bandit_args["arms"] = [(1,1.0), (2,1.0), (3,1.0)]
#bandit_args["initial_configuration"] = (1,1.0)

#We take control over if the bandit is actually called by SWIM or if we clean
def start(bandit_name,  dimmer, response_time, activeServers, servers, max_servers, total_util, arrival_rate, basic_throughput, opt_throughput, basic_response, opt_response, service_time, formula, experimentID, elapsedTime):
    activate_experiment(experimentsECSA[experimentID])
    
    # print(str(arrival_rate) + "arrival rate")
    # print(str(response_time) + "response time")
    # print(str(basic_throughput) + "basic_throughput")
    # print(str(opt_throughput) + "opt_throughput")
    # print(str(basic_response) + "basic response")
    # print(str(opt_response) + "opt response")
    # print(str(service_time) + "service time")

    # print(str(elapsedTime) + "internalinterfacecalled\n\n")
    # #print("arms are ")
    #print(bandit_args["arms"])
    if(bandit_args["bandit_instance"]):
        bandit = bandit_args["bandit_instance"]

        if(isinstance(bandit, Bandit)):
            print_rounds()
            #print_bounds()

           
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
    #NEED TO CONVERT CONF HERE NOW!
                reward, is_bound_diff, bound_delta = calculate_utility(arrival_rate, dimmer, response_time, max_servers, servers)

                #print(bandit.arm_reward_pairs)
                if(is_bound_diff and isinstance(bandit, UCB) and bandit_args["dynamic_bounds"]):
                #delta sigma (oldsum) vs sigma delta sum_i
                    print("\n\n\n\nAdjusted the rewards\n\n\n\n")

                    for arm in bandit.arms: bandit.arm_reward_pairs[arm][CUM_REWARD] = bandit.arm_reward_pairs[arm][CUM_REWARD] * bound_delta
                    print(bandit.arm_reward_pairs)


                #print("last action is ")
                #print(bandit.last_action)
                #print("\n\n\n")
                if(bandit.last_action != (servers, dimmer)): 
                    raise RuntimeError("Previously chosen configuration " + str(bandit.last_action) + " is not reflected in SWIM's" + str((servers,dimmer)))
               
                new_choice = bandit.start_strategy(reward[0])
                print("returned arm " + str(new_choice))
                #bandit.visualize()
                #print("new choice is " + str(new_choice))

                if(response_time > RT_THRESH): #is the floor dirty
                    #clean
                    #print("\nCleaning in progress -----")
                    janitor = Cleaner()

                    bandit_args['cleaning'] = True

                    bandit_args["stored_choice"] = new_choice
                    bandit_args['round_counter'][0]+=1
                    return janitor.clean(servers,dimmer)
                else: #dont need to clean
                    #print("Cleaning was not necessary")
                    bandit_args['round_counter'][1]+=1
                    if(bandit_args["record_decisions"]): 
                        save_to_pickle(bandit, bandit.name + str(formula) + "_" + str(bandit_args["start_time"]))
                    converted =  convert_conf(new_choice, (servers,dimmer))
                    #print("converted is " + str(converted))
                    return converted
    else:
        #print("first this")
        #print((bandit_name,formula))
        bandit_args["bandit_instance"] = init_bandit(bandit_name,formula)
        return start(bandit_name,  dimmer, response_time, activeServers, servers, max_servers, total_util, arrival_rate, basic_throughput, opt_throughput, basic_response, opt_response, service_time, formula, experimentID, elapsedTime)
    #start_strategy: takes swim variables, returns swim tactics





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
