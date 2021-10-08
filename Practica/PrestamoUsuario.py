#Realizar un programa que conste de una clase llamada Usuario 
# que contenga como atributos el nombre y el valor de sus ahorros
# Definir los métodos para inicializar sus propiedades, imprimirlos y
# mostrarlos en pantalla indicando si se le permite el préstamo o no

class Usuario:
    __nombre__ = ''
    __ahorros__ = ''
    __validacionAhorros__ = None

    def __init__(self, nombre, ahorros):
        self.__nombre__ = nombre
        self.__ahorros__ = ahorros

#------------------------------------------------------

    def setNombre(self, nombre):
        self.__nombre__ = nombre

    def getNombre(self):
        return self.__nombre__

    def setAhorros(self, ahorros):
        self.__ahorros__ = ahorros

    def getAhorros(self):
        return self.__ahorros__

#------------------------------------------------------

    def validarPrestamo(self, nombre, ahorros):
        self.__ahorros__ = ahorros
        self.__nombre__ = nombre
        if self.__ahorros__ > 10000000:
            validacionAhorros = True
            return validacionAhorros
        else:
            validacionAhorros = False
            return validacionAhorros
        




