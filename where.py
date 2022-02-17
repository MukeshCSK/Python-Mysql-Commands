import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "1234", database = "mydatabase")
mycursor = mydb.cursor()
sql = ("select * from customers where address = 'Highway 21'")
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
