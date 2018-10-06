# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 09:10:03 2018

@author: User
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

url = "http://www.pythonscraping.com/pages/page3.html"
html = urlopen(url)
html_data = BeautifulSoup(html.read(), "lxml")
img_list = html_data.find_all("img", {"src": re.compile("\.\./img*\.jpg")})

for img in img_list:
    print(img["src"])