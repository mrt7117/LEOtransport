# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 16:45:02 2022

@author: trlon
"""


#import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.cm as cm
#import datetime
#%matplotlib inline

def passenger_model(passengers):
    
    #Create time steps
    time_stamp = pd.date_range("00:00", "23:30", freq="30min").time
    
    # Import passenger data, and generate Oxford data set for 15 minute intervals
    underground_sample = pd.read_csv("data/underground_10_day_sample_reordered.csv")
    sample_df = pd.DataFrame(underground_sample)
    underground_overall = sample_df.iloc[0:267:,4:100].sum(axis=0)
    ox_estimate = (passengers.hhourly/3950251)*underground_overall
    
    
    # Generate data for 30 minute intervals
    ox_hhourly = pd.Series(48)
    for i in range(48):
        ox_hhourly[i] = ox_estimate[2*i] + ox_estimate[2*i+1]
    
    
    #Plot data
    ax1 = plt.subplot(3,1,1)
    plot = ox_hhourly.plot(kind='bar')
    
    plt.xticks(rotation=90)
    plot.set_xticklabels(time_stamp)
    plt.xticks(np.arange(0, 47, 2))
    plt.xlabel('time')
    plt.ylabel('Number of passengers\nin 30 minute interval')
    plt.show()
    
    
    
    
    #%%
    #Model number of passengers on train

    
    T = len(ox_hhourly)
    pot = np.zeros((T,1))  # passengers on train
    pas = np.zeros((T,1))  # passengers waiting at station
    lf = np.zeros((T,1))
    hhourly_capacity = np.zeros((T,1))
    
    
    for j in range(T):
        if ox_hhourly[j] > passengers.train_capacity:
             hhourly_capacity[j] = 2*passengers.train_capacity
        else:
            if ox_hhourly[j] < 20 :
                hhourly_capacity[j] = 0
            else:
                hhourly_capacity[j] = passengers.train_capacity
            
        pot[j] = min(hhourly_capacity[j], ox_hhourly[j])
        pas[j] = ox_hhourly[j] - pot[j]
        
        if pot[j] == 0:
            lf[j] = 0
        else: 
            lf[j] = pot[j]/hhourly_capacity[j]
    
    
    
    
    
    #%%
    # Create Dataframe
    
    #Convert variables into suitable types
    trains_per_hhour = (1/passengers.train_capacity)*hhourly_capacity
    trains_per_hhour = np.array(trains_per_hhour, dtype='int')
    trains_per_hhour = trains_per_hhour.tolist()
    ox_hhourly = np.array(ox_hhourly)
    # ox_hhourly = ox_hhourly.tolist()
    lf = lf.tolist()
    passengers.hhourly = np.array(ox_hhourly, dtype='int')
    
    
    # Convert to dataframe
    d = {'time':time_stamp,'passengers':ox_hhourly,'trains_per_hhour':trains_per_hhour,'load_factor':lf}
    df = pd.DataFrame(d)
    df = df.set_index('time')
    df.passengers = np.array(df.passengers, dtype='int')
    print(df.head())
    
    
    #Plot
    #passengers = df["passengers"]
    # ax1 = plt.subplot(2,1,1)
    # p1 = plt.plot(passengers)
    # ax1.legend(loc='upper left')
    # plt.show()
    
    # ax2 = plt.subplot(2,1,2)
    # p2 = plt.plot(lf, label='Load Factor')
    # p3 = plt.plot(trains_per_hhour, label='Number of Trains per half hour')
    # ax2.legend(loc='upper left')
    # plt.show()


    trains_per_hhour =  np.array(trains_per_hhour)


            

    passengers.hhourly = passengers.hhourly
    passengers.lf = lf
    passengers.trains_per_hhour = trains_per_hhour
    
    print(passengers)
    return passengers

