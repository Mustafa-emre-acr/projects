#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[21]:


veriler = pd.read_csv("satislar.csv")
satislar =  veriler[['Satislar']]
aylar    =  veriler[['Aylar']]


# In[22]:


from sklearn.model_selection import train_test_split

x_train , x_test , y_train, y_test = train_test_split(aylar,satislar,test_size=0.33,random_state=0)


# In[40]:


from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

Y_train = sc.fit_transform(y_train)
Y_test = sc.fit_transform(y_test)




# In[44]:


from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train , y_train)

tahmin = lr.predict(x_test)


# In[50]:





# In[48]:





# In[65]:


x_train = x_train.sort_index() ## verileri index e gore sıralayacak
y_train = y_train.sort_index()
plt.plot(x_train , y_train)
plt.plot(x_test , tahmin)
plt.show()


# In[ ]:




