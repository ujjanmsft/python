import pandas as pd

s = pd.Series([42, 21, 7, 3.5])
print(s)

fruits = pd.Series(['apple', 'banana', 'cherry'])
print(fruits)

df = pd.DataFrame({'age': [18, 19, 20],
                   'name': ['Alice', 'Bob', 'Carl'],
                   'cardio': [60, 70, 80]
})
df.loc[:, 'friend'] = 'Alice'
print(df)