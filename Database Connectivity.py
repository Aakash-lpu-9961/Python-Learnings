import mysql.connector

conn = mysql.connector.connect(host="localhost", password="@Aakash9961", user="root")

if conn.is_connected():
    print("Connection Established")
