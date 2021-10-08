from flask import Flask, render_template
app = Flask(__name__)


@app.route('/') 
def index():
    productos = ['Mouse Inalambrico', 'Teclado', 'SSD 512gb', 'Diadema']
    datos = {
        'titulo': 'Sistema de facturacion',
        'subtitulo': 'Manejo de clientes',
        'productos': ['Mouse Inalambrico', 'Teclado', 'SSD 512gb', 'Diadema'],
        'cantProductos': len(productos)
    }

    return render_template('index.html', data=datos)


@app.route('/login')
def login():
    user = "Jdom"
    return render_template('login.html', user = user)

if __name__ == '__main__':
    app.run(debug=True, port= 3500)