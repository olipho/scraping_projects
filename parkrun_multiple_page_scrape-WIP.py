#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 21:54:28 2020

@author: Dave
"""

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1'}

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 20:58:30 2020

@author: Dave
"""

import requests
from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd
import numpy as np
import requests
import re
import matplotlib.pyplot as plt

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1'}

# Need to enter individual's parkrun id
parkrun_id = '1163526'

prefix = 'https://www.parkrun.org.uk/'
# Commented out below so not run by mistake (n.b. 403 error)
webpage_response = requests.get('https://www.parkrun.org.uk/results/athleteresultshistory/?athleteNumber=' + parkrun_id, headers = headers)

webpage = webpage_response.content
#parse_only = SoupStrainer("a",{'class': 'review_link'})
soup = BeautifulSoup(webpage, "html.parser", parse_only=SoupStrainer('a'))
#print(soup)

links = []

# This will scrape the page based on the individual's parkrun id entered above
search_str = 'athletehistory?athleteNumber=' + parkrun_id

# Output below : I have moved the code into the next cell but do not want to run this cell again 
# as it may get me a 403 FORBIDDEN again. 


# In[2]:


# Adds all link from soup onto links list
for link in soup: 
    if link.has_attr('href'):
        links.append(link['href'])
#print(links)

# Filters out links other than relevant event link string using search_str
event_links = []
for a in links:
    if search_str in a:
        event_links.append(a)
        #print(link['href'])
print(event_links)   


# In[3]:


soup_name = BeautifulSoup(webpage, "html.parser", parse_only=SoupStrainer('h2'))
print(soup_name)

for i in soup_name:
    runner_name = i.get_text(',')

print(runner_name)


# In[115]:


from itertools import repeat

#follow each link:
run_data = []
event_list = []

for course in event_links: 

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1'}
    webpage_new = requests.get(course, headers = headers)
    new_soup = BeautifulSoup(webpage_new.content, "html.parser") #, parse_only=SoupStrainer('table')
    #pretty_soup = new_soup.prettify()
    #print(pretty_soup)
    running = new_soup.find_all('td')

    for r in running[16:]:     # Don't need first 16 items from each page
            run_data.append(r.get_text(','))
#            results_text = r.get_text(',')
    #print(results_text)

    #print(results[1:2])

    split_text = results_text.split(',')
    
    soup_h3 = new_soup.find_all('h3')

    for j in soup_h3:
        venue_string = j.get_text(',')
        venue_name = venue_string.split(' parkrun')[0]
    
    soup_h2 = new_soup.find_all('h2')     
    
    for k in soup_h2:
        run_string = k.get_text(',')
        venue_count =  run_string.split(' ')[3]
    
    #convert venue_count to integer format:
        venue_count = int(venue_count)
        
        #add venue_name venue_count times to the list
        event_list.extend(repeat(venue_name, venue_count))

print(run_data)
print(df.head())


# In[44]:


# To count how many of each course in the df and to produce graph
course_count = dict()
for i in event_list:
  course_count[i] = course_count.get(i, 0) + 1
print(course_count)


# In[63]:


plt.bar(range(len(course_count)), list(course_count.values()), align='center')
plt.xticks(range(len(course_count)), list(course_count.keys()))
plt.title('Count of parkrun venues for ' + runner_name)
#plt.set_xticklabels('Venue Name')
plt.show()


# In[64]:


years_tuple = ('2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020')

run_data_clean = []
new_list = []
        
for idx, val in enumerate(run_data):
    if val in years_tuple:
        print(idx, val)
        run_data_clean.append(idx)
        run_data_clean.append(idx + 1)
        run_data_clean.append(idx + 2)
        
        
print(run_data_clean)

for idx, val in enumerate(run_data):
    if idx in run_data_clean:
        print(idx)
    else:
        new_list.append(val)

print(new_list)


# In[116]:


import datetime, time

column_names = ['Run Date', 'Run Number', 'Position', 'Time', 'Age Grade', 'PB?'] # , 'Event Name'

df = pd.DataFrame(np.array(new_list).reshape(-1, 6), columns = list(column_names))

soup_name = BeautifulSoup(webpage, "html.parser", parse_only=SoupStrainer('h2'))
#convert list into dataframe column
df.loc[:,'Event Name'] = event_list
print(df.head(30))


# In[118]:


time_list = [] # list created to store times as strings
seconds_list = [] # list created to store times in seconds to allow calculation of standard dev
time_list = df.loc[:, 'Time'].tolist()

#Convert time into seconds to enable calculation of stdev
def get_sec(time_str):
    m, s = time_str.split(':')
    return int(m) * 60 + int(s)

for i in time_list:
    seconds = get_sec(i)
    seconds_list.append(seconds)
print(seconds_list)


# In[254]:


# Mean and standard deviation calcs for times
#mean_time = df.loc[:,'Time'].mean()
df.loc[:,'Time_seconds'] = seconds_list
mean_time_s = df.loc[:,'Time_seconds'].mean()
st_dev = round(np.std(seconds_list), 2)

# Max and min values for times
max_value = df.loc[:,'Time'].max()
min_value = df.loc[:,'Time'].min()
#print('Mean time = ', mean_time)
print('Mean time in seconds = ', mean_time_s, 'seconds')
print('Standard Deviation = ', st_dev, 'seconds')
print('Max value = ', max_value)
print('Min value = ', min_value)
#print(df_data2.info())


# In[303]:


#convert mean time in seconds back to hours, minutes, seconds
#full hours

##### DRY - use last function as input for second last and again for first (can't get this to work so commented out)
def min_conv(time_seconds):
    converted_h = int(time_seconds / 3600)
    #remainder hours to be converted to minutes
    converted_h_rem = time_seconds % 3600
    #print(converted_h_rem)
    #full minutes
    return str(int(converted_h_rem / 60))

def sec_conv(time_seconds):
    converted_h = int(time_seconds / 3600)
    #remainder hours to be converted to minutes
    converted_h_rem = time_seconds % 3600
    #full minutes
    converted_m = str(int(converted_h_rem / 60))
    #remainder minutes to be converted to seconds, rounded to 2dp
    return str(int(converted_h_rem % 60))

#def sec_conv(time_seconds):
#    remainder minutes to be converted to seconds, rounded to 2dp
#    converted_m = float(min_conv(time_seconds)) % 60
#    print(converted_m)
#    return str(int(converted_m))

def time_conv(time_seconds):
    converted_h = int(time_seconds / 3600)
    #remainder hours to be converted to minutes
    converted_h_rem = time_seconds % 3600
    #full minutes
    converted_m = int(converted_h_rem / 60)
    #remainder minutes to be converted to seconds, rounded to 2dp
    converted_m_rem = int(converted_h_rem % 60)
    return '0{0}:{1}:{2}'.format(converted_h, converted_m, converted_m_rem)

#print(time_conv(1250))
#print(min_conv(1250))
#print(sec_conv(1250))
 

# As much as it isn't particularly meaningful to calculate summary statistics for my best times, it's a useful learning exercise.
Mean_Time_string = 'The mean of ' + runner_name + ' times is ' +  time_conv(mean_time_s) + ' or ' + min_conv(mean_time_s) + ' minutes and ' + sec_conv(mean_time_s) + ' seconds and the standard deviation is ' + min_conv(st_dev) + ' minutes and ' + sec_conv(st_dev) + ' seconds.'
print(Mean_Time_string)
                                                                    


# In[281]:


full_times = []

for i in seconds_list:
    convert_time = time_conv(i)
    full_times.append(convert_time)
print(full_times)


# In[121]:


cx = plt.subplot()
plt.boxplot(seconds_list)
plt.title('Spread of parkrun best times for ' + runner_name)
#cx.set_xticks(range(len(seconds_list)))
#cx.set_yticklabels(range(len(seconds_list)))
cx.set_xticklabels('')
plt.show()

#sort axis labels
#remove outliers


# In[271]:


import datetime, time
df.loc[:,'Time_new'] = full_times
df.loc[:,'Time_new'] = pd.to_datetime(df.loc[:,'Time_new']).dt.time


# In[282]:


#convert dates to datetime format so can filter list on dates
import datetime
#datetime.datetime.strptime('Run Date', "%d%m%Y").date()
df.loc[:,'Run Date'] = pd.to_datetime(df.loc[:,'Run Date'])
#df.loc[:,'Time'] = pd.to_datetime(df.loc[:,'Time']).dt.time #doesn't work - no hour data
print(df.info())
print(df.head)


# In[283]:


dates = df[(df['Run Date'] > '2016-01-01') & (df['Run Date'] < '2020-02-01') ]
print(dates)


# In[272]:


# Query to pull out all dates after a certain date and times over a certain amount 
# Specifically to allow me to filter on runs with Oliver 
time_cutoff = '2:30' # insert time you want to filter from
date_limit = '2010-01-01' # insert date you want to filter from

time_conv = get_sec(time_cutoff)

#print(time_conv)

runs_with_O = df[(df['Run Date'] > date_limit) & (df['Time_seconds'] > time_conv)]

print(runs_with_O)


# In[304]:


# Use pandas to create a new df showing summary data. Can then use this instead of a dictionary for creating the bar chart

print(df.info())

#unique values in list
unique_venues = df.loc[:, 'Event Name'].unique()
print(unique_venues)

#loop through values in unique_venues list to collect summary data
for i in unique_venues:
    fastest = df2.loc[:,'Time'].min()
    rows = [pd.Series([fastest, 100, 20,'Blue','Label_1'], index=df.columns)


# In[ ]:




