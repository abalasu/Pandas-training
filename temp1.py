import pandas as pd

def adjustments(m):
    return m + 5

my_df = pd.read_csv('d:/pythondata/Marks.csv',header='infer')
print(my_df)

table = pd.pivot_table(my_df,index=['Name'],values='Marks',aggfunc='sum')
print(table)

table = pd.pivot_table(my_df,index=['Subject'],values='Marks',aggfunc='sum')
print(table)

my_df['Marks'] = my_df['Marks'].transform(adjustments)
print(my_df)
"""
d1 = {'name':['arul','john','sam','radha','sita'],
      'age':[52,np.NaN,50,53,43],
      'gender':['m','m','m','f','f']
      }
df1 = pd.DataFrame(d1)
df1.index = pd.Index(['row-1','row-2','row-3','row-4','row-5'])
#df1.columns = ['n','a','g']
print(df1)
print('Size of DF is ', df1.size)
print('Dimension of DF ',df1.ndim)
df1.fillna(method='bfill',inplace=True)
df1.dropna(axis=1,inplace=True)
print(df1)
#print(df1.loc[[2,3,4]])
print(df1.iloc[[2,3,4]])
print(df1['name'])

df2 = pd.DataFrame([['a','b','c'],['x','y','z'],[1,2,3]])
print(df2)
print(df2.loc[:,[0,1]])
"""