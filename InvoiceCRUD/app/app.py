from flask import Flask, app, render_template, request, redirect
import CustomerController
import InvoiceController
import validacionCRUD

app=Flask(__name__)
DB = CustomerController
DBI = InvoiceController

#Rutas de navegacion frontend
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addCustomer')
def addCustomer():
    return render_template('addCustomer.html')    


@app.route('/customerList')
def customerList():
    customers = DB.getCustomers()
    return render_template('customerList.html', customers=customers)

@app.route('/invoiceList')
def invoiceList():
    invoices = DBI.getInvoices()
    return render_template('invoiceList.html', invoices=invoices)

@app.route('/addInvoice')
def addInvoice():
    return render_template('addInvoice.html')

#Lista de peticiones a la DB

@app.route('/customerAdd', methods=['POST'])
def customerAdd():
    name = request.form['name']
    status = request.form['status']
    mobile = request.form['mobile']
    DB.insertCustomer(name, status, mobile)
    return redirect('/customerList')
#Refactorizar con la validacion

@app.route('/editCustomer/<int:id>')
def editCustomer(id):
    customer = DB.getOneCustomer(id)
    return render_template('editCustomer.html', customer=customer)

@app.route('/customerUpdate', methods=['POST'])
def customerUpdate():
    name = request.form['name']
    status = request.form['status']
    mobile = request.form['mobile']
    id = request.form['id']
    DB.updateCustomer(name, status, mobile, id)
    return redirect('/customerList')
#Refactorizar con la validacion

@app.route('/deleteCustomer', methods=['POST'])
def deleteCustomer(): 
    id = request.form['id']
    query = validacionCRUD.deletingCustomer(id)
    if query:
        DB.deleteCustomer(id)
        return redirect('customerList')
    else:
        return redirect('/')
#Refactorizar con la validacion

#--------------------------------------------------------------------

#Crear peticiones a la DB desde la tabla Invoice y sus validaciones
@app.route('/invoiceAdd', methods=['POST'])
def invoiceAdd():
    customerIds = DB.getCustomerIds()
    dateInvoice = request.form['dateInvoice']
    idCustomer = request.form['idCustomer']
    price = request.form['price']
    balance = request.form['balance']

    query = validacionCRUD.addingInvoice(idCustomer)
    if query:
        DBI.insertInvoice(dateInvoice, idCustomer, price, balance)
        return redirect('/invoiceList')
    else:
        return redirect('/addInvoice')


    # IDCustomer = int(idCustomer)
    # listIds = []
    # data = customerIds

    # for i in range(len(data)):
    #     listIds.append(data[i][0]) 
    # newListIds = tuple(listIds)

    # response = IDCustomer in newListIds
    # if response:
    #     DBI.insertInvoice(dateInvoice, idCustomer, price, balance)
    #     return redirect('/invoiceList')
    # else:
    #     return redirect('/addInvoice')

@app.route('/editInvoice/<int:number>')
def editInvoice(number):
    invoice = DBI.getOneInvoice(number)
    return render_template('editInvoice.html', invoice=invoice)

@app.route('/invoiceUpdate', methods=['post'])
def invoiceUpdate():
    dateInvoice = request.form['dateInvoice']
    idCustomer = request.form['idCustomer']
    price = request.form['price']
    balance = request.form['balance']
    number = request.form['number']
    DBI.updateInvoice(dateInvoice, idCustomer, price, balance, number)
    return redirect('invoiceList')

@app.route('/deleteInvoice', methods=['POST'])
def deleteInvoice():
    number = request.form['number']
    query = validacionCRUD.deletingInvoice(number)
    if query:
        DBI.deleteInvoice(number)
        return redirect('/invoiceList')
    else:
        return redirect('/')

        



# Organizar peticiones CRUD a la DB
# Cambiar los datos estáticos por las peticiones desde el frontend
@app.route('/addI', methods=['POST'])
def addI():
    customIds = DB.getCustomerIds()
    date = '2021-10-04'
    idC = 11
    price = 66700
    balance = 13000
    query = validacionCRUD.addingInvoice(idC, customIds)
    if query:
        DBI.insertInvoice(date, idC, price, balance)
        return 'Factura Agregada'
    else:
        return 'No se puede agregar la factura porque no existe ese ID del cliente'
    

@app.route('/update', methods=['POST'])
def updateInvoices():
    number = 7
    date = '2020-11-06'
    idC = 11
    price = 66450
    balance = 0
    DBI.updateInvoice(date, idC, price, balance, number)
    return 'Factura actualizada'


@app.route('/delC', methods=['POST'])
def val():
    data = validacionCRUD.deletingCustomer(2)
    if data:
        DB.deleteCustomer(16)
        return 'Cliente eliminado correctamente'
    else:
        return 'No se puede eliminar el cliente'

@app.route('/delI', methods=['POST'])
def delI():
    data = validacionCRUD.deletingInvoice(2)
    if data:
        DBI.deleteInvoice(2)
        return 'Factura eliminada correctamente'
    else:
        return 'No se puede eliminar la factura'


if __name__ == "__main__":
    app.run(debug=True, port=3500)