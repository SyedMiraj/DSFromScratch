# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 21:34:41 2018

@author: Shahriar Miraj
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html.read(), "lxml")

for link in bsObj.find_all("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])




