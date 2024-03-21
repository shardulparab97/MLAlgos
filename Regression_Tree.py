import pandas as pd
import numpy as np

dataset= pd.read_csv("data/day.csv",
usecols=['season', 'holiday', 'weekday', 'workingday', 'weathersit','cnt']).sample(frac=1)

print(dataset.head)

default_output = np.mean(dataset['cnt'])
mean_data = np.mean(dataset.iloc[:, -1])

