import pandas as pd
import numpy as np

l1 = {'id':['1','2','1','5'], 'salary':[4000, 2000, 3500, 5000]}
df1 = pd.DataFrame(l1)
print(df1)
print('Filtered slary > 3500')
val = 3500
print(df1.query('salary > @val'))
print(df1.groupby('id').sum('salary'))
print(df1['salary'].mask(df1['salary']>3500,9999))
"""
school_df = pd.read_csv("C:/Users/jeyar/OneDrive/Documents/Arulwork/TestFiles/school_master.csv")
board_df = pd.read_csv("C:/Users/jeyar/OneDrive/Documents/Arulwork/TestFiles/board_master.csv")
state_df = pd.read_csv("C:/Users/jeyar/OneDrive/Documents/Arulwork/TestFiles/state_master.csv")

print(school_df)
print(board_df)
print(state_df)

# Inner Join
merge_df1 = school_df.merge(board_df, how='inner', left_on='board_id', right_on = 'board_id')
print(merge_df1)

# Left outer Join
merge_df2 = school_df.merge(board_df, how='left', left_on='board_id', right_on = 'board_id')
print(merge_df2)

# Right outer Join
merge_df3 = school_df.merge(board_df, how='right', left_on='board_id', right_on = 'board_id')
print(merge_df3)

# Outer Join
merge_df4 = school_df.merge(board_df, how='outer', left_on='board_id', right_on = 'board_id')
print(merge_df4)
"""