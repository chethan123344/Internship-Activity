#importing panadas

import pandas as pd

s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

print(s1)
print(s2)


#indexing selection
marks = pd.Series([85, 90, 78], index=['Math', 'Physics', 'Chemistry'])

print(marks['Math'])
print(marks[['Math', 'Chemistry']])


#boolean

scores = pd.Series([45, 67, 89, 34, 90])

passed = scores[scores > 60]
print(passed)

#handle miss data
data = pd.Series([10, None, 30, None])

print(data.isnull())
print(data.fillna(2))

#string operation

names = pd.Series(['Alice', 'bob', 'CHARLIE'])

print(names.str.lower())
print(names.str.contains('A'))
print(names.str.upper())









