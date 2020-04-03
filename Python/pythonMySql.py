# Author: Jean J Barros
# Github: https://github.com/jjeanjacques10/

# --- Conectando com o Mysql com Python ---

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

def insert():
    sql = "INSERT INTO usuario (name, contato) VALUES (%s, %s)"
    val = ("jjean_dev", "XXXXXXXX")
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def select():
    mycursor.execute("SELECT * FROM usuario")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def delete():
    sql = "DELETE FROM usuario WHERE name = 'jjean'"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")


def update():
    sql = "UPDATE usuario SET name = 'jean jacques barros' WHERE name = 'jjean_dev'"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")