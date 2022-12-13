#!/usr/bin/env python
# coding: utf-8

# In[27]:


import re

def isValid(s):
    Pattern = re.compile("^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$")
    return Pattern.match(s)
s= input("Enter the number")
if(isValid(s)):
    print("Valid Number")
else:
    print("Invalid Number")

