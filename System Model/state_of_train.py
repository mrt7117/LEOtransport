# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 12:51:39 2022

@author: trlon
"""

#import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.cm as cm
#import datetime
#%matplotlib inline

def state_of_train(passengers):
    
    #Model number of passengers on train
    T = len(passengers.hhourly)
    pot = np.zeros((T,1))  # passengers on train
    pas = np.zeros((T,1))  # passengers waiting at station
    lf = np.zeros((T,1))
    hhourly_capacity = np.zeros((T,1))
    
    
    for j in range(T):
        if passengers.hhourly[j] > passengers.train_capacity:
             hhourly_capacity[j] = 2*passengers.train_capacity
        else:
            if passengers.hhourly[j] < 20 :
                hhourly_capacity[j] = 0
            else:
                hhourly_capacity[j] = passengers.train_capacity
            
        pot[j] = min(hhourly_capacity[j], passengers.hhourly[j])
        pas[j] = passengers.hhourly[j] - pot[j]
        
        if pot[j] == 0:
            lf[j] = 0
        else: 
            lf[j] = pot[j]/hhourly_capacity[j]
            
            
    passengers.train_capacity = hhourly_capacity
    passengers.lf = lf
    passengers.pot = pot
    passengers.pas = pas
    passengers.trains_per_hhour = hhourly_capacity
        
    return passengers
            
        