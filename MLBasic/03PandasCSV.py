import numpy as np
import pandas as pd

df = pd.read_csv('Test.csv', header=None)
print(df)

xx = df[2]

xx.to_csv('TestWrite.csv')