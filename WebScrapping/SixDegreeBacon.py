# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 11:42:45 2018

@author: User
"""
# find_all(tag, attributes, recursive, text, limit, keywords)
# find(tag, attribute, recursive, text, keyword)

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html.read(), "lxml")
for link in bsObj.find("div", {"id":"bodyContent"}).findall("a", href = re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])

        