import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/sitan/OneDrive/Desktop/Python/Raw_Data_File/Gap10.csv')
# df2 = pd.read_csv('C:/Users/sitan/OneDrive/Desktop/Python/Raw_Data_File/Gap_First.csv')

#print(df)  #this will show all the data which is present in our file 

#print(df.head())  #Using it I can See first 5 row in data Set

#print(df.shape)  #(number of row, number of coloumn)
#print(df.columns) #(Show all columns Name with type of data)
#print(df.dtypes)  #(It will show you each column data type)
print(df.info())  #(gives full details of each coloumn)

country_df = df['country']  #(We are storing country coloumn in data variable)

print(country_df.head())  #(This will show you country first five data)

print(country_df.tail()) #(show the last five coloumn)

subset = df[['country','year','lifeExp','pop']]  #(create ab subset of main dataSet)

print(subset.head())  #(show 5 data from the subset of data)

print(subset.tail())

print(df.loc[0])  #(as we know python index start from "0" index, Loc[] print a particular index that we want to see)

print(df.loc[9])   #(access 10 coloumn from the data file)