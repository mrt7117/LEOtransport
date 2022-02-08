# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 13:32:10 2022

@author: trlon
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.cm as cm
#import datetime
#%matplotlib inline

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


#    def __init__(self,hhourly,daily,train_capacity,lf,trains_per_hhour,pot,pas):
#    (ticket,railway,generation,storage,operation)
import Train_model_one

finances1 = Train_model_one.system_model(Costs(10,200000000,10000000,20000000,0),finances,passengers)
print(finances1.irr)
#%%
finances2 = Train_model_one.system_model(Costs(10,220000000,10000000,20000000,0),finances,passengers)
print(finances2.irr)
#%%
finances3 = Train_model_one.system_model(Costs(10,260000000,10000000,20000000,0),finances,passengers)
print(finances3.irr)

y = np.array(finances.pv)

x = np.array(range(finances1.lifetime+1))
plt.plot(x, y, color = "red", marker = "o", label = "Array elements")

x = np.array(range(finances2.lifetime+1))
plt.plot(x, y, color = "blue", marker = "o", label = "Array elements")

x = np.array(range(finances3.lifetime+1))
plt.plot(x, y, color = "blue", marker = "o", label = "Array elements")

plt.title("Present Value of Transport System")
plt.xlabel("Time (years)")
plt.ylabel("Present Value (£)")
plt.legend()
plt.show()

    

import pv_plot
# pv_plot.pv_plot(finances1)
# pv_plot.pv_plot(finances2)
# pv_plot.pv_plot(finances3)
# plt.show()

#import