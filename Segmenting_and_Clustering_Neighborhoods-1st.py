#!/usr/bin/env python
# coding: utf-8

# In[38]:


import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analsysis
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import json # library to handle JSON files


# In[39]:


get_ipython().system('conda install -c anaconda beautifulsoup4 --yes')


# In[40]:


get_ipython().system('conda install -c anaconda lxml --yes')


# In[41]:


import requests # library to handle requests

from bs4 import BeautifulSoup
import xml


# In[66]:


List_url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
source = requests.get(List_url).text


# In[67]:


s = BeautifulSoup(source, 'xml')


# In[68]:


table=s.find('table')


# In[69]:


#Table consists of three columns: PostalCode, Borough, and Neighborhood. Now make it as a data frame.
column_names = ['Postalcode','Borough','Neighborhood']
df = pd.DataFrame(columns = column_names)


# In[70]:


for tr_cell in table.find_all('tr'):
    row_data=[]
    for td_cell in tr_cell.find_all('td'):
        row_data.append(td_cell.text.strip())
    if len(row_data)==3:
        df.loc[len(df)] = row_data


# In[71]:


df.head()


# In[73]:


df=df[df['Borough']!='Not assigned']


# In[81]:


df


# In[83]:


df.shape

