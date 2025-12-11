import mysql.connector

conn =mysql.connector.connect(host='localhost',user='root',password='12345')

if conn.is_connected():
    print('yes connet')
    
mycursor=conn.cursor()
mycursor.execute('show databases')
print(mycursor)