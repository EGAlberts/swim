/*******************************************************************************
 * Simulator of Web Infrastructure and Management
 * Copyright (c) 2016 Carnegie Mellon University.
 * All Rights Reserved.
 *  
 * THIS SOFTWARE IS PROVIDED "AS IS," WITH NO WARRANTIES WHATSOEVER. CARNEGIE
 * MELLON UNIVERSITY EXPRESSLY DISCLAIMS TO THE FULLEST EXTENT PERMITTED BY LAW
 * ALL EXPRESS, IMPLIED, AND STATUTORY WARRANTIES, INCLUDING, WITHOUT
 * LIMITATION, THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
 * PURPOSE, AND NON-INFRINGEMENT OF PROPRIETARY RIGHTS.
 *  
 * Released under a BSD license, please see license.txt for full terms.
 * DM-0003883
 *******************************************************************************/

#include "DummyAdaptationManager.h"
#include "managers/adaptation/UtilityScorer.h"
#include "managers/execution/AllTactics.h"
#include <Python.h>

using namespace std;

Define_Module(DummyAdaptationManager);

/**
 * Dummy adaptation
 *
 * RT = response time
 * RTT = response time threshold
 *
 * - if RT > RTT, add a server if possible, if not decrease dimmer if possible
 * - if RT < RTT and spare utilization > 1
 *      -if dimmer < 1, increase dimmer else if servers > 1 and no server booting remove server
 */
Tactic* DummyAdaptationManager::evaluate() {
    MacroTactic* pMacroTactic = new MacroTactic;
    // Model* pModel = getModel();
    // const double dimmerStep = 1.0 / (pModel->getNumberOfDimmerLevels() - 1);
    // double dimmer = pModel->getDimmerFactor();
    // double spareUtilization =  pModel->getConfiguration().getActiveServers() - pModel->getObservations().utilization;
    // bool isServerBooting = pModel->getServers() > pModel->getActiveServers();
    // bool isServerRemoving = pModel->getServers() < pModel->getActiveServers();
    // double responseTime = pModel->getObservations().avgResponseTime;
    // double totalUtilization = pModel->getObservations().utilization; //I think this is correct
    // double activeServers = pModel->getConfiguration().getActiveServers();
    // double servers = pModel->getServers();
    // double maxServers = pModel->getMaxServers();
    // double arrivalRate = (pModel->getEnvironment().getArrivalMean() > 0) ? (1 / pModel->getEnvironment().getArrivalMean()) : 0.0;
    // PyObject *pModule, *pFunc;
    // PyObject *pArgs, *pValue, *pElement, *pName;

    // int i;


    // Py_Initialize();
    // pName = PyUnicode_DecodeFSDefault("multiply");
    // /* Error checking of pName left out */

    // pModule = PyImport_Import(pName);
    // Py_DECREF(pName);

    // if (pModule != NULL) {
    //     pFunc = PyObject_GetAttrString(pModule, "multiply");
    //     /* pFunc is a new reference */

    //     printf("got here");}
    
    return pMacroTactic;

}
