# import the python pandas package
import pandas as pd
# create a sample dataframe
data = pd.DataFrame({"cars": ["bmw", "bmw", "benz", "benz"],
					"sale_q1 in Cr": [20, 22, 24, 26],
					'sale_q2 in Cr': [11, 13, 15, 17]},
					columns=["cars", "sale_q1 in Cr",
							'sale_q2 in Cr'])
print(data)
# stack the data using stack() function
stacked_data = data.stack()
print('Stacked Data')
print(stacked_data)

print('Level 0 unstacked data')
# unstack the dataframe by first level
stack_level_1 = stacked_data.unstack(level=0)
print(stack_level_1)

print('Level 1 unstacked data')
# unstack the dataframe by second level
stack_level_2 = stacked_data.unstack(level=1)
print(stack_level_2)

