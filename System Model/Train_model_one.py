# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 10:13:03 2022

@author: trlon
"""



# This is a function that represents the overall system model.
# It contains the constituent models for the system eg. Rosa's generation model,
# my investment model etc so they can be called by each other and insights be
# produced back in the main script 'Initialisation_and_insights'.

#%% 

#Create loop here
def system_model(costs,finances,passengers,PV_farm_inputs):

    #%%       
    #Call functions to generate model

    import passenger_distribution
    passengers = passenger_distribution.passenger_distribution(passengers)
    
    #%%
    #State of train. Determine number of services, load factor etc.
    
    import state_of_train
    passengers = state_of_train.state_of_train(passengers)
    
    
    #%%
    #Energy Generation
    import PV_farm_ref
    PV_farm_ref = PV_farm_ref.Produce_PV_Farm_Structure(PV_farm_inputs)
    
    #%%
    
    import npv
    finances = npv.financing_model(passengers,costs,finances)
        
    
    #%%

    return(costs,finances,passengers,PV_farm_ref)






   
