# %load q01_read_data/build.py
import yaml
import os
#print(os.getcwd())
#os.chdir('/home/notebooks/data')

def read_data():
    data={}
    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    #with open('ipl_match.yaml','r') as f:
        
    data=yaml.load(open('./data/ipl_match.yaml','r'))
        

    return data









