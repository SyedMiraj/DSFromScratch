# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 07:17:57 2018

@author: User
"""

# def an function which takes arguments and return a result
'''
def bring_output (x):
    return x**3
'''
bring_output = lambda x : x**3 


# define a function that calls another aninomous function

def my_function(n):
    return lambda a : a*n

myDoubler = my_function(2)
print(myDoubler)