import pandas as pd
import pickle
import os


raw_data = {'first_name': ['Sheldon', 'Raj', 'Leonard', 'Penny', 'Howard', 'Amy'],
                'last_name': ['Copper', 'Koothrappali', 'Hofstadter', 'Hofstadter', 'Wolowitz', 'Fowler'],
                'age': [42, 38, 36, 32, 41, 35],
                'Comedy_Score': [9, 7, 8, 9, 8, 5],
                'Rating_Score': [25, 25, 49, 80, 62, 70]}

df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age','Comedy_Score', 'Rating_Score'])
#print(df)

df1 = df.where(df.last_name == "Hofstadter")
df1.dropna(axis=0, how='any', inplace=True)
#print(df1)

os.chdir('c:/Users/jeyar/OneDrive/Documents/Arulwork/TestFiles')
df = pd.read_csv('tips1.csv', header=0, index_col=["tip","time", "sex"])
df.to_pickle('DfPickle.pk1')

new_df = pd.read_pickle('DfPickle.pk1')
print(new_df)
first = new_df.query('tip == 3.21', inplace=False)
#first = new_df.query('tip == 3.21 and time == "Dinner" and sex == "Male"', inplace=False)

print("The final list")
print(first)


#df1 = pd.read_table('tips1.csv')
#print(df)
#print(df1)

#df2 = pd.read_clipboard()
#print(df2.to_string())

