#!/usr/bin/env python
# coding: utf-8

# # nem(humidity) tahmini

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler = pd.read_csv("odev_tenis.csv")



# In[2]:


#encoding (outlook)
#veriler2 = veriler.apply(preprocessing.LabelEncoder().fit_transform()) == bütün kolonların le sini alır
outlook = veriler.iloc[:,0:1].values

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
outlook[:,0] =le.fit_transform(veriler.iloc[:,0])

ohe = preprocessing.OneHotEncoder()
outlook = ohe.fit_transform(outlook).toarray()



# In[12]:


#encoding (windy)

windy = veriler.iloc[:,3:4].values

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
veriler["windy"] = pd.DataFrame(le.fit_transform(veriler["windy"]))



# In[13]:


#encoding (play)
play = veriler.iloc[:,4:].values

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
play[:,0] =le.fit_transform(veriler.iloc[:,4])



# In[14]:


dftem_hum = veriler[["temperature","humidity"]].astype(float)
dftem_hum.head()


# In[15]:


#dataFrame yapma
dfoutlook= pd.DataFrame(data=outlook,index=range(14),columns=["overcast","rainy","sunny"])
dfoutlook.head()


# In[16]:


dfwindy = pd.DataFrame(data=windy,index=range(14),columns=["windy"])
dfwindy.head()


# In[17]:


dfplay = pd.DataFrame(data=play,index=range(14),columns=["play"])
dfplay.head()


# In[20]:


#DataFrameleri concat etmek

pdList = [dfoutlook,dfwindy,dfplay,dftem_hum]  # List of your dataframes
test_verisi = pd.concat(pdList,axis=1)



# In[23]:


import statsmodels.api as sm
X = np.append(arr = np.ones((14,1)).astype(int) , values=test_verisi.iloc[:,:-1] , axis= 1)

X_l=test_verisi.iloc[:,[0,1,2,3,4,5]].values
X_l=np.array(X_l,dtype=float)
model = sm.OLS(test_verisi.iloc[:,-1:],X_l).fit()
print(model.summary())


# In[25]:


X_l=test_verisi.iloc[:,[0,1,2,4,5]].values
X_l=np.array(X_l,dtype=float)
model = sm.OLS(test_verisi.iloc[:,-1:],X_l).fit()
print(model.summary())


# In[26]:


X_l=test_verisi.iloc[:,[0,1,4,5]].values
X_l=np.array(X_l,dtype=float)
model = sm.OLS(test_verisi.iloc[:,-1:],X_l).fit()
print(model.summary())


# In[27]:


X_l=test_verisi.iloc[:,[1,4,5]].values
X_l=np.array(X_l,dtype=float)
model = sm.OLS(test_verisi.iloc[:,-1:],X_l).fit()
print(model.summary())


# In[28]:


X_l=test_verisi.iloc[:,[1,5]].values
X_l=np.array(X_l,dtype=float)
model = sm.OLS(test_verisi.iloc[:,-1:],X_l).fit()
print(model.summary())


# In[29]:


X_l=test_verisi.iloc[:,[5]].values
X_l=np.array(X_l,dtype=float)
model = sm.OLS(test_verisi.iloc[:,-1:],X_l).fit()
print(model.summary())


# In[ ]:




