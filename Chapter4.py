# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 13:40:23 2018

@author: User
"""

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[10, 11],
     [11, 12],
     [13, 14]]

# find the shape of matrics

def shape_of_matrics(matrics):
    row = len(matrics)
    column = len(matrics[0])
    return row, column

# create this touple to a matrix form
friendship = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), 
               (2, 4), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
    

def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_i[j] for A_i in A]


def make_matrics(num_rows, num_columns, entry_fn):
    return [[entry_fn(i, j) 
             for j in range(num_rows)
             for i in range(num_columns)]]
     
            


    