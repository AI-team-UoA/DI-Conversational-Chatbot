import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="root"
)

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE DiBot")