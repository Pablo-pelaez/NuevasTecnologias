from os import name
from flask import Flask, app, render_template, request, redirect, flash, session
import CustomerController
import InvoiceController
import validacionCRUD
import UserController

app=Flask(__name__)
DB = CustomerController
DBI = InvoiceController
DBU = UserController
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



@app.route('/registerUser', methods=['post'])
def registerUser():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    photo = request.form['photo']
    
    query = validacionCRUD.existEmail(email)
    if query:
        flash('El correo ya existe en la DB')
        return redirect('/register')
    else:
        DBU.register(name, email, password, photo)
        return redirect('/')
    

@app.route('/loginUser', methods=['post'])
def loginUser():
    name = None
    email = request.form['email']
    password = request.form['password']
    query = validacionCRUD.verifyCredentials(email, password)
    
    if query:
        session['email'] = email
        session['password'] = password
        data = (DBU.getEmails())
        for i in range(len(data)):
            name = data[i][1]
        return render_template('index.html', name=name)
    else:
        flash('Las credenciales son incorrectas')
        return redirect('/login')
        
    

#Rutas de navegacion frontend
@app.route('/')
def index():
    if 'email' and 'password' in session:
        return render_template('index.html')
    else:
        return redirect('/login')   

@app.route('/login')
def logIn():
    return render_template('login.html')


@app.route('/addCustomer')
def addCustomer():
    if 'email' and 'password' in session:
        return render_template('addCustomer.html') 
    else:
        return redirect('/login')  


@app.route('/customerList')
def customerList():
    if 'email' and 'password' in session:
        customers = DB.getCustomers()
        return render_template('customerList.html', customers=customers)
    else:
        return redirect('/login')
    

@app.route('/invoiceList')
def invoiceList():
    if 'email' and 'password' in session:
        invoices = DBI.getInvoices()
        return render_template('invoiceList.html', invoices=invoices)
    else:
        return redirect('/login')


@app.route('/addInvoice')
def addInvoice():
    if 'email' and 'password' in session:
        return render_template('addInvoice.html')
    else:
        return redirect('/login')


@app.route('/register')
def register():
    return render_template('register.html')
    

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


@app.route('/deleteCustomer', methods=['POST'])
def deleteCustomer(): 
    id = request.form['id']
    query = validacionCRUD.deletingCustomer(id)
    if query:
        DB.deleteCustomer(id)
        flash('Cliente eliminado correctamente')
        return redirect('customerList')
    else:
        flash('No se puede eliminar el cliente')
        return redirect('customerList')
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

#--------------------------------------------------------------------

#Crear peticiones a la DB desde la tabla Invoice y sus validaciones
@app.route('/invoiceAdd', methods=['POST'])
def invoiceAdd():
    # customerIds = DB.getCustomerIds()
    dateInvoice = request.form['dateInvoice']
    idCustomer = request.form['idCustomer']
    price = request.form['price']
    balance = request.form['balance']

    query = validacionCRUD.addingInvoice(idCustomer)
    if query:
        DBI.insertInvoice(dateInvoice, idCustomer, price, balance)
        flash('Factura agregada correctamente')
        return redirect('/invoiceList')
    else:
        flash('No se puede agregar la factura')
        return redirect('/invoiceList')


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
    flash('Factura actualizada correctamente')
    return redirect('invoiceList')

@app.route('/deleteInvoice', methods=['POST'])
def deleteInvoice():
    number = request.form['number']
    query = validacionCRUD.deletingInvoice(number)
    if query:
        DBI.deleteInvoice(number)
        flash('Factura eliminada correctamente')
        return redirect('/invoiceList')
    else:
        flash('No se puede eliminar la factura')
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=3500)