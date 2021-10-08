from PrestamoUsuario import Usuario

Usuario = Usuario('Mark', 100)

def imprimirResultado(nombre, ahorros):
        validacion = Usuario.validarPrestamo(nombre, ahorros)
        respuesta = f'{nombre}, tu crédito ha sido aprobado' if validacion else f'{nombre}, tu crédito fue denegado'
        print(respuesta)

lista = [
    {
        'nombre': 'Mark',
        'ahorros': 10000000
    },
    {
        'nombre': 'Mike',
        'ahorros': 10000000
    },
    {
        'nombre': 'Tessa',
        'ahorros': 10000001
    },
    {
        'nombre': 'Soria',
        'ahorros': 10000001
    },
    {
        'nombre': 'Jaime',
        'ahorros': 100000003
    }
]
nombre = ''
ahorros = ''
# while nombre != '*' or ahorros != '*':
#     nombre = input('Ingresa tu nombre: ')
#     ahorros = input('Ingresa tus ahorros: ')
#     # if nombre != '*' and ahorros != '*':
#     lista.append({'nombre': nombre, 'ahorros': ahorros})
#     # print(lista[4]['nombre'], lista[4]['ahorros'])


for i in range(len(lista)):
    # print(lista[i]['nombre'], lista[i]['ahorros'])
    imprimirResultado(lista[i]['nombre'], lista[i]['ahorros'])







