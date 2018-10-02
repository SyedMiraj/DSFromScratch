# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 22:47:46 2018

@author: User
"""

import bs4
import requests

url = "http://www.espncricinfo.com/"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, "html.parser")
print(soup.prettify())

