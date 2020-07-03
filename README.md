# scraping_fun

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 06:09:48 2020

@author: Dave
"""
import pandas as pd
import matplotlib.pyplot as plt
#pd.set_option('display.max_colwidth', -1)
#plt.close('all')
data = pd.read_csv(r'C:\Users\Dave\Documents\Dave\Data_Analytics_Science\Python\raw.csv')
# Create new columns to group European, Asian and African data respectively
data['Europe'] = data['European Union EU15'] + data['European Union EU8'] + data['European Union EU2'] + data['European Union Other'] + data['Other Europe']
data['Asia'] = data['Middle East and Central Asia'] + data['East Asia'] + data['South Asia'] + data['South East Asia']
data['Africa'] = data['North Africa'] + data['Sub-Saharan Africa']
# For plotting line graph starts here
bx = plt.subplot()
# Take every third row of data
every_3rd = data.iloc[2::3, :] 
# Display lines on chart
plt.plot(range(len(every_3rd)), every_3rd['Europe'], color='green')
plt.plot(range(len(every_3rd)), every_3rd['Asia'], color='blue')
plt.plot(range(len(every_3rd)), every_3rd['Africa'], color='red')
plt.plot(range(len(every_3rd)), every_3rd['Oceania'], color='orange')
plt.plot(range(len(every_3rd)), every_3rd['North America'], color='black')
plt.plot(range(len(every_3rd)), every_3rd['Central and South America'], color='purple')

legend_labels = (['Europe', 'Asia', 'Africa', 'Oceania', 'North America', 'Central and South America'])
plt.legend(legend_labels, loc = 0)

x_axis_values = every_3rd['Date'].tolist()
bx.set_xticks(range(len(every_3rd['Date'])))
bx.set_xticklabels(x_axis_values, rotation='vertical') 
plt.xlabel('Period')
plt.ylabel('Number of People')
plt.title('Number of newly created NI numbers by count of people from outside of UK by world region')
#plt.show()
# Save figure, second parameter ensures the output image isn't cropped
plt.savefig('NI_stats.jpg', bbox_inches='tight')
