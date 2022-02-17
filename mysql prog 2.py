import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "1234", database = "ex")
my = mydb.cursor()
a = input('A : ')
b = input('B : ')
my.execute("insert into language values ("+a+","+b+")")

mydb.commit()
print('done')
