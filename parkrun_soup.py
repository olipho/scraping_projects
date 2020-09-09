# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 21:54:28 2020

@author: Dave
"""

#import codecademylib3_seaborn
#import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1'}

webpage_response = requests.get('https://www.parkrun.org.uk/torbayvelopark/results/athletehistory/?athleteNumber=3149490', headers = headers)
print(webpage_response)

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "lxml")
pretty_soup = soup.prettify()
#  print(pretty_soup)
running = soup.find_all(attrs={"class": "sortable"})
#print(running)

results = []

for r in running:
#    results.append(r.get_text(','))
    results_text = r.get_text(',')
#print(results_text)

#print(results[1:2])

split_text = results_text.split(',')
#for word in words:
#   words.append(word)
print(split_text)
#print(type(split_text))
dates = split_text[2::6]
times = split_text[5::6]
print(dates)
print(times)
