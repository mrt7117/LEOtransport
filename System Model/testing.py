# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 09:11:03 2022

@author: trlon
"""

#import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.cm as cm
#import datetime
#%matplotlib inline




class Passengers:
    def __init__(self,train_capacity,daily,hhourly,lf,trains_per_hhour):
        self.hhourly = hhourly
        self.daily = daily
        self.train_capacity = train_capacity
        self.lf = lf 
        self.trains_per_hhour = trains_per_hhour
passengers = Passengers(0,10000,300,0,0)




time_stamp = pd.date_range("00:00", "23:30", freq="30min").time

# Import passenger data, and generate Oxford data set for 15 minute intervals
underground_sample = pd.read_csv("data/underground_10_day_sample_reordered.csv")
sample_df = pd.DataFrame(underground_sample)
underground_overall = sample_df.iloc[0:267:,4:100].sum(axis=0)
ox_estimate = (passengers.hhourly/3950251)*underground_overall


# Generate data for 30 minute intervals
ox_hhourly = np.zeros(48)
for i in range(48):
    ox_hhourly[i] = ox_estimate[2*i] + ox_estimate[2*i+1]


#Plot data
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(time_stamp,ox_hhourly)
# plot = ox_hhourly.plot(kind='bar')
plt.xticks(rotation=90)
plot.set_xticklabels(time_stamp)
plt.xticks(np.arange(0, 47, 2))
plt.xlabel('time')
plt.ylabel('Number of passengers\nin 30 minute interval')
plt.show()

passengers.hhourly = ox_hhourly

print(passengers)