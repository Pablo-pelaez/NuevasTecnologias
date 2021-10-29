from flask import Flask, render_template, request, redirect, flash
import UserController  

app = Flask(__name__)
DB = UserController

@app.route('/')
@app.route('/index')
def index():
    users = DB.getUsers()
    return render_template('index.html', users=users)

@app.route('/formAddUser')
def formAddUser():
    return render_template('addUser.html')

@app.route('/saveUser', methods=['POST'])
def saveUser():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    DB.insertUser(name, email, password)
    return redirect('/index')

@app.route('/deleteUser', methods=['POST'])
def deleteUser():
    id = request.form['id']
    DB.deleteUser(id)
    return redirect('/')

@app.route('/editUser/<int:id>')
def editUser(id):
    user = DB.getOneUser(id)
    return render_template('editUser.html', user=user)

@app.route('/updateUser', methods=['POST'])
def updateUser():
    id = request.form['id']
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    DB.updateUser(name, email, password, id)
    return redirect('/index')

if __name__ == "__main__":
    app.run(port=3501, debug=True)

