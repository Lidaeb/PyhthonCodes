#!/usr/bin/env python
# coding: utf-8

# In[4]:


## Logistic Regression Assumption
## Free of missing data/the predictant variable is binary or ordinal(Orderedvalues)
## Predictors are independent
## 50 observation at least
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import sklearn 



# In[6]:


from pandas import Series, DataFrame
from pylab import rcParams
from sklearn import preprocessing


# In[7]:


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict

from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score


# In[8]:


##to get inline and our graph size
get_ipython().run_line_magic('mtplotlib', 'inline')
rcParams['figure.figsize'] = 5,4
sb.set_style('whitegrid')


# In[11]:


address = 'C:/Users/lebad/Downloads/Ex_Files_Python_Data_Science_EssT_Pt2/Ex_Files_Python_Data_Science_EssT_Pt2/Exercise Files/Data/titanic-training-data.csv'


# In[13]:


titanic_training = pd.read_csv(address)
titanic_training.columns = ['passengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
print(titanic_training.head())


# In[14]:


print(titanic_training.info())


# ## VARIABLE DESCRIPTIONS
# ## Survived - Survival (0 = No; 1 = Yes)
# ## Pclass - Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
# ## Name - Name
# ## Sex - Sex
# ## Age - Age
# ## SibSp - Number of Siblings/Spouses Aboard
# ## Parch - Number of Parents/Children Aboard
# ## Ticket - Ticket Number
# ## Fare - Passenger Fare (British pound)
# ## Cabin - Cabin
# ## Embarked - Port of Embarkation (C = Cherbourg, France; Q = Queenstown, UK; S = Southampton - Cobh, Ireland)

# In[16]:


sb.countplot(x='Survived', data=titanic_training, palette='hls')


# In[17]:


## Checking for missing values
titanic_training.isnull().sum()


# In[18]:


titanic_training.describe()


# In[ ]:


Taking care of missing values
Dropping missing values
So let's just go ahead and drop all the variables that aren't relevant for predicting survival. We should at least keep the following:

Survived - This variable is obviously relevant.
get_ipython().set_next_input("Pclass - Does a passenger's class on the boat affect their survivability");get_ipython().run_line_magic('pinfo', 'survivability')
get_ipython().set_next_input("Sex - Could a passenger's gender impact their survival rate");get_ipython().run_line_magic('pinfo', 'rate')
get_ipython().set_next_input("Age - Does a person's age impact their survival rate");get_ipython().run_line_magic('pinfo', 'rate')
SibSp - Does the number of relatives on the boat (that are siblings or a spouse) affect a person survivability? Probability
Parch - Does the number of relatives on the boat (that are children or parents) affect a person survivability? Probability
Fare - Does the fare a person paid effect his survivability? Maybe - let's keep it.
Embarked - Does a person's point of embarkation matter? It depends on how the boat was filled... Let's keep it.
What about a person's name, ticket number, and passenger ID number? They're irrelavant for predicting survivability. And as you recall, the cabin variable is almost all missing values, so we can just drop all of these.


# In[19]:


titanic_data = titanic_training.drop(['Name', 'Ticket', 'Cabin'], axis=1)
titanic_data.head()


# In[20]:


## Imputing missing values
sb.boxplot(x='Parch', y='Age', data=titanic_data, palette='hls')


# In[21]:


Parch_groups = titanic_data.groupby(titanic_data['Parch'])
Parch_groups.mean()


# In[22]:


def age_approx(cols):
    Age = cols[0]
    Parch = cols[1]
    
    if pd.isnull(Age):
        if Parch == 0:
            return 32
        elif Parch == 1:
            return 24
        elif Parch == 2:
            return 17
        elif Parch == 3:
            return 33
        elif Parch == 4:
            return 45
        else:
            return 30
        
    else:
        return Age


# In[23]:


titanic_data['Age']= titanic_data[['Age', 'Parch']].apply(age_approx, axis=1)
titanic_data.isnull().sum()


# In[24]:


## drop 2 embark values
titanic_data.dropna(inplace=True)
## Reset indexes
titanic_data.reset_index(inplace=True, drop=True)

print(titanic_data.info())


# In[25]:


## Converting categorical variables to a dummy indicators
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
gender_cat = titanic_data['Sex']
gender_encoded = label_encoder.fit_transform(gender_cat)
gender_encoded[0:5]


# In[26]:


titanic_data.head()


# In[27]:


# 1 = male / 0 = female
gender_DF = pd.DataFrame(gender_encoded, columns=['male_gender'])
gender_DF.head()


# In[28]:


embarked_cat = titanic_data['Embarked']
embarked_encoded = label_encoder.fit_transform(embarked_cat)
embarked_encoded[0:100]


# In[29]:


## there are three categories that we need to transform to a binary code
from sklearn.preprocessing import OneHotEncoder
## we transform one column into 3 colmns with 3 binary codes
binary_encoder = OneHotEncoder(categories='auto')
## create columns
embarked_1hot = binary_encoder.fit_transform(embarked_encoded.reshape(-1,1))
## we need to create a matrix
embarked_1hot_mat = embarked_1hot.toarray()
embarked_DF = pd.DataFrame(embarked_1hot_mat, columns = ['C', 'Q', 'S'])
embarked_DF.head()


# In[30]:


## To drop the old columns and have the new columns
titanic_data.drop(['Sex', 'Embarked'], axis=1, inplace=True)
titanic_data.head()


# In[31]:


## concatate the created varibales and add them to the dataset[titanic_data, gender_DF, embarked_DF]
titanic_dmy = pd.concat([titanic_data, gender_DF, embarked_DF], axis=1, verify_integrity=True).astype(float)
## print first 5 records
titanic_dmy[0:5]


# In[32]:


## Checking for independence between features
sb.heatmap(titanic_dmy.corr())


# In[33]:


## variables should be indepemdant of each other so we need to drop Fare and Pclass
titanic_dmy.drop(['Fare','Pclass'], axis=1, inplace=True)
titanic_dmy.head()


# In[34]:


## Checking that your dataset size is sufficient
titanic_dmy.info()


# In[35]:


## to check if we have sufficient data to run the model
## (6 predicted fitures and we need to have at least 50 records for each predicted fitures6*50)
## 0.2 is the 80-20 rule of seprating train and test data set
## 200 is set the seed?
X_train, X_test, y_train, y_test = train_test_split(titanic_dmy.drop('Survived', axis=1),
                                                   titanic_dmy['Survived'], test_size=0.2,
                                                   random_state=200)


# In[36]:


print(X_train.shape)
print(y_train.shape)


# In[39]:


X_train[0:5]


# In[40]:


y_train[0:5]


# In[41]:


## Deploying and evaluating the model
LogReg = LogisticRegression(solver='liblinear')
LogReg.fit(X_train, y_train)


# In[42]:


y_pred = LogReg.predict(X_test)


# In[43]:


## Model Evaluation
## Classification report without cross-validation
print(classification_report(y_test, y_pred))


# In[44]:


## K-fold cross-validation & confusion matrices
y_train_pred = cross_val_predict(LogReg, X_train, y_train, cv=5)
confusion_matrix(y_train, y_train_pred)


# In[45]:


precision_score(y_train, y_train_pred)


# In[ ]:


## Make a test prediction


# In[46]:


titanic_dmy[863:864]


# In[49]:


test_passenger = np.array([866, 40, 0, 0, 0,0,0,1]).reshape(1,-1)


# In[52]:


print(LogReg.predict(test_passenger))
print(LogReg.predict_proba(test_passenger))


# In[ ]:


## the person will survive, the probibility of the prediction being correct is 70%

