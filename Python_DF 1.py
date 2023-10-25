import pandas as pd

# Creating DF from CSV files
# df = pd.read_csv('C:/Users/jeyar/OneDrive/Documents/Arulwork/TestFiles/gapminder.tsv', sep='\t')
# print(df)

# print(df.size)
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.info())
# subset = df[['country', 'continent', 'year']]
# print(subset)
# print(subset.to_string(columns=['country', 'year'], header=['country1', 'year1'], index=False, justify='center'))
# print(pd.__version__)
# print(subset.loc[[1, 2, 4]])
# print(pd.options.display.max_rows)

# Creating DF from JSON
# df_from_json = pd.read_json('C:/Users/jeyar/OneDrive/Documents/Arulwork/TestFiles/data.json')
# print(df_from_json)

# Creating DF from 2 Series
# data = {
#  "calories": [420, 380, 390],
#  "duration": [50, 40, 45]
# }
# myvar = pd.DataFrame(data)
# print(myvar)

# Creating DF from Dictionary of Dictonaries
data = {
    "child1":{"name":"Arul", "Age":51, "Sex":"M"},
    "child2":{"name":"Santa", "Age1":53, "Sex":"F"}
       }
df = pd.DataFrame(data)
print(df)
print(df.columns)
df1 = df.transpose()
print(df1)
print(df1.columns)
