#!/usr/bin/env python
# coding: utf-8

# Write a function in python that can reverse a string using stack data structure.
# reverse("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

# In[ ]:


from collections import deque
class stack:
    def __init__(self):
        self.container=deque()
    def insert(self,value):
        self.container.append(value)
    def remove(self):
        return self.container.pop()
    def reverse(self,value):
        for i in value:
             self.insert(i)
        r=''
        while len(self.container)!=0:
            r+=self.remove()
        return r


# In[ ]:


s=stack()


# In[ ]:


# s.insert("Hello Anurag")


# In[ ]:


s.reverse("We will conquere COVID-19")


# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




