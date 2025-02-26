import pandas as pd
import numpy as np

df = pd.read_csv('waze_dataset.csv')

# Summary information

df.head(10)
df.info()

# Seeing rows that have null values in column 'label'

null_df = df.loc[df.isnull().any(axis=1)]
null_df.describe()

not_null_df = df.loc[~df.isnull().any(axis=1)]
not_null_df.describe()
