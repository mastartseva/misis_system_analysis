import numpy as np
import pandas as pd
import math

def task3(path:str):
    matrix=pd.read_csv(path, header=None)
    entropy=0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]!=0:
                entropy+=(matrix[i][j]/(len(matrix)-1)*math.log2(matrix[i][j]/(len(matrix)-1)))
    return(-entropy)