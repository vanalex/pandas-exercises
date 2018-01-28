import inline as inline
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('max_columns', 50)

# create a series with an arbitrary list
s = pd.Series([2, 'Alex', 3.1, -34234, 'Yeeha!'])
print(s)

# Alternatively, you can specify an index to use when creating the Series.
s = pd.Series([2, 'Alex', 3.1, -34234, 'Yeeha!'],
              index=['A', 'Z', 'C', 'Y', 'E'])
print('')
print(s)

# The Series constructor can convert a dictonary as well, using the keys of the dictionary as its index.
d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
     'Austin': 450, 'Boston': None}

cities = pd.Series(d)
print('')
print(cities)

# You can use the index to select specific items from the Series ...
print('')
print(cities['Chicago'])

print('')
print(cities[['Chicago', 'Portland', 'San Francisco']])

# using boolean as an index for selection
print('')
print(cities[cities < 1000])

print('')
less_than_1000 = cities < 1000
print(less_than_1000)
print('\n')
print(cities[less_than_1000])

print('')
# change value of a Series on the fly
print('Old Value:', cities['Chicago'])
cities['Chicago'] = 1400
print('New Value:', cities['Chicago'])

# Changing values using boolean logic

print('')
print(cities[cities < 1000])
print('\n')
cities[cities < 1000] = 750
print('')
print(cities[cities < 1000])

# What if you aren't sure whether an item is in the Series? You can check using idiomatic Python.

print('')
print('Seattle' in cities)
print('San Francisco' in cities)

# Mathematical operations can be done using scalars and functions.
print('')
print(cities / 3)

# square city values
print('')
print(np.square(cities))