# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 14:56:35 2022

@author: Charles Davies
"""

from dataclasses import dataclass
from typing import NamedTuple
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import datetime
#%matplotlib inline


def Produce_PV_Farm_Structure(PV_farm_inputs):
    DF_HOUR_1MW = PV_farm_inputs.DF_HOUR_1MW
    CAPACITY = PV_farm_inputs.CAPACITY
    POWER_INTENSITY = PV_farm_inputs.POWER_INTENSITY
    
    capacity_ratio = int(CAPACITY/1e6) #capacity in MW
    #scale up 1MW data figure
    DF_HOUR=DF_HOUR_1MW.multiply(capacity_ratio)
    
    DF_DAY = DF_HOUR.resample("D").sum()
    DF_YEAR = DF_HOUR.resample("Y").sum()
    ANNUAL_OUTPUT = DF_YEAR["electricity (kWh)"].item()
    AREA = CAPACITY/(POWER_INTENSITY)
    
    @dataclass
    class User(NamedTuple):
        name: str
    
    
    # determine the different aspects of the PV_Farm, and the nature of each aspect (float, string etc)
    class PV_Farm(NamedTuple):
        #capacity in W
        Capacity: float
        #dataframe of hourly output
        df_hour: pd.DataFrame
        #dataframe of daily output
        df_day: pd.DataFrame
        #annual production of energy (kWh)
        Annual_Output: float
        #area in metres squared
        Area: float
    
    
    
    PV_Farm_Out = PV_Farm(Capacity=CAPACITY,df_hour=DF_HOUR,df_day=DF_DAY,Annual_Output=ANNUAL_OUTPUT,Area=AREA)
    
    
    
    return PV_Farm_Out