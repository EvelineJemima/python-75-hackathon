#!/usr/bin/env python
# coding: utf-8

# In[97]:


import pandas as pd
import numpy as np
from orderby import orderby
import matplotlib.pyplot as plt
import natsort
df =  pd.read_csv(r'C:\Users\Admin\Downloads\WA_Retail-SalesMarketing_-ProfitCost.csv')

df=df.dropna()

d=df.groupby('Retailer country')
print(d['Revenue'].max())



# In[ ]:





# In[ ]:




