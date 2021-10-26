from os import name
from flask import Flask, app, render_template, request, redirect
import CustomerController

app=Flask(__name__)
DB = CustomerController

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

@app.route('/addInvoice')
def addInvoice():
    return render_template('addInvoice.html')

@app.route('/invoiceList')
def invoiceList():
    return render_template('invoiceList.html')

#------------------
@app.route('/customerAdd', methods=['POST'])
def customerAdd():
    name = request.form['name']
    status = request.form['status']
    mobile = request.form['mobile']
    DB.insertCustomer(name, status, mobile)
    return redirect('/customerList')

@app.route('/customerUpdate', methods=['POST'])
def customerUpdate(id):
    name = request.form['name']
    status = request.form['status']
    mobile = request.form['mobile']
    DB.updateCustomer(name, status, mobile, id)
    return redirect('/customerList')

if __name__ == "__main__":
    app.run(debug=True, port=3500)