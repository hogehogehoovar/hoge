# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.cluster import KMeans
import pymysql.cursors

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
np_data = np.array(data, dtype=np.int32)

 # MySQL接続
connection = pymysql.connect(user='sonoda', password='sonoda', host='localhost', database='webEng')

# カーソル取得
cursor = connection.cursor()

for np_data_t in np_data:
    data_t=[]
    for d in np_data_t:
        data_t.append(int(d))

    # SQLクエリ実行（データ追加）
    sql = 'INSERT INTO users(Channel,Region,Fresh,Milk,Grocery,Frozen,DetergentsPaper,Delicassen) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql,data_t)
    # autocommitではないので、明示的にコミットする
    connection.commit()
cursor.close
#mysql切断
connection.close

