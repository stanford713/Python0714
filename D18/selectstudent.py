import sqlite3

conn=sqlite3.connect('student.db')
cursor=conn.cursor()
print('序號','身高','體重 ','BMI','  姓名')
print('-----------------------------------')
sql='SELECT b.id, b.h, b.w, ROUND(b.w / ((b.h / 100)*(b.h / 100)), 2) AS bmi, s.name '\
    'FROM student as s, bmi as b '\
    'WHERE s.id = b.sid '\
    'ORDER BY h DESC' #由大到小

cursor.execute(sql)
rows=cursor.fetchall()








for row in rows:
    print(row[0],row[1],row[2],row[3],row[4])
