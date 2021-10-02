from flask import Flask, render_template, url_for, redirect, jsonify
# from flask_mysqldb import MySQL

#Conexion a la base de datos de MySQL
# cnx = MySQL(app)
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dbflask'



# app.route('/customers')
# def listCustomers():
#     dataCustomer = {}
#     try:
#         cursorCustomer = cnx.connection.cursor()
#         query = 'select id, nombre, telefono, correo from cliente'
#         cursorCustomer.excute(query)
#         customers = cursorCustomer.fetchall()
#         dataCustomer['customers'] = customers
#     except Exception as ex:
#         dataCustomer['message'] = 'Error ...'
#     return jsonify(dataCustomer)


@app.route('/')

def index():
    programas = ['Desarrollo','Redes','Sistemas','Video Juegos','Administracion', 'Fotografia']
    submodulos = ['Logica', 'Cisco', 'Excel', 'Unity', 'Finanzas', 'Teoria del color' ]

    datos = {
        'titulo':' Sistema Academico',
        'bienvenida': 'Saludos desde CESDE',
        'programas': programas,
        'cantidadProgs': len(programas),
        'valorcuota': 1200000,
        'telefonos' : ['4889756', '3148964476'],
        'submodulos' : submodulos,
    }
    return render_template('index.html', datosPag=datos)


@app.route('/fotos')
def fotos():
    return render_template('fotos.html')

def noPageFound(error):
    #return render_template('404.html'), 404
    return redirect(url_for('index'))
app.register_error_handler(404, noPageFound)

if __name__== "__main__":
    app.run(debug=True, port=3500)