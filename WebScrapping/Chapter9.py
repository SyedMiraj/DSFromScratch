# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 22:47:46 2018

@author: User
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://pythonscraping.com/pages/page1.html"
solid_page = urlopen(url)

# Running the BeautifulSoup
url2 = "http://www.pythonscraping.com/exercises/exercise1.html"
html = urlopen(url2)
bsObj = BeautifulSoup(html.read(), "lxml")

# A way to explicitely check situation

try:
    badContent = bsObj.find("nonExistent").h1
except AttributeError as e:
    print("Tag not found")
else:
    # Do the programming
    if badContent == None:
        print("Tag was not found")
    else:
        print(badContent)
        



  

