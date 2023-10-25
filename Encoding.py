import pandas as pd
state_list = ['tn','ka','kl','ts','ap','ka','kl','tn','tn','ka']
city_list = ['virudhunagar','bangalore','cochin','hyderabad','vizag','mysore','calicut','madurai','madurai','hubli']
zone_list = ['south','se','south','central','east','se','east','south','south','central']

dict1 = {'state_code': {'tn':22, 'ka':8, 'kl':9, 'ts':23, 'ap':1},
         'city_code': {'virudhunagar':626001,'bangalore':560001,'cochin':650001,'hyderabad':500001,'vizag':421001,'mysore':570001,'calicut':655001,'madurai':625001,'hubli':550001},
         'zone_code':{'south':1, 'se':2, 'central':3, 'east':4}
         }

merged_list = list(zip(city_list, state_list, zone_list))
print(merged_list)
df1 = pd.DataFrame(merged_list, columns=['city_code','state_code','zone_code'])
print(df1)
df2 = df1.replace(dict1)
print(df2)