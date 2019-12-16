import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pwd283841",
)
print(mydb)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE employees")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)
