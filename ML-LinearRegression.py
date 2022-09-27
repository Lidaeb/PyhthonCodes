#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Linear Regression 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn 

from pylab import rcParams

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing  import scale


# In[ ]:


##to get inline and our graph size
get_ipython().run_line_magic('mtplotlib', 'inline')
rcParams['figure.figsize'] = 10,8


# In[ ]:



##create syntetic data for linear regression
##no.random is random number generateor,1= columns
rooms = 2*np.random.rand(100, 1) +3


# In[ ]:


## print 10 random numbers
rooms[1:10]


# In[ ]:


##create anothe variable and absolute amount of random generated 100 values
price = 265 + 6*rooms +abs(np.random.randn(100,1))
price[1:10]


# In[ ]:


## r^ a point plot is generate instead of line 
##
plt.plot(rooms,price,'r^')
plt.xlabel("# of rooms, 2019 Avarage")
plt.ylabel("2019 Avarage Home, 1000s USD")
plt.show()


# In[ ]:


##Beaware of Capital Letters
X = rooms
y = price

LinReg = LinearRegression()
LinReg.fit(X,y)
print(LinReg.intercept_, LinReg.coef_)


# In[ ]:


print(LinReg.score(X,y))


# In[ ]:




