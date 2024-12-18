import pandas as pd

def task(file1:str,n,m):
    file = pd.read_csv(file1)
    n, m = map(int, input().split())
    return(file.iloc[n, m])