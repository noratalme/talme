#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.style.use('seaborn-whitegrid')

from matplotlib.ticker import MultipleLocator
from matplotlib.dates import DateFormatter

myLoc = MultipleLocator(14)
myFmt = DateFormatter('%d/%m')


# In[41]:


aktia = pd.read_csv('M://Aktia_osake.csv', sep=';', decimal=',')
nordea = pd.read_csv('M://Nordea_osake.csv', sep=';', decimal=',')

nordea.head(10)


# In[42]:


aktia.index = pd.to_datetime(aktia['Päivämäärä'], dayfirst=True)
nordea.index = pd.to_datetime(nordea['Päivämäärä'], dayfirst=True)

aktia.sort_index(inplace=True)
nordea.sort_index(inplace=True)

nordea.head()


# In[43]:


nordea.tail()


# In[44]:


nordea['Päätöskurssi'].plot()


# In[31]:


nordea['Päätöskurssi'].resample('M').mean().plot()


# In[32]:


nordea['Päätöskurssi'].resample('Q').mean().plot()


# In[33]:


nordea['Päätöskurssi'].resample('Y').mean().plot()


# In[34]:


aktia['Päätöskurssi'].plot()


# In[35]:


aktia['Päätöskurssi'].resample('M').mean().plot()


# In[36]:


aktia['Päätöskurssi'].resample('Q').mean().plot()


# In[37]:


aktia['Päätöskurssi'].resample('Y').mean().plot()


# In[38]:


nordea['Vaihto €'].resample('Q').sum().plot()


# In[39]:


kuvio1 = nordea['Päätöskurssi']['2019':].plot()


# In[46]:


kuvio1 = nordea['Päätöskurssi']['2019':].plot()

kuvio1.xaxis.set_major_locator(myLoc)
kuvio1.xaxis.set_major_formatter(myFmt)


# In[47]:


nordea['Päätöskurssi'].plot()

nordea['Päätöskurssi'].rolling(50).mean().plot()
nordea['Päätöskurssi'].rolling(200).mean().plot()


# In[49]:


nordea['nordea%'] = nordea['Päätöskurssi'].pct_change()
aktia['aktia%'] = aktia['Päätöskurssi'].pct_change()

aktia.head(20)


# In[52]:


muutokset = pd.concat([nordea['nordea%'], aktia['aktia%']], axis=1)

muutokset.tail(20)


# In[53]:


kuvio2 = muutokset['2019':].plot()

kuvio2.set_ylabel('Muutos')

kuvio2.xaxis.set_major_locator(myLoc)
kuvio2.xaxis.set_major_formatter(myFmt)


# In[54]:


muutokset.describe()


# In[57]:


muutokset[(abs(muutokset['nordea%'])>0.1) |
         (abs(muutokset['aktia%'])>0.1)]


# In[67]:


muutokset['Viikonpäivä'] = muutokset.index.weekday

vkpaivat = ['ma', 'ti', 'ke', 'to', 'pe']

muutokset.groupby('Viikonpäivä')['nordea%'].describe()


# In[68]:


muutokset.corr()


# In[69]:


muutokset.plot.scatter(x='nordea%', y='aktia%')


# In[70]:


muutokset['nordea%'].rolling(50).corr(muutokset['aktia%']).plot()


# In[71]:


(muutokset['nordea%'].rolling(252).std()*(252**0.5)).plot(label='nordea', legend=True)
(muutokset['aktia%'].rolling(252).std()*(252**0.5)).plot(label='aktia', legend=True)


# In[73]:


fig, kuvio = plt.subplots(figsize = (11, 7))

kuvio.set_ylabel('nordea', color='maroon', fontsize=15)
kuvio.plot(nordea['Päätöskurssi'], color='maroon')
kuvio.set_ylim(3,12)

kuvio_T = kuvio.twinx()

kuvio_T.set_ylabel('aktia', color='pink', fontsize=15)
kuvio_T.plot(aktia['Päätöskurssi'], color='pink')
kuvio_T.set_ylim(3,12)


# In[ ]:




