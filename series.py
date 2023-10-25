# 11 ways to create Pandas series
import pandas as pd
from numpy import array, linspace, random, arange

#1. From Lists
l1 = [2, 3, 5, 4, 3]
s1 = pd.Series(l1)
print(s1)

#2. From arrays
arr = array(l1)
s2 = pd.Series(arr)
print(s2)

#3. From dict
dict1 = {'name':'Arul', 'age':51, 'sex':'M'}
s3 = pd.Series(dict1)
print(s3)

#4. From scalar values
s4 = pd.Series(5, index=['a', 'b', 'c', 'd', 'e'])
print(s4)

#5. From numpy linspac method
s5 = pd.Series(linspace(1, 20, 5, dtype=int), index=[1, 2, 3, 4, 5])
print(s5)

#6. From numpy random.rand methods
s6 = pd.Series(random.randint(low=1, high=15, size=5, dtype=int), index=['a', 'b', 'c', 'd', 'e'])
print(s6)

#7. From the range method
s7 = pd.Series(range(10, 20, 3), index=['first', 'second', 'third', 'fourth'])
print(s7)

#8. From mathematical expressions
t = arange(5, 10)
s8 = pd.Series(data=t*5, index=t)
print(s8)

#9. From a Dataframe
l2 = [['a', 'b', 'c'],['d','e','f']]
df = pd.DataFrame(l2, index=['first', 'second'])
s9 = pd.Series(df[0])
print(s9)

#10. Using the data frame squeeze function 
l2 = [['a'],['d']]
df = pd.DataFrame(l2, index=['first', 'second'])
s10 = df.squeeze()
print(s10)
print(type(s10))

#11. Creating from sets
set1 = (2, 1, 5, 3, 6, 'a', 'c')
s11 = pd.Series(set1)
print(s11)

# Operations on Series
# print(dir(s1))

#help(s1)
# __add__ -> add's the number to each element in the series
print('Other Operations')
print(s1.mean())
print(s1.median())
print(s1.mode())
print(s1.min())
print(s1.max())
print(s1.value_counts())
# unique - prints the unique elements in the series
print(s1.unique())
# nunique - prints the count of unique elements in the series
print(s1.nunique())
print(len(s1))

print('Ways to access specific elements of a Series')
# Ways to access Series elements
#1. Using index
print(s1[1])

#2. Using named index
print(s7['third'])

#3. Using the position parameter to pull out specific ranges as a series
print(s2[0:3])

#4. Using the position parameter to pull out specific elements as a list
print(s2[1:5].values)
print(s2[-1:].values)

print(s2)
# print s2 in reverse as a series
print(s2[::-1])
# print first 5 elements
print(s2[:5])

# Access using loc method and the named index
print(s7.loc['second'])

# Access using iloc method and index
print(s2.iloc[1])