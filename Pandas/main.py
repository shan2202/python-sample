#! /opt/anaconda3/bin/ python

import pandas as pd
import numpy as np

#Create a dictionary to store Cars data
cars = {'Brand': ['Honda', 'Toyota', 'Ford'],
        'Price': [22000,25000,27000]
        }
#Create a dataframe using dictionary
cars_df = pd.DataFrame(cars, columns=['Brand','Price'], index=['car 1','car 2','car 3'])

#Add a new column
year = [2010,2011,2008]
cars_df['Year']=year

cars_df.insert(1,'Model',['civic','Prius','Focus'],True)
#insert new row with new Index
cars_df.loc['car 4']=['Hyundai','Avante',20000,2010]
#update the existing row based on Index
cars_df.loc['car 3']=['Suzuki','Swift',26000,2013]

#Calc new value based on existing column and insert as new column
cars_df['Discount']=cars_df['Price']*0.1
cars_df['Discounted Price']=cars_df['Price']-cars_df['Discount']

print(cars_df)
