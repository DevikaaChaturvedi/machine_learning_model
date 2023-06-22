#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[8]:


data=pd.read_csv(r'Housing.csv')


# In[9]:


data


# In[10]:


print(data.shape)
print(data.isna().sum())


# In[11]:


print(data.columns)


# In[12]:


X=data['area'].values
Y=data['price'].values
print(Y)
print(X.shape)
print(Y.shape)


# In[50]:


X=X.reshape(X.shape[0],1)


# In[51]:


Y=Y.reshape(Y.shape[0],1)
print(X.shape)
print(Y.shape)


# In[52]:


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=100)


# In[53]:


from sklearn.linear_model import LinearRegression


# In[54]:


reg=LinearRegression()
reg.fit(X_train,Y_train)


# In[55]:


Y_pred=reg.predict(X_test)
err=Y_test-Y_pred


# In[56]:


Y_custom=reg.predict([[3000]])
print(Y_custom)


# In[57]:


r=reg.coef_


# In[58]:


r


# In[59]:


reg.intercept_


# In[60]:


y2=3000*reg.coef_+reg.intercept_
y1=3000*469.75690529+2353148.37956561
print(y1)


# In[61]:


reg.score(X,Y)


# In[ ]:





# In[ ]:




