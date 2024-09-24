import pandas as pd

file = pd.read_csv("example.csv")
n, m = map(int, input().split())
print(file)
print(file.iloc[n, m])