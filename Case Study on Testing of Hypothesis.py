#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


sales_data=pd.read_csv(r'C:\Users\user\Downloads\Sales_add.csv')


# In[3]:


sales_data.head()


# # A company started to invest in digital marketing as a new way of their product promotions. For that they collected data and decided to carry out a study on it.
# ● The company wishes to clarify whether there is any increase in sales after
# stepping into digital marketing.
# 

# In[20]:


#Ho:digital marketing doesn't create any improvement in sales
#Ha:sales increased after stepping to digital marketing


# In[19]:


#Two Sample T Test


# In[4]:


from scipy.stats import ttest_ind


# In[5]:


t_stat,pval1=ttest_ind(sales_data['Sales_before_digital_add(in $)'],sales_data['Sales_After_digital_add(in $)'])


# In[6]:


pval1


# In[7]:


if pval1<0.05:
    print('Null hypothesis is rejected')
else:
    print('Null hypothesis is accepted')


# In[18]:


#The result shows there is an increase in sales afterstepping into digital marketing.


# #  The company needs to check whether there is any dependency between thefeatures “Region” and “Manager”

# In[9]:


sales_data.info()


# In[17]:


#Ho:No dependency between "region" & "manager" 
#Ha:A relation exist between "region" & "manager" 


# In[10]:


from scipy.stats import chi2_contingency


# In[11]:


column1=sales_data['Region']
column2=sales_data['Manager']


# In[12]:


contingency_table=pd.crosstab(column1,column2)
contingency_table


# In[13]:


chisquare_ststitics,pvalue,degreefreedom,expectedvalue=chi2_contingency(contingency_table)


# In[14]:


chi2_contingency(contingency_table)


# In[15]:


pvalue


# In[16]:


if pvalue<0.05:
    print('Null hypothesis is rejected')
else:
    print('Null hypothesis is accepted')


# In[ ]:




