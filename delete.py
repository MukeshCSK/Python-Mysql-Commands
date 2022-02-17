import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "1234", database = "mydatabase")
mycursor = mydb.cursor()
sql = ("delete from customers where address = 'Mountain 21'")
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) deleted")
