import pandas as pd
data = pd.read_csv(r"dataset.csv")
df = data.groupby(['urlProfile'])['numberPosts'].mean()
df.reset_index(drop = False, inplace = False)
print(df['urlProfile'])
