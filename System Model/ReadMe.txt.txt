Transport LEO System model. Thomas Long, Rosa Arthur, Charles Davies, Zhenqin Du

Main files:
1. Initialisation_and_insights.py
2. Train_model_one.py
These are the files that run the overall system. 
All other files are files that contain sub-system are owned and edited by their creator.


1. Initialisation_and_insights.py

SECTION 1: This is where initial variables are designated. If a variable has not been determined yet, give it the value 0. The idea here is to have a class for each section of the project. This keeps the structure of the program simpler as there are fewer variables being called into and out of functions. Feel free to add new classes for your subsystem

SECTION 2: This is where the system model function is called. If you want to loop over certain variables or to apply an optimisation this is where to look!

SECTION 3: Now you have access to all of the train data, create your own plotting function to analyse the data of interest



2. Train_model_one.py

This is where each of the sub-systems are called as functions. In order to integrate each sub-system:
-Embedd your code in a function 
-Add it to the folder
-In Train_model_one.py import the file and then call the function


Remember to set the input and ouput variables to functions in Initialisation_and_insights.py, Train_model_one.py and your own function.




