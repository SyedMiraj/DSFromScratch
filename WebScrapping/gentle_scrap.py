# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 22:04:29 2018

@author: User
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.espn.in/soccer/table/_/league/eng.1"
headers = {'User-Agent' : 'Mozilla/5.0'}
html = urlopen(url)
print(html.status_code)
bsObj = BeautifulSoup(html.read(), "lxml")


