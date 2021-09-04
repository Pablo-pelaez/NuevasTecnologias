# from funciones import fibonacci

#PUNTO 8 Y 9

ciudad = ""
listaCiudades = []
while ciudad != "*":
    ciudad = input("Ingresa la ciudad: ")
    if ciudad != "*":
        listaCiudades.append(ciudad)

print(listaCiudades)

delCiudad = input("Ingrese la ciudad a borrar: ")
listaCiudades.remove(delCiudad)
print(listaCiudades)