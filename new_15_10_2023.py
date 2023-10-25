import pandas as pd

def map_staff_rank(x):
    code = 0
    if x == 'A':
        code = 1
    elif x == 'B':
        code = 2
    elif x == 'C':
        code = 3
    elif x == 'D':
        code = 4
    elif x == 'E':
        code = 5
    return code

df = pd.read_csv('d:/pythondata/student_percentage.csv')
df.columns = ['Student_id', 'Sci_hrs', 'Math_hrs', 'Staff_Rank', 'Marks_Scored']
print(df)

print(df['Staff_Rank'].mode())
print(type(df['Staff_Rank'].mode()))

df['Sci_hrs'] = df['Sci_hrs'].fillna(value=df['Sci_hrs'].mean())
df['Math_hrs'] = df['Math_hrs'].fillna(method='ffill')
df['Marks_Scored'] = df['Marks_Scored'].fillna(method='bfill')
df['Staff_Rank'] = df['Staff_Rank'].fillna(value=df['Staff_Rank'].mode()[0])
df['Staff_Rank'] = df['Staff_Rank'].map(map_staff_rank)
print(df.to_string())

df1 = df.copy()
df1.drop(columns='Marks_Scored', inplace=True)
print(df1.to_string())

df2 = df['Marks_Scored']
print(df2.to_string())