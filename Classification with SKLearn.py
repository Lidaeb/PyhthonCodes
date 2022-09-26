#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Classification with SKLearn
pip install -U scikit-learn


# In[2]:


from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=0)
X = [[ 1,  2,  3],  # 2 samples, 3 features
     [11, 12, 13]]
y = [0, 1]  # classes of each sample
clf.fit(X, y)
RandomForestClassifier(random_state=0)


# In[3]:


clf.predict(X)  # predict classes of the training data
array([0, 1])
clf.predict([[4, 5, 6], [14, 15, 16]])  # predict classes of new data
array([0, 1])


# In[4]:


from sklearn.preprocessing import StandardScaler
X = [[0, 15],
     [1, -10]]
# scale data according to computed scaling values
StandardScaler().fit(X).transform(X)
array([[-1.,  1.],
       [ 1., -1.]])


# In[11]:


from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# create a pipeline object
pipe = make_pipeline(
    StandardScaler(),
    LogisticRegression()
)

# load the iris dataset and split it into train and test sets
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# fit the whole pipeline
 pipe.fit(X_train, y_train)
Pipeline(steps=[('standardscaler', StandardScaler()),
                ('logisticregression', LogisticRegression())])
# we can now use it like any other estimator
accuracy_score(pipe.predict(X_test), y_test)
0.97


# In[12]:


from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate

X, y = make_regression(n_samples=1000, random_state=0)
lr = LinearRegression()

result = cross_validate(lr, X, y)  # defaults to 5-fold CV
result['test_score']  # r_squared score is high because dataset is easy
array([1., 1., 1., 1., 1.])


# In[ ]:




