from pymysql import connect, connections
from dbConfig import getConnection


def insertInvoice(dateInvoice, idCustomer, price, balance):
    connection = getConnection()
    with connection.cursor() as cursor:
        cursor.execute('insert into invoice(dateInvoice, idCustomer, price, balance) values (%s, %s, %s, %s)',
        (dateInvoice, idCustomer, price, balance))
    connection.commit()
    connection.close()

def getInvoices():
    connection = getConnection()
    with connection.cursor() as cursor:
        cursor.execute('select number, dateInvoice, idCustomer, price, balance from invoice')
        invoices = cursor.fetchall()
    connection.close()
    return invoices

def getOneInvoice(number):
    connection = getConnection()
    with connection.cursor() as cursor:
        cursor.execute('select number, dateInvoice, idCustomer, price, balance from invoice where number=%s', (number))
        invoice = cursor.fetchone()
    connection.close()
    return invoice

def getInvoiceByCustomer(idCustomer):
    connection = getConnection()
    with connection.cursor() as cursor:
        cursor.execute('select number, dateInvoice, idCustomer, price, balance from invoice where idCustomer=%s', (idCustomer))
        invoice = cursor.fetchall()
    connection.close()
    return invoice

def updateInvoice(dateInvoice, idCustomer, price, balance, number):
    connection = getConnection()
    with connection.cursor() as cursor:
        cursor.execute('update invoice set dateInvoice=%s, idCustomer=%s, price=%s, balance=%s where number=%s', (dateInvoice, idCustomer, price, balance, number))
    connection.commit()
    connection.close()

def deleteInvoice(number):
    connection = getConnection()
    with connection.cursor() as cursor:
        cursor.execute('delete from invoice where number=%s', (number))
    connection.commit()
    connection.close()
