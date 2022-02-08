# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 10:25:14 2022

@author: trlon
"""


#import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.cm as cm
#import datetime
#%matplotlib inline


def financing_model(passengers,costs,finances):
    pv = np.zeros(finances.lifetime+1)
    npv = 0
    
    for i in range(1,finances.lifetime+1):        
        discount_factor = 1/((1+finances.dr)**i)
        
            
        if i == 1 or i == 2 or i ==3 or i ==4:
            pv[i] = pv[i-1] - ((costs.railway+costs.generation+costs.storage)/4)*discount_factor
            # print(pv[i])
        else:
            pv[i] = pv[i-1] + costs.ticket*passengers.daily*365*discount_factor - costs.operation*365*discount_factor
            # print(pv[i])
        if pv[i] > 0 :
            finances.irr = i
            
    import bisect
    index = bisect.bisect_left(pv, 0)
            
        
    finances.npv = pv[finances.lifetime]
    finances.pv = pv
    finances.irr = index
    
    
    return finances
        