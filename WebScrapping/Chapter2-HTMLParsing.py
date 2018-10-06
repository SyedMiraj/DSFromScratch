# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 08:24:41 2018

@author: User
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

parse_data = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
try:
    data = BeautifulSoup(parse_data.read(), "lxml")
except HTTPError as e:
    print("Nothing found")

namelist = data.find_all("", {"class":"green"})
for name in namelist:
    print(name.get_text())
    
# find_all(tag, attributes, recursive, text, limit, keywords)
# find(tag, attribute, recursive, text, keyword)
    
