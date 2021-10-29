from logging import fatal
from flask.scaffold import F
from werkzeug.utils import import_string
import CustomerController
import InvoiceController

DBC = CustomerController
DBI = InvoiceController

def deletingCustomer(idCustomer):
    data = DBI.getInvoiceByCustomer(idCustomer)
    if  not len(data) > 0:
        return True
    else:
        return False

def deletingInvoice(number):
    data = DBI.getOneInvoice(number)
    balance= data[4]
    Balance = int(balance)
    if Balance == 0:
        return True
    else:
        return False

def addingInvoice(idCustomer):

    IDCustomer = int(idCustomer)
    listIds = []
    data = DBC.getCustomerIds()

    for i in range(len(data)):
        listIds.append(data[i][0]) 
    newListIds = tuple(listIds)

    if IDCustomer in newListIds:
        return True
    else:
        return False

