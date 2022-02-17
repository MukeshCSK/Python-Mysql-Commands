import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "1234", database = "mydatabase")
mycursor = mydb.cursor()
mycursor.execute("create table customers (name varchar(255), address varchar(255))")
