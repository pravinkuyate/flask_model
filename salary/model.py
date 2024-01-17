import pickle 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

dataset =pd.read_csv(r"C:\Users\pravinkuyate\ML CLASS\flask\salary\hiring.csv")
dataset['experience'].fillna(0,inplace=True)

dataset['test_score'].fillna(dataset['test_score'].mean(),inplace=True)

x=dataset.iloc[:,:3]

def convert_to_int(word):
    word_dict={'one':1,"two":2,"three":3,'four':4,'five':5,'six':6,'seven':7,
               'seven':7,'eight':8,"nine":9,"ten":10,"eleven":11,"twelve":12,"zero":0,0:0}
    return word_dict[word]

x['experience']=x['experience'].apply(lambda x: convert_to_int(x))
y=dataset.iloc[:,-1]


regressor=LinearRegression()
regressor.fit(x,y)

pickle.dump(regressor,open('model.pkl','wb'))

model=pickle.load(open('model.pkl','rb'))
print(model.predict([[2,10,6]]))
    
