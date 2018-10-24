# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 09:29:00 2018

@author: User
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

# Find the team members name, designation and favourite film

url = "https://opencorporates.com/info/team"
html = urlopen(url)

if html.getcode() == 200:
    try:
        time.sleep(1)
        bsObj = BeautifulSoup(html.read(), "html.parser")
        divlist = bsObj.select("div.oc-media__wide.oc-media__wide--left")
        if len(divlist) != 0:
            for div in divlist:
                for child in div.children:
                        print(len(child.find_all('div')))
    except Exception as e:
        print("Error: {}".format(e))
else:
    print("Error, page not found!!")