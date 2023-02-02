import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_csv('C:\Users\andre\Downloads\datos.csv')
X = datos.iloc[:, :-1].values
y = datos.iloc[:, -1].values

datos.head()

print(X)