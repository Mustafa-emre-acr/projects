#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


veriler = pd.read_csv("veriler.csv")



# In[3]:


boykilo = veriler.iloc[:,4:].values




# In[4]:


c = veriler.iloc[:,4:].values

## label encoding

from sklearn import preprocessing 

le = preprocessing.LabelEncoder()
c[:,0] = le.fit_transform(veriler.iloc[:,4])

## one hot encoding

ohe = preprocessing.OneHotEncoder()
c=ohe.fit_transform(c).toarray()



# In[5]:


sonuc = pd.DataFrame(data = c[:,0] , index = range(22) , columns = ["cinsiyet"]) #dummy variable
print(sonuc)


# In[6]:


sonuc1 = veriler[["boy","kilo","yas"]]
sonuc1.head()


# In[7]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(sonuc1,sonuc,test_size = 0.33 ,random_state=0)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train,y_train)
y_predict = lr.predict(x_test)


# In[8]:


print(y_predict)


# In[9]:


print(y_test)


# # boy tahmini

# In[10]:


boy =veriler.iloc[:,1].values



# In[11]:


kilo_yas=veriler[["kilo","yas"]]
test_verisi = pd.concat([kilo_yas,sonuc], axis=1)
test_verisi.head()


# In[12]:


X_train,X_test,Y_train,Y_test = train_test_split(test_verisi , boy, test_size=0.33,random_state=0)

lr1 = LinearRegression()
lr1.fit(X_train,Y_train)
boy_predict = lr1.predict(X_test)
print(boy_predict)


# # BACKWARD  ELİMİNATİON

# In[14]:


import statsmodels.api as sm
X = np.append(arr = np.ones((22,1)).astype(int) , values=test_verisi , axis= 1)

##beta0 degeri eklenmiş oldu

X_l=test_verisi.iloc[:,[0,1,2]].values
X_l=np.array(X_l, dtype=float)
model = sm.OLS(boy,X_l).fit()
model.summary()

##bütün değişkenlerin p değerlerine bakılır p>sl(p<0.05) olanlar atılır


# In[15]:


X_l=test_verisi.iloc[:,[0,1]].values
X_l=np.array(X_l,dtype=float)
model = sm.OLS(boy,X_l).fit()
model.summary()


# In[18]:


X_l=test_verisi.iloc[:,[0]].values
X_l=np.array(X_l,dtype=float)
model = sm.OLS(boy,X_l).fit()
model.summary()


# In[ ]:





# In[ ]:




