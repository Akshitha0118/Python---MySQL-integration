import mysql.connector

conn =mysql.connector.connect(host='localhost',user='root',password='12345',database='pythondb')

mycursor=conn.cursor()
mycursor.execute('create table student(name varchar(50),branch varchar(20), id int)')
mycursor.execute('show tables')

for x in mycursor:
    print(x)