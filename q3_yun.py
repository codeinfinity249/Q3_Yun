# -*- coding: utf-8 -*-
"""Q3_Yun.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RCSbmqVXrZOn0XGtGaSvVhp40vFr59Lj
"""

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN

# Create a sample dataframe with x and y coordinates
data = {
    'x': [0.1, 0.4, 0.9, 1.2, 1.5, 2.0, 2.1],
    'y': [0.1, 0.5, 0.9, 1.1, 1.6, 2.1, 2.0]
}
df = pd.DataFrame(data)


coords = df[['x', 'y']].values

dbscan = DBSCAN(eps=0.5, min_samples=1, metric='euclidean')
clusters = dbscan.fit_predict(coords)

df['group'] = clusters

print(df)

