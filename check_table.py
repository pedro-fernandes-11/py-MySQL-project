import pymysql as sql

connection = sql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='formdb'
)

cursor = connection.cursor()

cursor.execute('SELECT * FROM tb_form')
tb_form = cursor.fetchall()

for each in tb_form:
    print(each)
