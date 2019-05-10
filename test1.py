#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import os


# In[2]:


os.getcwd()


# In[7]:


capability = pd.read_csv('capability.csv')
player=pd.read_csv('player.csv' ) 
playingposition=pd.read_csv('playingposition.csv') 


# In[30]:


player.head()


# In[27]:


playingposition.drop_duplicates(subset=['ID'],keep='first',inplace=True)


# In[25]:


playingposition.shape


# In[26]:


len(playingposition.ID.unique())


# In[28]:


playingposition.shape


# In[29]:


playingposition.to_csv("po.csv")


# In[ ]:




