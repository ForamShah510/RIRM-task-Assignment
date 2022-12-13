#!/usr/bin/env python
# coding: utf-8

# In[61]:


import requests
from bs4 import BeautifulSoup

url = "https://ful.io"

r = requests.get(url)
htmlContent = r.content

anchor = soup.find_all('a')
all_links = set()

for link in anchor:
    if(link.get('href')):
        all_links.add(link.get('href'))
        print(link.get('href'))


# In[ ]:




