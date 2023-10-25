import pandas as pd

df1 = pd.read_csv("C:/Users/jeyar/OneDrive/Documents/Arulwork/TestFiles/pew.csv")
print(df1)

df2 = pd.melt(df1, id_vars=['religion'], var_name='income', value_name='count')
print(df2[df2.index<10])

lol = {'name':['arul', 'ram', 'jeya', 'bhavna'],
       'sex':['M','M','F','F'],
        'mt':['Tamil', 'English', 'Tamil', 'Telugu']}
df3 = pd.DataFrame(lol)
print(df3)
df4 = pd.get_dummies(df3['sex'],drop_first=True)
print(df4)
df5 = pd.get_dummies(df3['mt'],drop_first=True)
print(df5)
df6 = pd.concat([df3, df4, df5], axis=1)
print(df6)