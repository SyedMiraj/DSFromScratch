# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 10:34:01 2018

@author: User
1.43.35-
"""

import re

string = "Hello, world."
if re.search(r".............", string):
    print(string + " has length <= 5")