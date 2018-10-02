# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 16:19:02 2018

@author: User
"""
from matplotlib import pyplot as plt

# Simple plot
'''
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.5, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
plt.title("GDP vs years")
plt.xlabel('Year')
plt.ylabel('GDP in taka')
'''

# Bar plot

movies = ['Annie Hall', 'Heu Hur', 'Casabalanca', 'Gandhi', 'Noth side story']
num_of_oskar = [5, 11, 3, 8, 10]

plt.bar(movies, num_of_oskar)
