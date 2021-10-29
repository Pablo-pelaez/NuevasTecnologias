from pymysql import NULL, connect, connections
from configdb import getConnection


def insertUser(name, email, password):
    connection = getConnection()
    with connection.cursor() as cursor:
        cursor.execute('insert into user(name, email, password) values (%s, %s, %s)', 
        (name, email, password))
    connection.commit()
    connection.close()

def getUsers():
    connection = getConnection()
    users = []
    with connection.cursor() as cursor:
        cursor.execute("select id, name, email from user")
        users = cursor.fetchall()
    connection.close()
    return users

def getOneUser(id):
    connection = getConnection()
    user = None
    with connection.cursor() as cursor:
        cursor.execute("select id, name, email, from user where id=%s", (id))
        user = cursor.fetchone()
    connection.close()
    return user

def updateUser(name, email, password, id):
    connection = getConnection()
    with connection.cursor() as cursor:
        cursor.execute("update user set name= %s, email= %s, password= %s where id= %s",
        (name, email, password, id))
    connection.commit()
    connection.close()

def deleteUser(id):
    connection = getConnection()
    with connection.cursor() as cursor:
        # cursor.execute("delete from user where id= %s)", (id))
        cursor.execute("delete from user where id =" + id)
    connection.commit()
    connection.close()