# 10 ways to create a dataframe

import pandas as pd
import numpy as np

#1. from list of lists
l1 = [[1,2,5],[5,2,1],[7,2,4],[3,1,3]]
df1 = pd.DataFrame(l1)
print(df1)

#2. from list of lists and adding row and col labels
l1 = [[1,2,5],[5,2,1],[7,2,4],[3,1,3]]
df2 = pd.DataFrame(l1, columns=['col1', 'col2', 'col3'], index=['row1', 'row2', 'row3', 'row4'])
print(df2)

#3. from series to dataframes. axis=0 by default which concats as rows, axis=1 concats as columns
l1 = [1, 3, 5]
l2 = [0, 2, 4]
s1 = pd.Series(l1)
s2 = pd.Series(l2)
df3 = pd.concat([s1, s2], axis=1)
df3.columns=['odd','even']
print(type(df3))
print(df3)

#4. from list of tuples
l1 = [(1,2,3), (4,5,6), (7,8,9)]
df4 = pd.DataFrame(l1)
print(df4)

#5. from dictonaries
dict1 = {'name':['arul','ram','jay','sita'],
         'age':[51,55,62,25],
         'sex':['m','m','m','f']}
df5 = pd.DataFrame(dict1)
print(df5)

#6. from csv files
df6 = pd.read_csv("C:/Users/jeyar/OneDrive/Documents/Arulwork/TestFiles/ser.csv")
print(df6)

#7. from json files
df7 = pd.read_json("C:/Users/jeyar/OneDrive/Documents/Arulwork/TestFiles/input_movie_data.json")
print(df7)

#8. from excel files
df8 = pd.read_excel("C:/Users/jeyar/OneDrive/Documents/Arulwork/TestFiles/test_data.xlsx")
print(df8)

#9. from the zip function on lists
name_list = ["arul", "ram", "sita", "maddy"]
age_list = [51, 55, 46, 18]
sal_list = [1000, 2000, 1800, 3000]
combined_list = list(zip(name_list, age_list, sal_list))
df9 = pd.DataFrame(combined_list, columns=["name","age","salary"])
print(df9)

#10. from raw data (the 1st list is taken as the data, 2nd list is taken as the index)
df10 = pd.DataFrame(['arul','ram','sita'],[1,2,3])
print(df10)

#11. creating NaN values in a Data frame using np
l1 = [[1,2,5],[5,np.nan,1],[7,2,4],[np.nan,1,3]]
df11 = pd.DataFrame(l1)
print(df11)

#12. creating NaN values in a Dataframe using to_numeric function
l1 = {'id':[1,"arul",'3','5'], 'salary':[4000, 2000, 'xyz', 5000]}
df12 = pd.DataFrame(l1)
print(df12)
df12 = pd.concat([pd.to_numeric(df12['id'], errors='coerce'),pd.to_numeric(df12['salary'], errors='coerce')],axis=1)
print(df12)
#df12 = pd.to_numeric(df12['id'], errors='coerce')
#print(df12)

#13. creating dataframes using linspace, random and range functions
df13 = pd.DataFrame([range(1,10,2), range(3,15,3), np.linspace(1,30,5,dtype=float), np.random.randint(low=10, high=20, size=4)])
print(df13)

#14. Reading from a Tab Delimited File
df14 = pd.read_csv("C:/Users/jeyar/OneDrive/Documents/Arulwork/TestFiles/gapminder.tsv", sep='\t')
# Functions in Dataframes
# print(dir(df1))
print("The shape of df1 is ", df1.shape)
print("The columns of df7 are ", df7.columns)
print("The Datatypes of columns in df7 are ", df7.dtypes)
print("Some basic info about df12 is ", df12.info())
print("The first 3 rows of df14 \n", df14.head(n=3))
print("The last 5 rows of df14 \n", df14.tail())
print("Only Country Names from df14 \n", df14["country"])
print("Only Country and Continent Names from df14 \n", df14[["country", "continent"]])
print("The 16th row of df14 using the loc function \n", df14.loc[15])
print("The last 5 rows using the iloc funtion in reverse order \n", df14.iloc[[-1, -2, -3, -4, -5]])
print("List of Unique countries in df14 \n", df14["country"].unique())
print("Number of unique countries in df14 \n", df14["country"].nunique())
boolean_mask = (df14["country"]=='India') & (df14["year"] == 2007)
print("List all the entries of df14 where country is India ", df14.where(boolean_mask).dropna())


df15 = df14.where((df14["country"] == 'India') & (df14['year'] > 2000))
print(df15.dropna())

df16 = df15.dropna().to_markdown()
print(df16)

df17 = df14.groupby(['country','continent'])
print('Type of groupby: ', type(df17))
print(df17)
# groups show the groups and all the row indexes which match the group
print(df17.groups)
# first() prints the first record of each of the data frame group
print(df17.first())

for name, group in df17:
    print(name)
#   print(group)

print(df17.get_group(('India','Asia')))
print(df17['pop'].agg(np.mean))
# Aggregate functions on Dataframegroups
df18=df17.get_group(('India','Asia'))
print(df18['gdpPercap'].agg([np.mean]))

# To get the max rows for specific columns using the max funtion followed by the where function
maxpop = df14['pop'].max()
print(df14.where(df14['pop'] == maxpop).dropna())

# To get the mean of all numeric fields grouped at a country level
print(df14.groupby('country').mean())

# To get the mean life expectancy across the globe 
print(df14.groupby('year')['lifeExp'].mean())

# To get the countries mean 
print(df14.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean())

# Print the number of countries in each Continent
print(df14.groupby(['continent'])['country'].nunique())

car_makers = pd.DataFrame(data={'parentname':['Honda', 'Ford', 'Toyota', 'GM', 'Honda', 'Tata'],
                                'country':['Japan', 'US', 'Japan', 'US', 'Japan', 'India'],
                                'vol':[3232, 2321, 5332, 2443, 750, 300]
                                }, 
                          index=['Honda', 'Ford', 'Lexus', 'Chevy', 'Acura', 'Range Rover'],
                          columns=['parentname','country','vol'])
print(car_makers)

car_series = car_makers.loc['Acura']
print(car_series)

print(car_series.index)
print(car_series.values)
print(car_series.keys())

