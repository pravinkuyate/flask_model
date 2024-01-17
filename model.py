import pickle 
import pandas as ps
import matplotlib.pyplot as plt

import numpy as np

dataset =pd.read_csv("hiring.csv")
dataset['experience'].fillna(0,inplace=True)

dataset['test_score'].fillna(dataset['test_score'].mean(),inplace=True)

x=dataset.iloc[:,:3]

def convert_to_int(word):
    word_dict
    
