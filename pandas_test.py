import pandas
from pandas import Series, DataFrame

# obj = Series([1, 4, 6, -7])
# print(obj)
# print(obj.index)
# print(obj.values)
#
# print(type({'a'}))

# obj2 = Series([1, 3, 5, 7], index=['d', 'b', 'c', 'a'])
# print(obj2)
# obj2['d'] = 999
# print(obj2)
# print('a' in obj2)
# print('e' in obj2)

# dict = {'beijing': 3000, 'shanghai': 2000, 'guangzhou': 100, 'shenzhen': 500}
# obj3 = Series(dict)
# print(obj3)
# obj3.index = ['bj', 'sh', 'gz', 'sz']
# print(obj3)

# data = {'city': ['shanghai', 'shanghai', 'beijing', 'shenzhen'],
#         'year': [2018, 2011, 2012, 2013],
#         'pop': [2.3, 1.9, 2.7, 1.9]}
# frame = DataFrame(data)
# print(frame)

# frame2 = DataFrame(data, columns=['year', 'city', 'pop'])
# print(frame2)
#
# print(frame.year)
# print(frame['city'])

# frame['new'] = 100
# frame['cap'] = frame['city'] == 'beijing'
# print(frame)


# data = {'beijing': {2008: 1.3, 2009:1.4},
#         'shanghai': {2008: 1.2, 2009: 1.5}}
# frame = DataFrame(data)
# print(frame)
# print(frame.T)

# obj4 = Series([1, 3, -9], index=['b', 'c', 'd'])
# obj5 = obj4.reindex(['a', 'b', 'c', 'd'], fill_value=0)
# print(obj5)
#
# obj6 = Series(['blue', 'purple', 'yellow'], index=[1, 2, 4])
# obj7 = obj6.reindex(range(6), method='ffill')
# print(obj7)

from numpy import nan as NA
import numpy as np

# data = Series([1, NA, 3])
# print(data)
# print(data.dropna())

# data2 = DataFrame([[1, 3, 9], [2, NA, NA], [NA, NA, NA]])
# print(data2)
#
# # print(data2.dropna(how='all'))
# data2[4] = NA
# print(data2)
# print(data2.dropna(axis=1, how='all'))

data3 = Series(np.random.randn(10), index=[['a', 'a', 'a', 'b', 'b', 'c', 'd', 'd', 'e', 'f'],
                                           [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]])
print(data3)

print(data3.unstack().stack())