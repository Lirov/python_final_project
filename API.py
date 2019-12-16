import MySQLdb
import json

dbconn = MySQLdb.connect(
    host="localhost",
    user="root",
    password="Pwd283841",
    database="employees"
)
query = ("SELECT * FROM employees")

with dbconn.cursor(MySQLdb.cursors.DictCursor) as cursor:
    cursor.execute(query)
    data = cursor.fetchall()

print(json.dumps(data, indent=4))