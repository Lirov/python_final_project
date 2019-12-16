import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pwd283841",
    database="employees"
)
mycursor = mydb.cursor()
mycursor.execute ("SELECT * FROM employees")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

