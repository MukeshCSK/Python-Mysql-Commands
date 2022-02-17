import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "1234", database = "mydatabase")
mycursor = mydb.cursor()
mycursor.execute("select name from customers ")
myresult = mycursor.fetchone()
for x in myresult:
        pass
print (x)
