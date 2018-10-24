# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 12:23:40 2018

@author: User
"""

import re

nameandage = """ 
Janice is 32 and Manish is 34
Gabreil is 25 and Julien in 28
"""

map = {}
x = 0

# name_pattern = re.findall("[A-Z]{1}[a-z]*", nameandage)
name_pattern = re.findall("[A-Z]{1}[a-z]*", nameandage)
age_pattern = re.findall("\d{2}", nameandage)

for name in name_pattern:
    map[name] = age_pattern[x]
    x += 1
    
print(map)