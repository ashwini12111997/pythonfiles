import pandas as pd

df = pd.read_csv('panda.csv')

grouped = df.groupby('city').size().reset_index(name='hyd')
grouped['activate'] = 'active'
grouped.to_csv('add_col.csv', index=False)

