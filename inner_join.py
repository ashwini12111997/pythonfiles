# importing pandas
import pandas as pd

# Creating dataframe a
a = pd.DataFrame()

# Creating Dictionary
d = {'id': [1, 2, 10, 12],
	'val1': ['a', 'b', 'c', 'd']}

a = pd.DataFrame(d)

# Creating dataframe b
b = pd.DataFrame()

# Creating dictionary
d = {'id': [1, 2, 9, 8],
	'val1': ['p', 'q', 'r', 's']}
b = pd.DataFrame(d)

# inner join
df = pd.merge(a, b, on='id', how='inner')

# left outer join
ldf = pd.merge(a, b, on='id', how='left')

# right outer join
rdf = pd.merge(a, b, on='id', how='right')

# full outer join
odf = pd.merge(a, b, on='id', how='outer')

# display dataframe
print("inner join",df)
print("left outer join",ldf)
print("right outer join",rdf)
print("full outer join",odf)
