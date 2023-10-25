import pandas as pd
import numpy as np

lol = [[1,2,np.nan], [3,np.NaN,4]]
df1 = pd.DataFrame(lol)
print(df1)

lol = [[1,3,5],[0,2,4],[1,2,3]]
df2=pd.DataFrame(lol,index=['row1','row2','row3'])
print(df2)
lol = [[0,2,4],[1,2,3]]
df3=pd.DataFrame(lol,index=['row4','row5'])
print(df3)

df4 = pd.concat([df2, df3],axis=1)
print(df4)

df5 = pd.read_csv("C:/Users/jeyar/OneDrive/Documents/Arulwork/TestFiles/school_master.csv", keep_default_na=True, na_values=['B001'],na_filter=True)
print(df5)

print(df5.fillna('X').iloc[0:7,0:4])
print(df5.fillna(method='ffill').iloc[0:7,0:4])
print(df5.fillna(method='bfill').iloc[0:7,0:4])
print(df5.interpolate().iloc[0:7,0:4])


df6 = pd.read_csv("C:/Users/jeyar/OneDrive/Documents/Arulwork/TestFiles/gapminder.tsv",sep=('\t'))
life_exp_over_years = df6.groupby(['year'])['lifeExp'].mean()

y2000 = life_exp_over_years[life_exp_over_years.index >= 2000]
print(y2000)

y2000 = y2000.reindex(range(2000, 2010))
print(y2000)

