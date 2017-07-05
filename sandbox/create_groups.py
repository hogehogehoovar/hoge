# -*- coding: utf-8 -*-
def create( arg1, arg2 ):

    import numpy as np
    import pymysql.cursors
    import sys
    from datetime import datetime

    #引数
    argvs = sys.argv
    eventId=arg1
    userId=arg2

    #イベントに参加しているユーザー
    #userList=[]
    #参加中のユーザの情報辞書
    userDic={}
    #groupsテーブルのid
    group=[]
    #グループとユーザの対応
    group_users={}

    #新しいグループを量産するフェーズかどうか
    isCreateFase=False
    #新しいグループを量産するフェーズの人数の閾値
    PARTICIPANTNUM=15
    #現在時刻
    now = datetime.today()


    def sql():
        # MySQL接続
        connection = pymysql.connect(user='root',
                                     password='',
                                     host='localhost',
                                     database='uchiage_development')

        # カーソル取得
        cursor = connection.cursor()

        # イベントに参加しているユーザーリスト
        sql_user = 'select  user_id from event_users where event_id=%s'
        cursor.execute(sql_user,eventId)
        results = cursor.fetchall()
        global userList
        userList = [x[0] for x in results]

        #参加中のユーザの情報辞書
        sql_userInfo = 'select gender,birthday,job,university from users where id=%s'
        global userDic
        userDic = {user: getCursor(cursor,sql_userInfo,user) for user in userList}
        #userDicをcos_sim計算しやすいように正規化
        userDic={k:(v[0],(now.year-v[1].year)/80,ord(v[2])/65535,ord(v[3])/65535) for k,v in userDic.items()}

        sql_group = 'select id from groups '
        cursor.execute(sql_group)
        results = cursor.fetchall()
        global group
        group=[x[0] for x in results]

        #グループとユーザの対応
        sql_group_user = 'select group_id,user_id from group_users '
        cursor.execute(sql_group_user)
        results = cursor.fetchall()
        global group_users
        group_users={k: {} for k, v in results}
        {k: group_users[k].update({v:userDic[v]}) for k, v in results}

        #cursor切断
        cursor.close

    def getCursor(cursor,sql,key):
        cursor.execute(sql,key)
        results = cursor.fetchall()
        return results[0]

    #新しいグループ作るかどうか->参加人数が閾値以下だと作成
    def getFase():
        global isCreateFase
        if len(userList)<PARTICIPANTNUM:
            isCreateFase=True

    def getGroup():
        group1=[k for k,v in group_users.items() if len(v)==1]
        group2=[k for k,v in group_users.items() if len(v)==2]
        #未完成のグループ(8人未満)
        group = {k:v for k,v in group_users.items() if len(v)<8 and len(v)>0}

        #未完成のグループ０個なら新しくグループ作る
        if len(group)==0:
            createGroup()
        #1人のグループあるならとりあえずそこに入れる
        elif not len(group1)==0:
            insert(group1[0])
        #それ以外
        else:
            #cos類似度計算
            cosDic={k:{ }  for k, v in group.items()}
            {k: cosDic[k].update({k2:cos_sim(userDic[int(userId)],v2)}) for k, v in group.items() for k2,v2 in v.items()}
            cosAve={k:np.average(list(v.values())) for k,v in cosDic.items() }
            #cos類似度の大きいグループに入れる
            maxCos=max([(v,k) for k,v in cosAve.items()])[0]
            maxGroup=max([(v,k) for k,v in cosAve.items()])[1]
            if isCreateFase:
                #cos類似度が十分に大きくなければ新しいグループ作るー＞グループ多いほど、作られにくい、2人のグループあるなら作られにくい
                if maxCos <0.8/(len(group)+len(group2)):
                    createGroup()
                else:
                    insert(maxGroup)
            else:
                #if maxCos <0.5/(len(group)+len(group2)):
                if maxCos <1/(len(group)+len(group2)):
                    createGroup()
                else:
                    insert(maxGroup)


    def insert(groupId):
        with pymysql.connect(user='sonoda', password='sonoda', host='localhost', database='webEng') as cur:
            str_now = now.isoformat()
            cur.execute("INSERT INTO group_users (user_id,group_id,attendance,created_at,updated_at) VALUES (%s,%s,%s,%s,%s)", (int(userId),int(groupId),0,str_now,str_now))

    def createGroup():
        if len(group)==0:
            maxGroupId=0
        else:
            maxGroupId=max([x for x in group])
        with pymysql.connect(user='sonoda', password='sonoda', host='localhost', database='webEng') as cur:
            str_now = now.isoformat()
            cur.execute("INSERT INTO groups (id,event_id,restaurant_id,created_at,updated_at) VALUES (%s,%s,%s,%s,%s)", (int(maxGroupId)+1,int(eventId),2,str_now,str_now))
            cur.execute("INSERT INTO group_users (user_id,group_id,attendance,created_at,updated_at) VALUES (%s,%s,%s,%s,%s)", (int(userId),int(maxGroupId)+1,0,str_now,str_now))


    def closeSql():
        connection = pymysql.connect(user='root',
                                     password='',
                                     host='localhost',
                                     database='uchiage_development')
        #mysql切断
        connection.close

    def cos_sim(v1, v2):
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

    if __name__ == '__main__':
        sql()
        getFase()
        getGroup()
        closeSql()

