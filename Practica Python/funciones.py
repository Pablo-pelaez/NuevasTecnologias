def numFactorial(number):
    number
    factorial = 1
    for i in range(1, number+1):
        factorial = factorial * i
    return factorial  
    
print(numFactorial(4))

#-----------------------------------------------------------------------------------------------
# def fibonacciNumber(nTerms):

#     def recursiveFibonacci(number):
#         if number <= 1:
#             return number
#         else:
#             return(recursiveFibonacci(number-1) + recursiveFibonacci(number-2))

#     nTerms

#     if nTerms <= 0:
#         print("Debes ingresar un valor positivo")
#     else:
#         print(f"La secuencia de fibonacci con los {nTerms} primeros términos es la siguiente: ")
#         for i in range(nTerms):
#             print(recursiveFibonacci(i))

# fibonacciNumber(8)

def fibonacci(nTerms):
    secFibo = [0,1]
    anterior, siguiente = 0,1

    for i in range(3, nTerms + 1):
        resultado = anterior + siguiente
        secFibo.append(resultado)
        anterior = siguiente
        siguiente = resultado
    return secFibo

#--------------------------------------------------------------------------------------------------

#Retornar el valor de la cuota de un prestamo, teniendo en cuenta que se debe especificar el valor del préstamo, número de cuotas, tasa mensual

def cuotaPrestamo(prestamo, nCuotas):
    tasaMensual = 0

    if prestamo <= 0 and nCuotas <=0:
        print("Ingresa un valor mayor a 0")
    else:
        if prestamo <= 5000000 and nCuotas <= 12:
            tasaMensual = 0.15
            cuotaMensual = (prestamo / nCuotas) + (prestamo / nCuotas * tasaMensual)
            total = cuotaMensual * nCuotas 
        else:
            if prestamo <=10000000 and nCuotas <= 24:
                print("prueba2")
            else:
                print("prueba3")
    
    return (cuotaMensual, total)


res = cuotaPrestamo(5000000, 10)
print(f"El valor de cada cuota y el total a pagar son los siguientes: {res}")

#--------------------------------------------------------------------------------------------

arrayPeople = [
    {
        "ID": "00879",
        "name": "Jaime",
        "email": "jaimerf24@gmail.com"
    },
    {
        "ID": "00775",
        "name": "Mark",
        "email": "marktf14@gmail.com"
    },
    {
        "ID": "00684",
        "name": "Teressa",
        "email": "tessagh47@gmail.com"
    },
    {
        "ID": "00426",
        "name": "Jem",
        "email": "jemcf55@gmail.com"
    },
    {
        "ID": "00539",
        "name": "Nate",
        "email": "nateft47@gmail.com"
    },
    {
        "ID": "00175",
        "name": "Kate",
        "email": "katetrf24@gmail.com"
    }
]

arrayNumbers = [1,2,3,4,5,6,7,8,9,11,111,132]


def mostrarDatos(arrayData):
    for data in arrayData:
        print(data)


mostrarDatos(arrayNumbers)

#------------------------------------------------------------------------------------------------
diccionarioEstudiuante = {
        "ID": "00175",
        "name": "Nate",
        "edad": "17",
        "email": "natefr24@gmail.com",
        "especializacion": "Desarrollo Web",
        "materias": ["Programación Avanzada", "Nuevas Tecnologías", "Móviles III"]
    }

def showDictionary(dictionaryData):
    for data in dictionaryData:
        valor = dictionaryData[data]
        print(data, valor)
    

showDictionary(diccionarioEstudiuante)

#---------------------------------------------------------------------------------------------
dpagos= {
    "placa":"tis123",
    "marca":"Aveo",
    "pagos":[100,200,30,400]
    }

def totalPagos(diccionario):
    total = 0
    for data in diccionario:
        if data == "pagos":
            pagos = diccionario[data]


    for data in range(len(pagos)):
        total += pagos[data]
        
    return total

            # for in range(len(diccionario[data])):
            #     total =+ diccionario[data]
    
    # return total

print(totalPagos(dpagos))

