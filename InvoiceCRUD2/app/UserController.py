from pymysql import connect, connections
from dbConfig import getConnection

#? Posibles cambios

def register(name, email, password, photo):
    connection = getConnection()
    with connection.cursor() as cursor:
        cursor.execute('insert into user(name, email, password, photo) values (%s, %s, %s, %s)', (name, email, password, photo))
    connection.commit()
    connection.close()


def login(email):
    connection = getConnection()
    with connection.cursor() as cursor:
        cursor.execute('select name from user where email=%s', (email))
        res = cursor.fetchone()
    connection.close()
    return res

def getEmails():
    connection = getConnection()
    with connection.cursor() as cursor:
        cursor.execute('select id, name, email, password, photo from user')
        res = cursor.fetchall()
    connection.close()
    return res