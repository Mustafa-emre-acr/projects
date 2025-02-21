#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv('veriler.csv')

x = veriler.iloc[:,2:4].values #bağımsız değişkenler
y = veriler.iloc[:,4:].values #bağımlı değişken


from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)

from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression(random_state=0)
log_reg.fit(X_train,y_train)
y_pred = log_reg.predict(X_test)
print(y_pred)


# # CONFUSSİON MATRIX

# In[2]:


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)
# 1 tane doğru var


# # K-NN

# In[3]:


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 1 , metric='minkowski')
knn.fit(X_train,y_train)

knn_pred = knn.predict(X_test)

cm1 = confusion_matrix(y_test,knn_pred)
print(cm1)


# # SVM

# In[4]:


'''from sklearn.svm import SVR 
svc = SVR(kernel='linear')
svc.fit(X_train,y_train)

svc_pred = svc.predict(X_test)

cm2 = confusion_matrix(y_test,svc_pred)
print(cm2)'''


# In[5]:


from sklearn.naive_bayes import GaussianNB
gnb  =GaussianNB()
gnb.fit(X_train,y_train)
gnb_pred = nb.predict(X_test)
gnb_pred

cm3 = confusion_matrix(y_test,gnb_pred)
print(cm3)


# In[ ]:





# In[ ]:




