#!/usr/bin/env python
# coding: utf-8

# In[10]:


class hash:
    def __init__(self):
        
        self.arr=[None for i in range(10)]
    def hashing(self,key):
        h=0
        for i in key:
            h+=ord(i)
        return h % 10
    def add(self,key,value):
        temp=self.hashing(key)
        self.arr[temp]=value
    def get(self,key):
        temp=self.hashing(key)
        print(self.arr[temp])
    def delete(self,key):
        temp=self.hashing(key)
        self.arr[temp]=None
    


# In[11]:


t=hash()
t.add("march 6",130)


# In[12]:


t.arr
t.get("march 6")


# In[13]:


t.add("march 7",200)
t.add("march 8",400)
t.add("march 9",500)


# In[14]:


t.get("march 7")
t.get("march 8")


# In[15]:


t.delete("march 6")
t.hashing("march 6")
t.arr


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




