#!/usr/bin/env python
# coding: utf-8

# Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]".

# In[30]:


def stack(value):
    s=[]
    balanced=True
    bracket={'{':'}','[':']','(':')'}
    for i in value:
        if i in "[{(":
            s.append(i)
        if i in '}])':
            if len(s)!=0:
                top=s.pop()
                if bracket[top]!=i:
                    balanced= False
                else:
                    balanced=True
            else:
                balanced= False
    if len(s)==0 and balanced:
        return True
    else:
        return False
            


# In[31]:


a=stack("({a+b})")


# In[32]:


print(a)


# In[33]:


a=stack("[a+b]*(x+2y)*{gg+kk}")
print(a)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




