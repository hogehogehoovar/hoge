import mysql.connector
import csv
import glob

def save_to_db():
    csvfile = glob.glob('*.csv')
    schedulefile = []
    for name in csvfile:
        if "schedule" in name:
            schedulefile.append(name)
    print("現在保持しているイベント情報")
    print(schedulefile)
    n_file = len(schedulefile)
    for i in range(n_file):
        save_file = schedulefile[i][8:-4]

    con = mysql.connector.connect(
            host='localhost',
            db='web_biz',
            user='root',
            #password='input your pass'
        )
    cursor = con.cursor()
    for i in range(n_file):
        save_file = schedulefile[i][8:-4]
        cursor.execute("DROP TABLE IF EXISTS "+save_file)
        cursor.execute("""CREATE TABLE IF NOT EXISTS """+save_file+"""(
            イベント名 TEXT,
            開始時間  DATETIME,
            終了時間 DATETIME,
            location_id TEXT)""")

        f = open("schedule"+save_file+".csv", "r")
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
          sql = "INSERT IGNORE INTO "+save_file+" values(%s,%s,%s,%s)"
          cursor.execute(sql, (row[1], row[2], row[3],row[4]))
        f.close()
    con.commit()
    con.close()
