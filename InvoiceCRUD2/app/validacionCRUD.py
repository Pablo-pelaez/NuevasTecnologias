from flask.scaffold import F
from werkzeug.utils import import_string
import CustomerController
import InvoiceController
import UserController

DBC = CustomerController
DBI = InvoiceController
DBU = UserController

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
    

def existEmail(email):
    data = DBU.getEmails()
    emailsList = []
    
    for i in range(len(data)):
        emailsList.append(data[i][2]) 
    newEmailsList = tuple(emailsList)

    if email in newEmailsList:
        return True
    else:
        return False
    
def verifyCredentials(email, password):
    data = DBU.getEmails()
    emailsList = []
    passwordList = []
    
    for i in range(len(data)):
        emailsList.append(data[i][2])
        passwordList.append(data[i][3])
    newEmailsList = tuple(emailsList)
    newPasswordList = tuple(passwordList)

    if email in newEmailsList and password in newPasswordList:
        return True
    else:
        return False

