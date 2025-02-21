#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


# In[6]:


veriler=pd.read_csv("maaslar.csv")
veriler


# In[36]:


x = veriler.iloc[:,1:2]
y = veriler.iloc[:,2:]
X = x.values
Y = y.values



# In[58]:


from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

   #### 1. derceden regresyon ####
lin_reg1=LinearRegression()
lin_reg1.fit(X,Y)
lin_predict = lin_reg1.predict(X)
print(lin_predict)

   #### 2. dereceden regresyon ####
lin_reg = LinearRegression()
poly_reg = PolynomialFeatures( degree = 2)

X_poly = poly_reg.fit_transform(X)
lin_reg.fit(X_poly,Y)
poly_predict = lin_reg.predict(X_poly)
print(poly_predict)


# In[41]:


plt.plot( X , poly_predict , color="red")
plt.scatter(X,Y ,color="blue")
plt.show()


# In[ ]:




