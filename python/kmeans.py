# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.cluster import KMeans

#データの読み込み
data = []
f = open('./Wholesale_customers_data.csv', 'r')
dataReader = csv.reader(f)
count = 0
#ヘッダ行読まない
for row in dataReader:
    data_t = []
    count += 1
    if count == 1:
        continue
    for ele in row:
        data_t.append(float(ele))
    data.append(data_t)

f.close()
#numpyのarrayに変換
np_data = np.array(data, dtype=np.float32)
print(np_data)

# K-means クラスタリングをおこなう
# この例では 3 つのグループに分割 (メルセンヌツイスターの乱数の種を 10 とする)
kmeans_model = KMeans(n_clusters=3, random_state=10).fit_predict(np_data)
print( kmeans_model)
print( type( kmeans_model))
np_kmeans = np.array(kmeans_model, dtype=np.float32)

np_data_c=np.c_[ np_data,np_kmeans]
print( np_data_c[ np_data_c[:,8]==0].mean( axis=0))

