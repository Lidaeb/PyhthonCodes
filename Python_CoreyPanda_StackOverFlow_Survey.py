#!/usr/bin/env python
# coding: utf-8

# Python_CoreyPanda_StackOverFlow_Survey

# In[ ]:


# import panda library
import pandas as pd


# In[ ]:


# define df as dataset or dataframe for future callings for csv files
df = pd.read_csv('C:/Users/lebad/Desktop/Personal enhancement/Job Enhancement/My projects/PYTHON/survey_results_public.csv')


# In[ ]:


# Shows the dataframe limited rows and columns
df


# In[ ]:


# Shows number of rows and columns
df.shape


# In[ ]:


#Show a limited cut of data
df.info


# In[ ]:


# Shows column names, Non-null Counts and data types
# object means string, float is decimal and int64 is int
df.info()


# In[ ]:


# To get and display all 48 columns when running df functions
pd.set_option('display.max_columns',48)


# In[ ]:


#Read Schema data file 
schema_df = pd.read_csv('C:/Users/lebad/Desktop/Personal enhancement/Job Enhancement/My projects/PYTHON/survey_results_schema.csv')


# In[ ]:


schema_df


# In[ ]:


schema_df.info()


# In[ ]:


# To get and display all 5 columns when running df functions
pd.set_option('display.max_columns',48)
# To get and display all 85 rows when running df functions
pd.set_option('display.max_rows',85)


# In[ ]:


# To get and display first 5 rows, () without number gives us 5
df.head(10)


# In[ ]:


# To get and display last 10 rows, () without number gives us 5
df.tail(10)


# In[ ]:


# To get the values of one  columns
df['Gender']


# In[ ]:


# To get the type of data
type('gender')


# In[ ]:


# To get the type of data in a framework result in pandas.core.series.Series
type(df['Gender'])


# In[ ]:


# To get the data frames column /should be case sensetive
df.Gender


# In[ ]:


# To access multiple columns/ Casesensetive
df[['Age','Gender']]


# In[ ]:


# To just get the name of olumns
df.columns


# In[ ]:


# To just get the name/value of rows which starts from 0
df.iloc[0]


# In[ ]:


# To just get the name/value of multiple rows/ which starts from 0/you need to use brackets because you are passing a list(more than one)
df.iloc[[0,3]]


# In[ ]:


# To just get the name/value of row 0,34 and 3 and columns name/values of 0,1,2,3,4 /Using integers for location
df.iloc[[0,34,3],[0,1,2,3,4]]


# In[ ]:


# To just get the name/value of row 0,34 and 3 and columns name/values of 0,1,2,3,4 /Using Labels for location
df.loc[[0,34,3,8880],['Age','Gender','Employment','US_State','DevType']]


# In[ ]:


# To get the unique value of the data for one columns(like DISTINCT COUNT)/accepts multiple column name as a LIST
df['US_State'].value_counts()


# In[ ]:


# TO get a slice of data/Casesensitive/get a data range
df.loc[2:5,'Age':'Accessibility']


# In[ ]:


# To assign an index to a dataset/ it doesn't changes the original dataset
df.set_index('ResponseId')


# In[ ]:


# To assign an index to a dataset
df.set_index('ResponseId', inplace = True)
df


# In[ ]:


df.index


# In[ ]:


df.iloc[0]


# In[ ]:


# To reset the index
df.reset_index(inplace= True)
df


# In[ ]:


# We can assign the data when we get the data we can do it when we load the data in
df = pd.read_csv('C:/Users/lebad/Desktop/Personal enhancement/Job Enhancement/My projects/PYTHON/survey_results_public.csv', index_col= 'ResponseId')


# In[ ]:


df.head()


# In[ ]:


#schema_df.loc['Gender','question']
#schema_df


# In[ ]:


# To filter data/ works like a mask for data
df['Gender'] == 'Men'


# In[ ]:


# To get the filtered data you can define a variable and then get the data later/ () is just to seprate two =s
filt = (df['Gender'] == 'Man')


# In[ ]:


# the other way to filter
df.loc[filt]
#df.loc[filt,'Country'] if we want to have data related to filtered data


# In[ ]:


# And and Or & |
filt2 = (df['Gender'] == 'Man') & (df['LearnCode'] == 'School') & (df['Country'] == 'Brazil')


# In[ ]:


df.loc[filt2]


# In[ ]:


# And and Or & | Have Tilda ~
filt3 = (df['Gender'] == 'Man') & (df['LearnCode'] == 'School') & (df['Country'] == 'Brazil')
df.loc[filt3,['Gender','LearnCode','Country']]


# In[ ]:


# NOT And and Or & | Have Tilda ~
filt4 = (df['Gender'] == 'Man') & (df['LearnCode'] == 'School') & (df['Country'] == 'Brazil')
df.loc[~filt4,['Gender','LearnCode','Country']]


# In[ ]:


# NOT And and Or & | Have Tilda ~
filt5 = (df['Gender'] == 'Man') & (df['LearnCode'] == 'School') | (df['Country'] == 'Brazil')
df.loc[~filt5,['Gender','LearnCode','Country']]


# In[ ]:


# NOT And and Or & | Have Tilda ~
filt6 = (df['Gender'] == 'Man') 
df.loc[~filt6,['Gender','LearnCode','Country']]


# In[ ]:


# filter a list
countries = ['United States of America','Germany','Israel','Norway',]
filt7 = df['Country'].isin(countries)
df.loc[filt7,['Gender','LearnCode','Country']]


# In[ ]:


# To filter part of a string
# na = false is for NaN values to scape them
filt8 = df['Employment'].str.contains('Student',na = False)
df.loc[filt8,['Employment','Gender','LearnCode','Country']]


# In[ ]:


# To replace or rename all column names you have to have them all in your list
# df.columns = ['x','y','z,....']
# To change the column names to uppercase/lowe 
df.columns = [x.upper() for x in df.columns]
df.columns


# In[ ]:


# To remove Spaces
df.columns = df.columns.str.replace(' ','_')
df.columns


# In[ ]:


# Without inplace it wouldn't change it in dataset
df.rename(columns = {'EMPLOYMENT':'Employ'}, inplace= True)
df.columns


# In[ ]:


# To replace the value
df.at[2,'Gender'] = 'Man'


# In[ ]:


# To replace the value
filter9 = (df['Gender'] == 'Man')
df.loc[filter9 ,'Gender'] = 'Male'
df


# In[ ]:


# To replace a column as a lower/upper case
df['US_State'] = df['US_State'].str.upper()


# In[ ]:


df['US_State']


# In[ ]:


# To calling a function on our values
df['Country'].apply(len)


# In[ ]:


# To get the max lenght of the column value
df['Country'].apply(len).max()


# In[ ]:


# To define a function
def update_Country(Country):
    return Country.upper()
df['Country'] = df['Country'].apply(update_Country)


# In[ ]:


df['Country'] 


# In[ ]:


# To define a function with lambda used with series
df['Country'] = df['Country'].apply(lambda x: x.lower())


# In[ ]:


df['Country'] 


# In[ ]:


# To define a function with the dataframe/ it will give us the number of rows
df.apply(len)


# In[ ]:


# To give you number of columns
df.apply(len, axis = 'columns')


# In[ ]:


# To get the min of columns with numeric value
df.apply(lambda x: x.min)


# In[ ]:


# To get lenght for all str values
df.applymap(len)


# In[ ]:


# Make them all lowercase
df.applymap(str.lower)


# In[ ]:


# To substitue some of our values
df['Gender'].map({'Male':'Men'})
# It will replace the notmentioned values with NaN


# In[ ]:


# To substitue some of our values
df['Gender'].replace({'Male':'Men'})
# it will not change the dataset


# In[ ]:


# To change the values in dataset we use this
df['Gender']= df['Gender'].replace({'Male':'Men'})


# In[ ]:


df.rename(columns={'ConvertedCompYearly': 'SalaryUSD'}, inplace = True)


# In[ ]:


df['SalaryUSD']


# In[ ]:


# To map Yes and No to Boilean value
df['Trans'].map({'Yes': True, 'No':False})
df['Trans']


# In[ ]:


df['Trans'] = df['Trans'].map({'Yes': True, 'No':False})
df['Trans']


# In[ ]:


# To add or remove columns
# To concat two columns
df['New Column']= df['Gender']+ '  '+df['Age']


# In[ ]:


df


# In[ ]:


# To drop a columns
# To make it permanet use inplace
df.drop(columns ='New Column', inplace = True)
df


# In[ ]:


# To Split
df['New Column'].str.split(' ')


# In[ ]:


# To Split in two columns
df['New Column'].str.split(' ',expand = True)


# In[ ]:


# To Split in two columns in columns
df[['Gender1','Age1','3','4','5','6','7','8','9','10','11','12','13','14']]=df['New Column'].str.split(' ',expand = True)


# In[ ]:


df


# In[ ]:


# To add a row
df.append({'Gender':'WTF'}, ignore_index = True)


# In[ ]:


# To append two dataframe
#  df= df.append(df2,ignore_index = True, sort = False)


# In[ ]:


# To remove a row by index
df.drop(index = 83438, inplace= True)


# In[ ]:


# To remove a row by index by looking for it
df.drop(index = df[df['Country']=='Canada'].index, inplace= True)
df['Country']
# Or have it this way
filt76 = df['Country']=='Canada'
df.drop(index = df[filt76].index, inplace= True)
df['Country']


# In[ ]:


# Sort by 1 attribute
df.sort_values(by = 'Country',ascending = False)


# In[ ]:


# Sort by >1 attribute
df.sort_values(by = ['Country','Age'],ascending = False)


# In[ ]:


# Sort by >1 attribute
df.sort_values(by = ['Country','Age'],ascending = False)


# In[ ]:


# Sort by >1 attribute asc and desc
df.sort_values(by = ['US_State','UK_Country'],ascending = [False,True])


# In[ ]:


df.sort_index()


# In[ ]:


df['US_State'].sort_values()


# In[ ]:


df[['US_State','LearnCode']].sort_values(by = 'US_State',ascending = True)
df[['US_State','LearnCode']].head(50)


# In[ ]:


df.columns


# In[ ]:


# To get the 10 largest number
df['SalaryUSD'].nlargest(10)


# In[ ]:


df.nlargest(10,'SalaryUSD')


# In[ ]:


df['SalaryUSD'].nsmallest(10)


# In[ ]:


# Grouping and Aggregating data
Median = df['SalaryUSD'].median()
Median


# In[ ]:


# for all numeric numbers
df.median()


# In[ ]:


Mean = df['SalaryUSD'].mean()
Mean


# In[ ]:


df.mean()


# In[ ]:


# To get aggregated info on numeric data
# count is count of non missing values
df.describe()


# In[ ]:


df['SalaryUSD'].count()


# In[ ]:


df.columns


# In[ ]:


# To get the count of value counts
df['Trans'].value_counts()


# In[ ]:


df['Gender'].value_counts()


# In[ ]:


df['Gender'].value_counts(normalize= True)


# In[ ]:


df.columns


# In[ ]:


df['OrgSize'].value_counts(normalize= True)


# In[ ]:


df['OrgSize'].value_counts(normalize= False)


# In[ ]:


# Group by
OrgGroup = df.groupby(['OrgSize'])


# In[ ]:


OrgGroup.get_group('20 to 99 employees')


# In[ ]:


# Filter does the same
filt76 = df['OrgSize'] == '20 to 99 employees'
df.loc[filt76]['Gender'].value_counts()


# In[ ]:


# To get more of aggregated
df.columns
CountryGroup = df.groupby(['Country'])
CountryGroup['SalaryUSD'].median()


# In[ ]:


CountryGroup = df.groupby(['Country'])
CountryGroup['SalaryUSD'].agg(['median','mean','max','min'])


# In[ ]:


# To answer : What % of people from each country know coding from school?
country_resp = df['Country'].value_counts()
country_resp


# In[ ]:





# In[ ]:


#School_df = pd.concat([country_resp,country_sc],axis= 'rows',sort= False)
#School_df


# In[ ]:


country_sc = CountryGroup['LearnCode'].apply(lambda x: x.str.contains('School').sum())
country_sc 


# In[1]:



#Note they are without '' /using axis because by default its rows
School_df = pd.concat([country_resp,country_sc],axis= 'columns',sort= False)
School_df


# In[ ]:


School_df.rename(columns= {'Country':'Respondants','LearnCode':'LearnInSchool'},inplace= True)
School_df


# In[ ]:


School_df['PCT']=(School_df['LearnInSchool']/School_df['Respondants'])*100
School_df.sort_values(by = 'PCT',ascending = False,inplace= True)
School_df.head(30)


# In[ ]:


School_df.loc['japan']


# In[ ]:


# Clean values
import numpy as np


# In[ ]:


df.columns


# In[ ]:


# if you want to delet listwise missing value
df.dropna()
# default values in () are axis= 'index', how='any'
df.columns
df.dropna(axis= 'index', how='all')
# it will drop values that all values are missing
# if it says axis='columns' it will drop whole column that have missing values


# In[ ]:


# drop rows in a custome attribute
df.dropna(axis='index', how='all',subset=['LearnCode'],inplace = True)


# In[ ]:


# To drop customized missing values
df.replace('NA',np.nan, inplace= True)
df.replace('Unknown',np.nan, inplace= True)


# In[ ]:


#Gives us a mask of if a value is missing
df.isna()


# In[ ]:


# To change values
df.fillna('MISSING')
# To make it perminent use inplace


# In[ ]:


# To get data type
df.dtypes


# In[ ]:



# NaN is a float underhood
type(np.NaN)


# In[ ]:


# To cast
# df['age'] = df['age'].astype(float)


# In[ ]:


df.columns


# In[ ]:


df['Age'].value_counts()


# In[ ]:


# See unique values
df['Age'].unique()


# In[ ]:


df['Age'].replace({'25-34 years old':'29','18-24 years old':'22', 'Prefer not to say':'0',
       '45-54 years old':'48', 'Under 18 years old':'9', '35-44 years old':'39',
       '65 years or older':'70', '55-64 years old':'62', nan]:'0'}, inplace=True)


# In[ ]:


#df['Age'].replace( nan:'0', inplace=True)

df['Age'].unique()


# In[ ]:


df['Age'] = df['Age'].astype(float)


# In[ ]:


df['Age'].mean()


# In[ ]:


# Work with Time and Date data
# if we have a datetime do as below
# if it is not a datetime type we can convert it
# df['Date'] = pd.to_datetime(df['Date'])
# if you get an error you can give it the format as well
# - http://bit.ly/python-dt-fmt
# df['Date'] = pd.to_datetime(df['Date'],format = 'Y-%m-%d %I-%p')
# get the day name/ df['Date'].day_name()
# if you want to get the data from begining as Date use 
# d_parser = lambda x:pd.datetime.strptime(x, 'Y-%m-%d %I-%p')
# df= pd.read_csv('X\f\v.csv'. parse_dates= ['Date'],date_parser = d_parser )


# In[ ]:


# if we want to get the dayname
# df['Day'] = df['Date'].dt.day_name()


# In[ ]:


# To see earliest and Latest
# df['Date'].min()  or .max()
# df['Date'].max()-df['Date'].min()


# In[ ]:


# To do filters on Date
# filt = (df['Date']>'2020')
# df.loc[filt]
# # filt = (df['Date']>'2020') & (df['Date']<'2022')
# df.loc[filt]
# filt = (df['Date']>pd.to_datetime('2019-01-01')) & (df['Date']<pd.To_datetime('2022-01-01'))
#
# df.set_index('Date', inplace= True)
# df['2019'] gives you the data for 2019 when you set date as index
# df['2020-01':'2020-03']
# df['2020-01':'2020-03']['Attribute'].mean()
# gives you the average of attribute in the days it has been filtered
# http://bit.ly/pandas-dt-fmt


# In[ ]:


# To group by hourly dates by day and maximum value 
#highs = df['Attribute'].resample('D').max()


# In[ ]:


# Plot a line
# %matplotlib inline


# In[ ]:


# highs.plot()


# In[ ]:


# df.resample('W').mean() gives you the avg for all numeric attributes weekly


# In[ ]:


# df.resample('W').agg({'At1':'mean','At2':'max','At3':'min'})


# In[ ]:


# To read and write data from varoius sources
# dp = pd.read_xlx(fileaddress, index_col= 'PrimaryKey')


# In[ ]:


# Tabdelimitedfiles filt_df.to_csv('address/filename.tsv', sep= '\t')
# For Tabseprated file also pd.read_table(Address on local or on web like 'http://bit.ly/chiporders')
# Another example
# user_cols = ['userid','age','gender','occupation','zip_code']
# users= pd.read_table('http://bit.ly/movieusers', sep='|',header=None , names= user_cols)


# In[ ]:


# To export the data frame to csv first filter the data as you wish and name it then
# filt_df.to_csv('address/filename.csv')


# In[ ]:


# to write as an Excel you need to pip install
# pip install xlwt /for xlx format
# pip install xlwt openpyxl / for xlxs format
# pip install xlwt openpyxl xlrd / to read xlxs format as well


# In[ ]:


# df.to_excel(address/filename.xlxs)
# df.to_json(address/filename.json, orient='record',lines= True) to have each record in a line
# To get data from DB
# first pip install SQLAlchemy 
# for Postgres
# pip install psycopg2-binary
from sqlalchemy import create_engine
import psycopg2


# In[ ]:


# for postgres first userpass then server,port, and db name
#engine= create_engine('postgressql://dbuser:dbpass@localhost:5432/sample_db')
#to export to sql: df.to_sql('sample_table',engine, if_exists = 'replace')
# we can replace or append or other options


# In[ ]:


# read data 
#engine= create_engine('postgressql://dbuser:dbpass@localhost:5432/sample_db')
# sql_df = pd.read_sql('sample_table',engine, index_col='At1')
## to read a query
## sql_df = pd.read_sql_query('select * from sample_table',engine, index_col='At1')


# In[ ]:


# to upload data(json) from URL
# df = pd.read_json('URLAddress')

