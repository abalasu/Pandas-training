import pandas as pd
import numpy as np

dict1 = {'name':['Arul','Jeya','Arul','Rekha', 'Rahim','John'],
         'lname':['Arul','Arul','Bright','Nair','Ulla','Peter'],
         'age':[51,47,np.nan,43,32,28],
         'sex':['M','F','M','F','M','M']}

dict2 = {'name':['a','b','c','d','e','f','g','h'],
         'state':['tn','ka','ts','tn','ts','tn','ka','tn'],
         'city':['vnr','blr','hyd','mdu','hyd','vnr','mys','vnr'],
         'salary':[2000,3000,2500,2200,3500,np.nan,2800,1800]}

dict3 = {'name':['a','b','c','d','e','f','g','h'],
         'bonus':[100,200,150,400,250,300,500,180]}

df1 = pd.DataFrame(dict1)
mean_age = df1['age'].mean()
df1['age'].fillna(mean_age,inplace=True)
# GroupBy
print("Groupby Examples ")
df2 = df1.groupby(by=['name','sex'],axis=0).mean('age')
print(df2)
df3 = pd.DataFrame(dict2)
mean_salary = df3['salary'].mean()
df3['salary'].fillna(mean_salary,inplace=True)

df4 = df3.groupby(['state','city']).count()
print(df4)
df4 = df3.groupby(['state','city']).mean('salary')
print(df4)

# Merge
df4 = pd.DataFrame(dict3)
df5 = df3.merge(df4,on='name')
print("Merge Example ")
print(df5)

# Conditions
print(df1.eq(['Arul','Jeya','Arul','Jeya','Rahim','John'],axis='index'))
print(df1.eq(['','Bright',46,'M']))

# Transformations
df2 = df1.groupby('sex')['age'].transform('mean')
print(df2)

# Most used Pandas methods
print(df1.head())
print(df1.describe())
print(df1.memory_usage())
print(df1.loc[1:3,['name','sex']])
print(df1['sex'].value_counts())
print(df1['name'].drop_duplicates())