#!/usr/bin/env python
# coding: utf-8

# # 基于TiVA数据的我国高科技行业全球价值链地位测算

# In[1]:


import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import warnings; warnings.simplefilter('ignore') 
import xlrd
import xlwt
import matplotlib.pyplot as plt
import seaborn as sns; 
get_ipython().run_line_magic('matplotlib', 'inline')
data1=pd.read_excel('EXGR_D26T27.xlsx')
data2=pd.read_excel('EXGR_DVA_D26T27.xlsx')
data3=pd.read_excel('EXGR_IDC_D26T27.xlsx')
data4=pd.read_excel('EXGR_RIM_D26T27.xlsx')
data1.index=data1.iloc[:,0]
data1.columns=data1.iloc[5,:]
data1=data1.iloc[8:,2:]
data1=data1.drop(index=['DXD: Domestic'])
data2.index=data2.iloc[:,0]
data2.columns=data2.iloc[5,:]
data2=data2.iloc[7:,2:]
data3.index=data3.iloc[:,0]
data3.columns=data3.iloc[5,:]
data3=data3.iloc[7:,2:]
data4.index=data4.iloc[:,0]
data4.columns=data4.iloc[5,:]
data4=data4.iloc[7:,2:]
index=data1.index
columns=data1.columns
FV=data2.loc['CHN: China (People\'s Republic of)']
IV=data3.loc['CHN: China (People\'s Republic of)']+data4.loc['CHN: China (People\'s Republic of)']
E=data1.loc['CHN: China (People\'s Republic of)']
GVC_position=np.zeros((1,11))
for i in range(11):
    a1=FV[i]
    a2=IV[i]
    a3=E[i]
    GVC_position[0][i]=np.log(1+a1/a3)+np.log(1+a2/a3)
    


# In[2]:


GVC_position


# In[ ]:




