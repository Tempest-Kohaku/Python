import mysql.connector 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="",
    database="mydatabase"
)
mycursor = mydb.cursor()
sql = "UPDATE customers SET address = 'Canyon 123' where name = 'Jhonson'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"records affected")