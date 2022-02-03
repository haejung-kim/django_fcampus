# select

import sqlite3
conn = sqlite3.connect('test.db')
cur = conn.cursor()
SQL = "select * from item LIMIT 2;"
cur.execute(SQL)
# selec는 실행하면 해당 값이 cur에 대기함 # fetchall로 값을 가져오기
# list(tuple)반환함


while (True):
    row = cur.fetchone()
    print(type(row))
    if not row:
        break
    print(row)
    print(row[0])


# print(type(rows))
# rows = cur.fetchall()
# for row in rows:
#     print(row)
