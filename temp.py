# importing the module
import pandas as pd

print(help(pd))
 
# create 2 series objects
series_1 = pd.Series([2, 4, 6, 8])
series_2 = pd.Series([10, 12, 14, 16])
print(type(series_1))
# adding series_2 to series_1 using the concat() function
df1 = pd.concat([series_1, series_2], axis=0)
print(df1)
df2 = pd.concat([series_1, series_2], axis=1)
df2.columns = ['a','b']
print(df2)
df3 = pd.concat([series_2, series_1], axis=1)
df3.columns = ['a','d']
print(df3)
df4 = pd.concat([df2, df3], axis=0, ignore_index=True)
print(df4)
df4 = pd.concat([df2, df3], axis=1, ignore_index=False)
print(df4)
df5 = pd.concat([df2, df3], axis=1, ignore_index=True)
print(df5)
df6 = pd.concat([df2, df3], axis=0, ignore_index=False, join='inner')
print(df6)
df7 = pd.concat([df2, df3], axis=0, ignore_index=False, join='outer')
print(df7)
pd.ExcelWriter('step1')
df2.index = [1,2,3,4]
df3.index = [0,1,2,3]
df8 = pd.concat([df2, df3], axis=1, ignore_index=True)
print(df8)


