# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 16:34:16 2018

@author: User
"""

import math

def mean(x):
    return sum(x)/len(x)

def median(x):
    n = len(x)
    x = sorted(x)
    midpoint = n // 2
    if n % 2 == 1:
        return x[midpoint]
    else:
        return (x[midpoint - 1] + x[midpoint + 1])/2
    


def quantile(x, p):
    position = int(p * len(x))
    return sorted(x)[position]


def sum_of_square(x):
    sum = 0
    for i in x:
        sum += i**2
    return sum
        
        
 
def variance(x):
    return sum_of_square(de_mean(x))/(len(x) - 1)

def de_mean(x):
    x_bar = mean(x)
    return [i-x_bar for i in x]

def covariance(x, y):
    return dot(x, y)/(len(x) - 1)

def dot(v, w):
    return sum(v_i * w_i 
               for v_i, w_i in zip(v, w))
    
print(covariance([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]))
                                                                                            
    
    
    
    
    
    

