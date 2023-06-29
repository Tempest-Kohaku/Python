# Create a New Database and then Create Two Tables INTERNSHIP and EMPLOYEE and Join these two tables

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE Project1")
cursor.execute("USE Project1")

# Create the INTERNSHIP table
cursor.execute('''CREATE TABLE INTERNSHIP (
                    intern_id INT PRIMARY KEY,
                    intern_name VARCHAR(50),
                    start_date DATE,
                    end_date DATE,
                    supervisor VARCHAR(50)
                )''')

# Create the EMPLOYEE table
cursor.execute('''CREATE TABLE EMPLOYEE (
                    empid INT PRIMARY KEY AUTO_INCREMENT,
                    empname VARCHAR(50),
                    department VARCHAR(50),
                    salary DECIMAL(10,2),
                    address VARCHAR(50),
                    email VARCHAR(50)
                )''')

# Query to Join two tables
query = '''
    SELECT INTERNSHIP.id, INTERNSHIP.intern_name, EMPLOYEE.empname
    FROM INTERNSHIP
    INNER JOIN EMPLOYEE ON INTERNSHIP.supervisor = EMPLOYEE.empname
'''

cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)
cursor.close()
mydb.close()
