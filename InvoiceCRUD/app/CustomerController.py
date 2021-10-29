from pymysql import connect, connections
from dbConfig import getConnection

def insertCustomer(name, status, mobile):
    connection = getConnection()
    with connection.cursor() as cursor:
        cursor.execute('insert into customer(name, status, mobile) values (%s, %s, %s)', (name, status, mobile))
    connection.commit()
    connection.close()

def getCustomers():
    connection = getConnection()
    with connection.cursor() as cursor:
        cursor.execute('select id, name, status, mobile from customer ')
        customers = cursor.fetchall()
    connection.close()
    return customers

def getOneCustomer(id):
    connection = getConnection()
    with connection.cursor() as cursor:
        cursor.execute('select id, name, status, mobile from customer where id=%s', (id))
        custom = cursor.fetchone()
    connection.close()
    return custom

def getCustomerIds():
    connection = getConnection()
    with connection.cursor() as cursor:
        cursor.execute('select id from customer')
        customerIds = cursor.fetchall()
    connection.close()
    return customerIds

def updateCustomer(name, status, mobile, id):
    connection = getConnection()
    with connection.cursor() as cursor:
        cursor.execute('update customer set name=%s, status=%s, mobile=%s where id=%s', (name, status, mobile, id))
    connection.commit()
    connection.close()

def deleteCustomer(id):
    connection = getConnection()
    with connection.cursor() as cursor:
        cursor.execute('delete from customer where id= %s', (id))
    connection.commit()
    connection.close()