# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 19:45:15 2018

@author: User
"""

# stdin and stdout

import sys, re


regex = sys.argv[1]

for line in sys.stdin:
    if re.search(regex, line):
        sys.stdout.write(line)