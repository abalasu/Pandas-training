import pandas as pd
import os
import matplotlib.pyplot as plt

#a = [1, 3, 5, 7]
#b = pd.Series(a, index=["a","b","c","d"])
#print(b)
#calories={"Day1":340, "Day2":480, "Day3":420, "Day4":640}
#c = pd.Series(calories, index=["Day1", "Day3"])
#print(c)

#data = {"Calories":[430, 400, 410],
#        "Duration":[45, 40, 42]}

#d = pd.DataFrame(data, index=["Day1","Day2","Day3"])

#print(d)
#print(d.loc["Day2"])
os.chdir('c:/Users/jeyar/OneDrive/Documents/Arulwork/TestFiles')
def new_func():
    df = pd.read_csv('tips3.csv',header=0)
    return df

df = new_func()
print(df.info())
print(df.head())
df.dropna(inplace=True)
print(df.head())
print(df.corr())

df.plot(x = "size", y = "tip")

plt.show()