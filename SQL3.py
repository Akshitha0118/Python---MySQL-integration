import mysql.connector
conn =mysql.connector.connect(host='localhost',user='root',password='12345',database='pythondb')

mycursor = conn.cursor()

sql = 'insert into student (name,branch,id) values(%s,%s,%s)'

val = [('john','cse','56'),('mike','IT','78'),('tyson','me','80')]

mycursor.executemany(sql,val)
conn.commit()
print(mycursor.rowcount,'record inserted')
