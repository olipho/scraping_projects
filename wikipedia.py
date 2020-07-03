# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 21:54:28 2020

@author: Dave
"""

#import codecademylib3_seaborn
#import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage_response = requests.get('https://en.wikipedia.org/wiki/List_of_Grand_Slam_men%27s_singles_champions')
print(webpage_response)

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

My_table = soup.find('table',{'class':'wikitable sortable'})
links = My_table.findAll('a')

winners = []
for link in links:
    winners.append(link.get('title'))
print(winners)
#slam_winners = soup.find_all(attrs={"class": "wikitable sortable"})
#print(slam_winners)

#winner_list = []

#for r in slam_winners:
#  winner_list.append(r.get('a'))
#print(winner_list)
#print(r.text)
