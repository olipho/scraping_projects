# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 22:08:32 2020

@author: Dave
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_raw = pd.read_csv(r'C:\Users\Dave\Documents\Dave\Data_Analytics_Science\Python\parkrun1.csv')


#convert imported csv which is a single column of data to list so data can be put into array
df_list = df_raw['parkrun_summary'].tolist()

#find column names from csv
column_names = df_list[0:5]

#The last column has no name so added in here. Could've used append.
column_names.insert(5, 'View')

#Convert list into array as dataframe
df = pd.DataFrame(np.array(df_list).reshape(-1, 6), columns = list(column_names))

#find list length
list_len = len(df)

#remove first row of data from dataframe so headers aren't there
df_data = df.iloc[1:list_len]

#need to reset indices
df_data1 = df_data.reset_index()
list1 = df_data1['Runs'].tolist()

df_data2 = df.iloc[1:11]
list2 = df_data2['Runs'].tolist()

#plotting 1st graph
ax = plt.subplot()
plt.bar(range(len(list2)), list2)
ax.set_xticks(range(len(list2)))
ax.set_xticklabels(df_data2['Event'], rotation = 'vertical')
plt.title('parkrun Summary Stats')
#sets two sets of y-axis, followed by second plot
bx = ax.twinx()
bx = plt.subplot
plt.plot(range(len(df_data2['Best Time'])), df_data2['Best Time'], color = 'green')
plt.show()

#quesitons - why are y axes upside down? Why is the line straight?

#print(columns)
print(df_data1.head(10))
#print(df_data1.info())
#print(column_names)
#print(df_data1['Best Position Overall'])
#plt.gca().invert_yaxis()










#event = []

#for item in df_raw:
#    event.append(df_raw.iloc[0::6,:]) 
    
    
    
#print(event)
    