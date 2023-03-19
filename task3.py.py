#!/usr/bin/env python
# coding: utf-8

# In[104]:


#installing dependencies
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt 
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import seaborn as sns

data_train=pd.read_csv('C:\dev\python_files/internship_train.csv')
data_test=pd.read_csv('C:\dev\python_files/internship_hidden_test.csv')

data_train.head()


# In[145]:


data.tail() # last 5 rows


# In[146]:


data.shape #size of dataset


# In[147]:


data.describe()


# In[148]:


data.isnull().sum() #checking for redundant values


# In[149]:


data.corr() #quantify the association between variables or features of a dataset
cor = data.iloc[:,0:5].corr()
print(cor)


# In[150]:


X=data_train.iloc[:,0:53]
Y=data_train.target
lm = LinearRegression()
lm.fit(X, Y)


# In[151]:


# Predict on the test data
X_test = data_test.iloc[:,0:53]
y_test = data_test
y_pred = lm.predict(X_test)
print(y_pred)


# In[157]:


print('Root Mean Squared Error:', np.sqrt(mean_squared_error(data_train.head(10000).target, y_pred))) 


# In[156]:


pip freeze > requirements.txt

