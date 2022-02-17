import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "1234", database = "mydatabase")
mycursor = mydb.cursor()
sql = ("update customers set address = 'Canyon 1324'")
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) affected")
