#!/usr/bin/env python
# coding: utf-8

# In[8]:


#fiboncci number = 0,1,1,2,3,5,8,13,21,34
n1 = 0
n2 = 1

f =[n1,n2]
i=1

while i < 9:
    n3 = n1+n2
    f.append(n3)
    n1=n2
    n2=n3
  
    i += 1
    
print(f)

