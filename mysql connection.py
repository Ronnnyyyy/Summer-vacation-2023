
#. importing a connector for python and mysql (mysql.connector.python)
 import mysql.connector as connector

#. connecting python to database
 con=connector.connect(host='localhost',
     port='3306',
     user='root',
     password='rohitonmysql',
     database='testdb'    #- name of database to be managed
 )

#.making a cursor
 mycursor=con.cursor()

#. making a database
mycursor.execute('CREATE DATABASE {name}')


#. showing a database
mycursor.execute('SHOW DATABASES')
for db in mycursor:
    print(db)

#. Creating a table in a particular database

mycursor.execute('CREATE TABLE Students(name VARCHAR(25), age INTEGER(3), gender VARCHAR(10))')

#. Showing the tables in a particular database

 mycursor.execute('SHOW TABLES')
 for tb in mycursor:
     print(tb)

#. Entering multiple data using executmany

 sqlFormula = "INSERT INTO students (name, age, gender) VALUES (%s,%s,%s)"
 students= [
     ('Rahul', 48,'male'),
     ("Rohan", 39,'male'),
     ("Ankita", 7,"female"),
     ("Amit", 20,"male"),
     ("Mahesh",18,"male")
 ]
#. Executing the insertion
 mycursor.executemany(sqlFormula,students)

#. Commiting the execution
 con.commit()
