import pandas as pd
import matplotlib.pyplot as plt

p_and_l = {'bu_id':[1,1,1,1,1,1],
           'month':['jan','feb','mar','apr','may','jun'],
           'cost':[8000,7000,8500,7500,8500,7800],
           'revenue':[12000,11000,13000,12000,14000,12500]}
bu = {'bu_id':[1,2,3,4,5],
      'by_name':['fsdc','solu','gto','e&u','cme']}

pldf = pd.DataFrame(p_and_l)
budf = pd.DataFrame(bu)

merge_df = pldf.merge(budf, left_on='bu_id', right_on='bu_id', how='inner')
merge_df['gross_margin'] = (merge_df['revenue'] - merge_df['cost'])/merge_df['revenue'] 
print(merge_df)

merge_df['month'] = merge_df['month'].str.upper()
merge_df.plot(x='month',y=['cost','revenue'],kind='bar', xlabel='Months', ylabel='USD',title='Monthwise P&L', stacked=True)
plt.show()
merge_df.plot(x='month',y=['cost','revenue'],kind='area', xlabel='Months', ylabel='USD',title='Monthwise P&L', stacked=False)
plt.show()

fig, pandl = plt.subplots()
pandl.plot(merge_df['month'],merge_df['revenue'],marker='o',color='green')
pandl.plot(merge_df['month'],merge_df['cost'],marker='d',color='blue')
pandl.set_xlabel("Month")
pandl.set_ylabel("USD")

gm = pandl.twinx()
gm.plot(merge_df['month'],merge_df['gross_margin'],marker='o',color='red')
gm.set_ylabel("Gross Margin")
plt.savefig('d:/pythondata/pandl.png')
plt.show()