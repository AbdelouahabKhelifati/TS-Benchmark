import pandas as pd
import numpy as np
from tqdm import tqdm

data = pd.read_csv("../data/GoldwindSensor.csv", header=None)
data.head(3072 * 2)

res_overlapped_1 = pd.DataFrame()
res_overlapped_10 = pd.DataFrame()

for i in tqdm(range(3072)):
    res_overlapped_1[i] = np.array(list(data[23])[i:i + 3072])
    res_overlapped_10[i] = np.array(list(data[23])[10 * i:(10 * i) + 3072])

res_overlapped_1.to_csv('column_23_3072_3072_overalpped_1.txt', sep=',', encoding='utf-8', header=None, index=None)
res_overlapped_10.to_csv('column_23_3072_3072_separaate_10.txt', sep=',', encoding='utf-8', header=None, index=None)
