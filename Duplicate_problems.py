#!/usr/bin/env python
# coding: utf-8

# In[15]:


myNums=[1,2,3,4,4]

def is_duplicate():
    for i in range(len(myNums)):
        for j in range(i+1,len(myNums)):
            if myNums[i]==myNums[j]:
                return True
    else:
        return False
is_duplicate()


# In[16]:


#time O(N2), space O(N)


# In[17]:


mySet = set(myNums)
if len(mySet) == len(myNums):
    print("its not duplicate")
else:
    print("its duplicate")
    
#bunu kısa yazacak olursak;
#def solution():
    #return len(myNums) != len(set(myNums))
#solution()   eğer bu true dönerse duplicatdir, false ise değildir. 


# In[18]:


# time O(N), space O(N)


# In[ ]:




