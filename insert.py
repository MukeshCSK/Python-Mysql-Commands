import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "1234", database = "mydatabase")
mycursor = mydb.cursor()
sql = ("insert into customers values (%s, %s)")
val = ("John", "Highway 21")
mycursor.execute(sql, val)
print(mycursor.rowcount,"record inserted.")
