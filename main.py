import pandas as pd

df = pd.read_csv('dataset.csv')
df.info()
df.isnull().num()
