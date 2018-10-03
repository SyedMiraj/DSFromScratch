# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 23:33:33 2018

@author: User
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("Page not found")
    try:
        bsobj = BeautifulSoup(html.read(), "lxml")
        title = bsobj.body.h1
    except AttributeError as e:
        return None
    return title

print(get_title("http://www.pythonscraping.com/exercises/exercise1.html"))
