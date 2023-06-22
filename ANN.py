#!/usr/bin/env python
# coding: utf-8

# In[108]:


import pandas as pd
import numpy as np
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix


# In[121]:


df=pd.read_csv("diabetes.csv")


# In[122]:


df


# In[124]:


df.head()


# In[126]:


df.dtypes


# In[127]:


data.shape


# In[128]:


df.isnull().sum()


# In[130]:


X = df.iloc[:,:8].values
y = df["Outcome"].values


# In[131]:


df.info()


# In[132]:


df.columns


# In[133]:


df.describe()


# In[134]:


df_cat=df.select_dtypes(np.object)
df_num=df.select_dtypes(np.number)


# In[120]:


df_num


# In[137]:


df_cat


# In[141]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.33,random_state=7)


# In[142]:


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# In[147]:


model=Sequential()
model.add(Dense(32,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(X_train,y_train,epochs=10,batch_size=32,validation_data=(X_test,y_test))


# In[149]:


val_loss,val_accuracy = model.evaluate(X_test,y_test)
print(val_loss,val_accuracy)


# In[ ]:




