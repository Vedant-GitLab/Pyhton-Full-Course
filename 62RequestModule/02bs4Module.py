#bs4 Module : There is another module called BeautifulSoup which is used for web scraping in Python. I have personally use  bs4 module to finish a lot of freelancing task.
#To know more "https://beautiful-soup-4.readthedocs.io/en/latest/"

import requests
from bs4 import BeautifulSoup
url = "https://leetcode.com/problemset/"
r  = requests.get(url)

# print(r.text)

soup = BeautifulSoup(r.text)
# print(soup.prettify())

#to print specific data
for heading in soup.find_all("h2"):
    print(heading.text)