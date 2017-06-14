# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.cluster import KMeans
import pymysql.cursors


 # MySQL接続
connection = pymysql.connect(user='sonoda', password='sonoda', host='localhost', database='webEng')

# カーソル取得
cursor = connection.cursor()

# Select結果を取り出す
sql = 'select Channel,Region,Fresh,Milk,Grocery,Frozen,DetergentsPaper,Delicassen from users'
cursor.execute(sql)

results = cursor.fetchall()
# K-means クラスタリングをおこなう
kmeans_model = KMeans(n_clusters=3, random_state=10).fit_predict(results)
print( kmeans_model)

#cursor切断
cursor.close
#mysql切断
connection.close


np_kmeans = np.array(kmeans_model, dtype=np.float32)
np_results = np.array(results, dtype=np.float32)
np_data_c=np.c_[ np_results,np_kmeans]
print( np_data_c[ np_data_c[:,8]==0].mean( axis=0))
