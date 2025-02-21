#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np


# In[40]:


veriler = pd.read_csv("veriler.csv")
sonuc3=veriler.iloc[:,1:4]


# In[20]:


ulkeler = veriler.iloc[:,0:1].values


# In[21]:


# In[22]:


from sklearn import preprocessing

le = preprocessing.LabelEncoder()

ulkeler[:,0]=le.fit_transform(veriler.iloc[:,0])




# In[23]:


ohe = preprocessing.OneHotEncoder()
ulkeler=ohe.fit_transform(ulkeler).toarray()


# In[24]:


sonuc1 =pd.DataFrame(data=ulkeler ,index = range(22), columns = ["fr","tr","us"] )



# In[25]:


cinsiyet = veriler["cinsiyet"]
sonuc2 = pd.DataFrame( data=cinsiyet , index= range(22),columns=["cinsiyet"])



# In[42]:


sonuc=pd.concat([sonuc1,sonuc2],axis=1)
Sonuc=pd.concat([sonuc1,sonuc3],axis=1)



#    # VERİLERİ BOLME #

# In[34]:


from sklearn.model_selection import train_test_split


# In[43]:


x_train, x_test , y_train, y_test = train_test_split(Sonuc,sonuc2, test_size=0.33, random_state=0)


# # StandardScaling - standart sapma

# In[47]:


from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)


# In[48]:


# In[ ]:




