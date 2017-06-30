# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.cluster import KMeans
import pymysql.cursors
import sys
from functools import reduce

#引数
argvs = sys.argv
eventId=argvs[1]
userId=argvs[2]

#参加人数
participants=0
#グループ数
group_num=0
#グループ
group=[]
#グループごとの人数
group_participants=[]
#1人のみのグループ数
group1_num=0
#2人のみのグループ数
group2_num=0
#新しいグループを量産するフェーズかどうか
isCreateFase=False
#新しいグループを量産するフェーズの人数の閾値
PARTICIPANTNUM=15
#コサイン類似度のリスト
cosList=[ ]
#最大のコサイン類似度
maxcos=0



def sql():
    # MySQL接続
    connection = pymysql.connect(user='sonoda', password='sonoda', host='localhost', database='webEng')

    # カーソル取得
    cursor = connection.cursor()

    # Select結果を取り出す
    sql = 'select gender,birthday,job,university from users where id=%s'
    cursor.execute(sql,userId)
    results = cursor.fetchall()
    print(results)
    sql_num = 'select count( user_id) from event_users where event_id=%s'
    cursor.execute(sql_num,eventId)
    results = cursor.fetchall()
    global participants
    participants = int(results[0][0])
    sql_groupnum = 'select count( event_id) from groups where event_id=%s'
    cursor.execute(sql_groupnum,eventId)
    results = cursor.fetchall()
    global group_num
    group_num = int(results[0][0])
    print("group_num")
    print(type(group_num))
    print(group_num)
    sql_group = 'select user_id,group_id from group_users '
    cursor.execute(sql_group)
    results = cursor.fetchall()
    global group
    group=results
    #cursor切断
    cursor.close

def getGroup():
    global group_participants
    global group1_num
    global group2_num

    for i in range(group_num):
        group_participants.append(len([x for x in group if x[1] ==i+1]))
        if group_participants[i]==1:
            group1_num+=1
        if group_participants[i]==2:
            group2_num+=1

def getFase():
    global isCreateFase
    if participants<PARTICIPANTNUM:
        isCreateFase=True




    '''
    # K-means クラスタリングをおこなう
    kmeans_model = KMeans(n_clusters=3, random_state=10).fit_predict(results)
    print( kmeans_model)
    '''
def closeSql():
    connection = pymysql.connect(user='sonoda', password='sonoda', host='localhost', database='webEng')
    #mysql切断
    connection.close

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

if __name__ == '__main__':
    x = np.array([1, 1, 1, 1, 1])
    y = np.array([1, 0, 1, 0, 1])
    z = np.array([0, 1, 0, 0, 0])
    sql()

    getGroup()
    getFase()

    closeSql()
    
    print(cos_sim(x, y))
    print(cos_sim(y, z))
    print(cos_sim(z, x))

