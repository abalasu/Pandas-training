import pandas as pd
"""
mydict = {"Name": ['Arul', 'Raj', 'Madhan', 'Vandan'],
          "Age": [51, 52, 51, 43],
          "City": ['Bangalore', 'Bangalore', 'Chennai', 'Hyderabad']}

df = pd.DataFrame(mydict)
df.set_index("Name")
print(df[['Name', 'City']])
print(df.Name, df.City)
"""
df1 = pd.read_csv("d:/pythondata/melb_csv_data.csv")
df1.set_index('Suburb')
print(df1.index)
x = df1['Postcode'][1]
print(x)

print(df1.loc[df1.Suburb.isin(['Abbotsford', 'Airport West'])])

print(df1.iloc[0,0])