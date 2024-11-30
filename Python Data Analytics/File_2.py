import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/sitan/OneDrive/Desktop/Python/Raw_Data_File/Gap10.csv')

# print(df)

#Get last row
print(df.tail(n=1))  #both are same 
print(df.tail(1))


#select The first, 5th, 9th row from the data file using LOC
print(df.loc[[0,5,9]])


#get details about the 2nd and 10th row
print(df.iloc[1])
print(df.iloc[9])

#using "-1" get last row
print(df.iloc[-1])  #( With iloc. we can pass in the -1 to get last row---- but samething we can't do the loc)

#select The first, 5th, 9th row from the data file using iLOC
print(df.iloc[[0,5,9]])




'''
       SubSetting Coloumn

-> The Python slicing syntax uses a colon, :
-> If we have just a colon, the attribute refers to everything.
-> So, if we just want to get the first column using the loc or iloc syntax,
 we can write something like df.locc[:,[columns]] to subset the column(s).

    *# Subset Columns with loc
    *# note the position of th colon
    *# it is ussed to select all rows
'''

subset = df.loc[:,['year','pop','lifeExp']]
print(subset.head()) 

'''
*# Subset columns with iloc
*# iloc will alow us to use integers
*# -1 will select the last column
'''

subset = df.iloc[:,[2,4,-1]]
subset = df.iloc[:,['year','pop']]  #Wrong
print(subset.head())



'''
*# creeate a range of integers from 0 to 4 inclusive
'''
small_range = list(range(5))
print(small_range)



'''
*# subset the dataframe with the small_range which was created...
'''
subset = df.iloc[:,small_range]
print(subset.head())