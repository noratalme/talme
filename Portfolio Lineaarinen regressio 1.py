#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


df=pd.read_excel('http://taanila.fi/ENB2012_data.xlsx')
df.head(20)


# In[21]:


sns.jointplot(data=df, x='X1', y='Y1', kind='reg')


# In[28]:


X = df['X1'].to_frame()

y = df['Y1']


# In[29]:


from sklearn.linear_model import LinearRegression 

malli = LinearRegression().fit(X,y)


# In[30]:


malli.coef_


# In[31]:


malli.intercept_


# In[27]:


malli.predict(pd.DataFrame([0.8, 1.3, 0.4]))


# In[ ]:




