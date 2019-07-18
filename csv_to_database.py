import sqlite3

con = sqlite3.connect('./shop_list.sqlite')
cur = con.cursor()
keyword = '渋谷駅'
smoking = '分煙'
sql = 'select shop_name, rate, rocation, comment, url from shop_list where rocation like {0} and smoking like {1}'.format('"%' + keyword +'%"', '"%' + smoking +'%"')
cur.execute(sql)

for row in cur.fetchall():
    print (row[0], row[1], row[2], row[3], row[4])

con.close()
