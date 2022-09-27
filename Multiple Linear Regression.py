#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Multiple Linear Regression 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn 

from pylab import rcParams

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing  import scale
from sklearn.pipeline import make_pipeline


# In[ ]:


##to get inline and our graph size
get_ipython().run_line_magic('mtplotlib', 'inline')
rcParams['figure.figsize'] = 10,8


# In[ ]:



##set style for seaborn
import seaborn as sb
sb.set_style('whitegrid')
from collections import Counter


# In[ ]:


address = 'C:/Users/lebad/Downloads/Ex_Files_Python_Data_Science_EssT_Pt2/Ex_Files_Python_Data_Science_EssT_Pt2/Exercise Files/Data/enrollment_forecast.csv'

enroll = pd.read_csv(address)
enroll.columns = ['year','roll', 'unem' ,'hgrad','inc']
enroll.head()


# In[ ]:


sb.pairplot(enroll)


# In[ ]:


print(enroll.corr())


# In[ ]:


enroll_data = enroll[['unem','hgrad']].values

enroll_target = enroll[['roll']]

enroll_data_names = ['unem', 'hgrad']

X, y = scale(enroll_data), enroll_target


# In[ ]:


## checking missing values
missing_values = X==np.NAN
X[missing_values == True]


# In[ ]:


LinReg = LinearRegression(normalize = True)

LinReg.fit(X,y)
print(LinReg.score(X, y))

