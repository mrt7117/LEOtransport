# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 08:34:39 2022

@author: trlon
"""

#import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.cm as cm
#import datetime
#%matplotlib inline

def passenger_distribution(passengers):
    
    #Create time steps
    time_stamp = pd.date_range("00:00", "23:30", freq="30min").time
    
    # Import passenger data, and generate Oxford data set for 15 minute intervals
    underground_sample = pd.read_csv("data/underground_10_day_sample_reordered.csv")
    sample_df = pd.DataFrame(underground_sample)
    underground_overall = sample_df.iloc[0:267:,4:100].sum(axis=0)
    ox_estimate = (passengers.daily/3950251)*underground_overall
    
    
    # Generate data for 30 minute intervals
    ox_hhourly = np.zeros(48)
    for i in range(48):
        ox_hhourly[i] = ox_estimate[2*i] + ox_estimate[2*i+1]
    
    
    #Plot data
    # plt.subplot(3,1,1)
    # plot = ox_hhourly.plot(kind='bar')
    # plt.xticks(rotation=90)
    # plot.set_xticklabels(time_stamp)
    # plt.xticks(np.arange(0, 47, 2))
    # plt.xlabel('time')
    # plt.ylabel('Number of passengers\nin 30 minute interval')
    # plt.show()

    passengers.hhourly = ox_hhourly

    return passengers