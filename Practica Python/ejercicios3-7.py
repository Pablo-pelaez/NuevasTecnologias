# PUNTO 3

# fifthPrime = 11
# italyCapital = "Rome"
# animal = "Peacock"
# century = "19"  

# dataDictionary = {
#     "fifthPrime": fifthPrime,
#     "italyCapital": italyCapital,
#     "animal": animal,
#     "century": century
# }

# print(f"\n{dataDictionary}\n")

#----------------------------------------------------------------

# PUNTO 4

# lista = []
# lengthNumber = 50
# for i in range(1, lengthNumber+1):
#         lista.append(i)

# print(lista)

#-----------------------------------------------------------------

#PUNTO 5

# listaImpar = []
# lengthNumber = 50

# for n in range(lengthNumber + 1):
#     if n % 2 == 0 and n > 0:
#         listaImpar.append(n)

# print(lista)

#-------------------------------------------------------------------------------

# PUNTO 6 Y 7

# automovil = {
#     'placa': 'AFT564',
#     'marca': 'RENAULT',
#     'valor': 85000000
# }
# print("Los datos del automóvil son los siguientes:")
# for i in automovil:
#     print(f"{i} {automovil[i]}")

#------------------------------------------------------------------------------------

#PUNTO 8 Y 9 Crear una lista, con datos por teclado, 
# que contenga las ciudades turísticas de Colombia

# ciudades = []
# numCiudades = int(input('Establece el número de ciudades: '))



# for i in range(numCiudades):
#     ciudades.append(input('Ingresa la ciudad de destino: '))

# print('Las ciudades ingresadas por el usuario son las siguientes: ')

# for n in ciudades:
#     print(n)


# ciudad = ""
# listaCiudades = []
# while ciudad != "*":
#     ciudad = input("Ingresa la ciudad: ")
#     if ciudad != "*":
#         listaCiudades.append(ciudad)

# print(listaCiudades)

# delCiudad = input("Ingrese la ciudad a borrar: ")
# listaCiudades.remove(delCiudad)
# print(listaCiudades)

#--------------------------------------------------------------------------------

#PUNTO 10 Y 11

# ciudades.append('Cali')
# ciudades.pop()

# print(ciudades)

#------------------------------------------------------------------------------------


#PUNTO 13

#Importar e Instanciar Objeto de la clase Vehiculo

# from Vehiculo import Vehiculo

# newVehicle = Vehiculo('ART587', 'Renault', '2021', 90000000)

# modelo = newVehicle.getModelo()

# print(modelo)


