import pandas as pd

df = pd.read_json('panda.json')
filtered = df[df["age"] == 25][["name","age"]]
print(filtered) 