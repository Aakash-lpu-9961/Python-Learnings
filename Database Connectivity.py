import mysql.connector as c

conn = c.connect(host="localhost",
                 password="@Aakash9961",
                 user='root',
                 database="aakashdb")

cursor = conn.cursor()
cursor.execute("select * from student")
data = cursor.fetchall()
print(data)

# if conn.is_connected():
#     print("Connection Established")
