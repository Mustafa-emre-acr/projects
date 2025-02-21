#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


veriler = pd.read_csv("maaslar.csv")



# In[5]:


x = veriler.iloc[:,1:2].values
y = veriler.iloc[:,2:].values


# In[7]:


## scale yapılmalı ##

from sklearn.preprocessing import StandardScaler
scale1 = StandardScaler()
x_scale=scale1.fit_transform(x)
scale2 = StandardScaler()
y_scale = scale1.fit_transform(y)


# In[14]:


from sklearn.svm import SVR

svr_reg = SVR(kernel = "rbf")
svr_reg.fit(x_scale , y_scale)
svr_pre = svr_reg.predict(x_scale)

plt.scatter(x_scale,y_scale)
plt.plot(x_scale,svr_pre)
plt.show()


# In[17]:


########## DECİSİON TREE REGRESSSİON ############
    
    
from sklearn.tree import DecisionTreeRegressor
tree_reg = DecisionTreeRegressor(random_state=0)
tree_reg .fit(x,y)
tree_pre = tree_reg.predict(x)

plt.scatter(x,y)
plt.plot(x,tree_pre)
plt.show()


# In[25]:


########### RANDOM FOREST ########3

from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators = 10 , random_state=0)   ### n_estimators = karar ağacı sayısı
rf_reg.fit(x,y)
rf_pre = rf_reg.predict(x)


plt.scatter(x,y)
plt.plot(x,rf_pre)
plt.show()
plt.plot(x, rf_reg.predict(x+0.5) )
plt.plot(x, rf_reg.predict(x-0.4))
plt.show()


# In[27]:


######## R^2 score  ######

from sklearn.metrics import r2_score

r2_score(y,rf_pre)


# In[28]:


r2_score(y,rf_reg.predict(x+0.5))


# In[ ]:




