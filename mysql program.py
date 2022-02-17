import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "1234", database = "ex")
my = mydb.cursor()
my.execute("select * from student")
res = my.fetchone()
for i in res:
    print(i)
