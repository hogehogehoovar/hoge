# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.cluster import KMeans
import pymysql.cursors
import sys
from functools import reduce
from datetime import datetime

#引数
argvs = sys.argv
eventId=argvs[1]
userId=argvs[2]

#イベントに参加しているユーザー
#userList=[]
#グループとユーザの対応
group_users={}
#ユーザの情報
userDic={}

#新しいグループを量産するフェーズかどうか
isCreateFase=False
#新しいグループを量産するフェーズの人数の閾値
PARTICIPANTNUM=15
#最大のコサイン類似度
maxcos=0



def sql():
    # MySQL接続
    connection = pymysql.connect(user='sonoda', password='sonoda', host='localhost', database='webEng')

    # カーソル取得
    cursor = connection.cursor()

    # Select結果を取り出す
    sql_user = 'select  user_id from event_users where event_id=%s'
    cursor.execute(sql_user,eventId)
    results = cursor.fetchall()
    global userList
    userList = [x[0] for x in results]
    print('user')
    print(userList)

    sql_userInfo = 'select gender,birthday,job,university from users where id=%s'
    global userDic
    userDic = {user: getCursor(cursor,sql_userInfo,user) for user in userList}
    print(userDic)

    sql_group_user = 'select group_id,user_id from group_users '
    cursor.execute(sql_group_user)
    results = cursor.fetchall()
    global group_users

    group_users={k: {} for k, v in results}
    print( "@@@")
    {k: group_users[k].update({v:userDic[v]}) for k, v in results}
    #group_users={k: [] for k, v in results}
    #{k: group_users[k].append(v) for k, v in results}
    print(group_users)


    #cursor切断
    cursor.close

def getCursor(cursor,sql,key):
    cursor.execute(sql,key)
    results = cursor.fetchall()
    return results[0]

def getFase():
    global isCreateFase
    if len(userList)<PARTICIPANTNUM:
        isCreateFase=True

def getGroup():
    group1=[k for k,v in group_users.items() if len(v)==1]
    print(group1)
    #未完成のグループ(8人未満)
    group = {k:v for k,v in group_users.items() if len(v)<8 and len(v)>0}
    print( group)

    if not len(group1)==0:
        insert(group1)
    else:
        #cos_simの計算
        cosDic={k:[]  for k, v in group.items()}
        {k: group[k].append(v) for k, v in group.items()}
        #if isCreateFase:



def insert(groupId):
    with pymysql.connect(user='sonoda', password='sonoda', host='localhost', database='webEng') as cur:
        now = datetime.today()
        str_now = now.isoformat()
        cur.execute("INSERT INTO group_users (user_id,group_id,attendance,created_at,updated_at) VALUES (%s,%s,%s,%s,%s)", (int(userId),int(groupId),0,str_now,str_now))



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

