#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df=pd.read_csv("heart.csv")


# In[4]:


df


# In[6]:


df.isnull().sum()


# In[8]:


X = df.drop(columns = 'target')
X


# In[9]:


y=df['target']


# In[10]:


from sklearn.model_selection import train_test_split


# In[12]:


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=21)


# In[13]:


X_train


# In[14]:


X_test


# In[15]:


from sklearn.preprocessing import StandardScaler


# In[16]:


scaler = StandardScaler()


# In[18]:


X_train_scaled = scaler.fit_transform(X_train)


# In[19]:


X_test_scaled = scaler.transform(X_test)


# In[20]:


X_train_scaled


# In[21]:


X_test_scaled


# In[22]:


from sklearn.linear_model import LogisticRegression


# In[23]:


log_reg = LogisticRegression(random_state = 0).fit(X_train_scaled,y_train)


# In[24]:


log_reg.predict(X_train_scaled)


# In[25]:


log_reg.score(X_train_scaled,y_train)


# In[27]:


log_reg.score(X_test_scaled,y_test)


# In[38]:


log_reg1= LogisticRegression(random_state = 0,C =0.01,fit_intercept = True).fit(X_train_scaled,y_train)


# In[39]:


log_reg1.score(X_train_scaled,y_train)


# In[40]:


log_reg.score(X_test_scaled,y_test)


# In[ ]:




