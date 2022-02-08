# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 13:08:51 2022

@author: trlon
"""

#import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.cm as cm
#import datetime
#%matplotlib inline

def present_value_plot(finances):
    
    x = np.array(range(finances.lifetime+1))
    y = np.array(finances.pv)
    plt.title("Present Value of Transport System")
    plt.xlabel("Time (years)")
    plt.ylabel("Present Value (£)")
    plt.plot(x, y, color = "red", marker = "o", label = "Array elements")
    plt.legend()
    plt.show()
    
    
    # # Plot net present value
    # plt.plot(range(finances.duration+1),pv)
    # plt.axhline(0, color='gray')    
    # plt.grid()
    # plt.xlabel('Number of years')
    # plt.ylabel('Present Value (£M)')
    