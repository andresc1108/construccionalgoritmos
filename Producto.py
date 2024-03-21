from enum import Enum

"""---------------------------------------------
Enumeraciones
---------------------------------------------"""
class Tipo(Enum):
    """-----------------------------------------
    # Enumeraciones para los tipos de productos
    --------------------------------------------"""
    PAPELERIA = 1 
    SUPERMERCADO = 2
    FARMACIA = 3 

class producto:


    __subsidio = True
    __calidad = 'A'
    """----------------------------------------------
    # Constantes
    ---------------------------------------"""
    __IVA_PAPELERIA = 0.16
    __IVA_SUPERMERCADO = 0.04  
    __IVA_FARMACIA = 0.12

    PRECIO_MAXIMO = 50000

    """----------------------------------------------
    # Atributo
    ----------------------------------------------"""
    __nombre = None
    __tipo = Enum('Tipo',['PAPELERIA', 'SUPERMERCADO', 'FARMACIA'])
    __ValorUnitario = 0.0
    __CantidadBodega = 0
    __CantidadMinima = 0
    __CantidadUnidadesVendidas = 0

    """-------------------------------------------------
    # Metodos
    ----------------------------------------------------"""

    def getnombre(self):
        return self.__nombre
    
    def getTipo(self):
        return self.__tipo
    
    def getValorUnitario(self):
        return self.__ValorUnitario
    
    def getCantidadBodega(self):
        return self.__CantidadBodega
    
    def getCantidadMinima(self):
        return self.__CantidadMinima
    
    def getCantidadUnidadesVendidas(self):
        return self.__CantidadUnidadesVendidas
