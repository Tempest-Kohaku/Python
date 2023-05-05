import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Practice_Test"
)
mycursor = mydb.cursor()
mycursor.execute("Insert Into Customers Values('Hirasaki','Highway 27',13400)")
mydb.commit()
print(mycursor.rowcount,"row(s) updated")