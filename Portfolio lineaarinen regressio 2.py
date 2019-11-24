#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


df=pd.read_excel('http://taanila.fi/ENB2012_data.xlsx')
df.head(20)


# In[5]:


sns.pairplot(df, kind='reg')


# In[7]:


correlation_matrix = df.corr().round(2)

sns.heatmap(data=correlation_matrix, annot=True)


# In[8]:


X = df[['X4', 'X5']]
y = df['Y1']


# In[9]:


from sklearn.linear_model import LinearRegression

malli = LinearRegression().fit(X,y)


# In[10]:


malli.coef_


# In[11]:


malli.intercept_


# In[12]:


malli.score(X,y)


# In[13]:


plt.scatter(malli.predict(X), malli.predict(X)-y)

plt.hlines(y=0, xmin=50, xmax=250)

plt.xlabel('Ennuste')
plt.ylabel('Poikkeama todellisesta')


# In[14]:


plt.scatter(y, malli.predict(X))

plt.xlabel('Todellinen lämmitys')
plt.ylabel('Ennuste')


# In[ ]:




