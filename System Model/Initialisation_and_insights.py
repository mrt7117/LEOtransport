# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 14:17:40 2022

@author: trlon
"""
from dataclasses import dataclass
from typing import NamedTuple
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import datetime
#%matplotlib inline


#%%
# SECTION 1
# Define Variables Here
class Costs:
    def __init__(self,ticket,railway,generation,storage,operation):
        self.ticket = ticket
        self.railway = railway
        self.generation = generation
        self.storage = storage
        self.operation = operation
costs = Costs(10,200000000,10000000,20000000,0)

class Finances:
    def __init__(self,dr,lifetime,pv,npv,irr):
        self.dr = dr
        self.lifetime = lifetime
        self.pv = pv
        self.npv = npv
        self.irr = irr
finances = Finances(0.1,30,0,0,0)

class Passengers:
    def __init__(self,hhourly,daily,train_capacity,lf,trains_per_hhour,pot,pas):
        self.hhourly = hhourly
        self.daily = daily
        self.train_capacity = train_capacity
        self.lf = lf 
        self.trains_per_hhour = trains_per_hhour
        self.pot = pot
        self.pas = pas
passengers = Passengers(0,10000,300,0,0,0,0)


class PV_farm_inputs:
    def __init__(self,DF_HOUR_1MW,CAPACITY,POWER_INTENSITY):
        self.DF_HOUR_1MW = DF_HOUR_1MW
        self.CAPACITY = CAPACITY
        self.POWER_INTENSITY = POWER_INTENSITY

df_epr1MW = pd.read_csv("data/ninja_pv_eynsham_PR_1MW.csv", index_col=0,parse_dates=True,dayfirst=True, delimiter=",")
#import value used to turn area into power capacity
#power_intensity_epr = 90 #W/m2
#Capacity_ref = 1e6 #reference capacity of 1MW
PV_farm_inputs = PV_farm_inputs(df_epr1MW,1e6,90)



#%%
# SECTION 2 - DON'T CHANGE EXCEPT TO LOOP AROUND
# Run Train model with given inputs

import Train_model_one
[costs,finances,passengers,PV_farm_ref] = Train_model_one.system_model(costs,finances,passengers,PV_farm_inputs)


#%%
# SECTION 3
# Call your plotting function to make insights on data

import present_value_plot
present_value_plot.present_value_plot(finances)
