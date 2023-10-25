import pandas as pd
import numpy as np
print('Reading from CSV file')
df1 = pd.read_csv('d:/pythondata/pre_process.csv')
print(df1)
print('The head() method is used to print the top 5 records')
print(df1.head())
x = input('Hit Enter')

print('Reading from Excel file')
df2 = pd.read_excel('d:/pythondata/Rainfall data.xlsx')
print(df2)
print('The to string function is used to print all the data')
print(df2.to_string())
print('Use the Describe method to give a description of the data')
print(df2.describe())
x = input('Hit Enter')

print('Creating a Dataframe from a dict')
dict1 = {'fname':['A','B','C','D','E','F'],
         'lname':['M','N','O','P','Q','R'],
         'gende':['m','m','f','f','f','f'],
          'dept':[1,2,3,np.NaN,4,1],
          'loca':['S','E','W',np.NaN,'N','S'],
          'salary':[5000,4000,6000,4500,np.NaN,5000]}
df3 = pd.DataFrame(dict1)
print(df3)
print('The info method gives a crisp description of the structure of the dataframe')
print(df3.info())

df4_cols = ['gende','dept','loca']
df5_cols = ['salary']

df4 = df3[df4_cols]
df5 = df3[df5_cols]
print(df4)
print(df5)

x = input('Hit Enter')
print('Accessing Specific Elements')
print("All Depts are \n",df4['dept'])
print("fname of the 3rd person in the Dataframe \n",df3['fname'][2])

x = input('Hit Enter')
print('fillna and dropna methods')
print(df3)
arr_mode = df3['dept'].mode()
df3['dept'].fillna(value=arr_mode[0],inplace=True)
arr_sal = df3['salary'].mean()
df3['salary'].fillna(value=arr_sal,inplace=True)
print(df3)
df3.dropna(inplace=True)
print(df3)

x = input('Hit Enter')
print('Encoding')
df3['loca'] = df3['loca'].map({'S':1,'E':2,'W':3,'N':4})
print(df3)