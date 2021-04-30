import pandas as pd
import numpy as np
from tqdm import tqdm

data = pd.read_csv("../data/GoldwindSensor.csv", header=None)
data.head(3072*2)

res = pd.DataFrame()

for i in tqdm(range(3072)):
    res[i] = np.array(list(data[23])[i:i+3072])


res.to_csv('column_23_3072_3072.txt', sep=',', encoding='utf-8')

