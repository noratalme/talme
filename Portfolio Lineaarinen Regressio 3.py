#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_excel('http://taanila.fi/Concrete_Data.xlsx')
df


# In[3]:


df.isnull().sum()


# In[4]:


sns.distplot(df['Age (day)'], bins=20)


# In[14]:


correlation_matrix = df.corr().round(2)

plt.figure(figsize=(30,25))

sns.set(font_scale=3.5)

sns.heatmap(data=correlation_matrix, annot=True, annot_kws={'size':27})


plt.text(3,-0.5, "Heat Map", fontsize = 95, color='Maroon', fontstyle='italic')


# In[20]:


features = ['Superplasticizer (component 5)(kg in a m^3 mixture)', 'Water  (component 4)(kg in a m^3 mixture)']
df['Age in days'] = np.log(df['Age (day)'])
target = df['Age in days']

plt.figure(figsize=(10, 5))
sns.set(font_scale=1.0)
for i, feature in enumerate(features):
    plt.subplot(1, len(features), i+1)
    plt.scatter(df[feature], target)
    plt.xlabel(feature)
    plt.ylabel('Age (day)')


