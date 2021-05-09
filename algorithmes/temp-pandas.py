import pandas as pd
import matplotlib.pyplot as plt
'''
print('-' * 20)
print('Series([5, 6, 7, 8, 9, 10])')
my_series = pd.Series([5, 6, 7, 8, 9, 10])
print(my_series[0:])
'''
print('-' * 20)
print("Series({'a': 5, 'b': 6, 'c': 7, 'd': 8})")
my_series3 = pd.Series({'a': 5, 'b': 6, 'c': 7, 'd': 8})
print(my_series3)


print('-' * 20)
print("DataFrame({'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'], 'population': [17.04, 143.5, 9.5, 45.5],'square': [2724902, 17125191, 207600, 603628]}, index=['KZ', 'RU', 'BY', 'UA'])")


df = pd.DataFrame({'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'], 
'population': [17.04, 143.5, 9.5, 45.5],
'square': [2724902, 17125191, 207600, 603628]}, 
index=['KZ', 'RU', 'BY', 'UA'])
df.index.name = 'ZIP'
print (df)

'''
print('-' * 20)
df.plot()
plt.show()



print('-' * 20)

'''