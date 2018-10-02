# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 08:42:00 2018

@author: User
"""

# Function define

double =  lambda x : 2*x


def apply_to_one(f):
    return f(5)

# print(apply_to_one(double))

# Tuples

my_list = []
my_touple = (1, 2)
'''
try:
    my_touple[1] = 3
except TypeError:
    print("Cannot modify a touple")
    
'''

def sum_and_product(x, y):
    return (x+y),(x*y)

#print(sum_and_product(10, 11))
    
empty_dict = {}
empty_dict2 = dict()

grades = {'selim' : 80, 'halim' : 40}
'''
try:
    fatemas_grade = grades['fatema']
except KeyError:
    print("Data not found")
'''

tweet = {
        'user' : 'Shahriar Miraj',
        'text' : 'Sleep is important as well as exercise',
        'retweet_count' : 100,
        'hashtags' : ['#sleep', '#exercise', '#soundsleep']
        }
    
#print('hashtags' in tweet)

    # Counter
from collections import Counter
c = Counter([1,2,2,3,4,4,4,5,6])
#print(c)
# Control Flow

if 1>2:
    messge = "If only 1 is greater than 2"
elif 1<3:
    messge = "If only 1 is less than 3"
else:
    messge = "when all fails"
    
#print(messge)
    
# Sorting 
a = [15, 25, 5, 24, 25, 22, 30, 45]

import random

four_random_data = [random.random() for _ in range(4)]
print(four_random_data)

































