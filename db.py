import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pwd283841",
    database="employees"
)
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE employees (employee_id INTEGER(10),name VARCHAR(255),surname VARCHAR(255),"
#                  "email VARCHAR(255),phone_number INTEGER(10), salary VARCHAR(255), job_id VARCHAR(255), department_id VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
# for db in mycursor:
#     print(db)

mycursor = mydb.cursor()
sqlFormula = "INSERT INTO employees (employee_id, name, surname, email, phone_number, salary, job_id, department_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
employee = [(1, "Zachery", "Ziolkowski", "zziolkowski@iwork.com", 555101234, "12.000$", "accounting", 30),
            (2, "Hilde", "Hollenbeck", "hhollenbeck@iwork.com", 555101235, "12.000$", "accounting", 30),
            (3, "Traci",  "Tobia", "ttobia@iwork.com", 555101236, "12.000$", "accounting", 30),
            (4, "Luigi", "Lineman", "llineman@iwork.com", 555101237, "13.000$", "advertising", 40),
            (5, "Denny","Deacon", "ddeacon@iwork.com", 556111234, "13.000$", "advertising", 40),
            (6, "Loise" ,"Levert", "llevert@iwork.com", 556111235, "13.000$", "advertising", 40),
            (7, "Felisha" ,"Fellers","ffellers@iwork.com", 556111236, "15.000$", "management", 10),
            (8, "Stefan", "Sebring", "ssebring@iwork.com", 553121236, "15.000$", "management", 10),
            (9, "Jodie", "Jarmon", "jjarmon@iwork.com", 553121237, "13.000$", "IT", 20),
            (10, "Wilson", "Watley","wwatley@iwork.com", 553121238, "13.000$", "IT", 20),]
mycursor.executemany(sqlFormula, employee)
mydb.commit()


