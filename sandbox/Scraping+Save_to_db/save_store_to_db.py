import mysql.connector
import csv
import glob

def save_to_db():
    csvfile = glob.glob('*.csv')
    storefile = []
    for name in csvfile:
        if "store" in name:
            storefile.append(name)
    print("現在保持している店舗情報")
    print(storefile)
    n_file = len(storefile)
    for i in range(n_file):
        save_file = storefile[i][8:-4]

    con = mysql.connector.connect(
            host='localhost',
            db='web_biz',
            user='root',
            #password='input your pass'
        )
    cursor = con.cursor()
    for i in range(n_file):
        save_file = storefile[i][0:-4]
        cursor.execute("DROP TABLE IF EXISTS "+save_file)
        cursor.execute("""CREATE TABLE IF NOT EXISTS """+save_file+"""(
            ID TEXT,
            店舗名  TEXT,
            phone_number TEXT,
            address TEXT,
            shopimage_url TEXT,
            url TEXT,
            location_id TEXT)""")

        f = open(save_file+".csv", "r")
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
          sql = "INSERT IGNORE INTO "+save_file+" values(%s,%s,%s,%s,%s,%s,%s)"
          cursor.execute(sql, (row[1], row[2], row[3],row[4],row[5],row[6],row[7]))
        f.close()
    con.commit()
    con.close()
