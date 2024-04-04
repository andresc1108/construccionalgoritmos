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
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setTipo(self, tipo):
        self.__tipo = tipo

    def setValorUnitario(self, ValorUnitario):
        self.__ValorUnitario = ValorUnitario

    def setCantidadBodega(self, CantidadBodega):
        self.__CantidadBodega = CantidadBodega
    
    def setCantidadMinima(self, CantidadMinima):
        self.__CantidadMinima = CantidadMinima

    def setCantidadUnidadesVendidas(self, CantidadUnidadesVendidas):
        self.__CantidadUnidadesVendidas = CantidadUnidadesVendidas

    def Vender(self, cantidad):
        if cantidad <= self.__CantidadBodega:
            self.__CantidadUnidadesVendidas += cantidad
            self.__CantidadBodega -= cantidad 
        else:
            print("Cantidad no disponible")
    def HaySuficiente(self, cantidad):
        if cantidad <=self.__CantidadBodega:
            return True
        
    #Forma 2 
        #if cantidad <=self.__CantidadBodega:
            HaySuficiente = False
            return HaySuficiente
    #Forma 3
        #return cantidad <=self.__CantidadBodega

        
    def DarIva(self):
        if(self.__tipo=="PAPELERIA"):
            return self.::__IVA_PAPELERIA
        elif(self.__tipo=="FARMACIA"):
            return self.__IVA_FARMACIA
        elif(self.__tipo=="SUPERMERCADO"):
            return self.__IVA_SUPERMERCADO
        else:
            print("Categoria de producto no existe")

        
        #*Si el producto cuesta - de 1000 aumentar el 1%, si cuesta entre 1 y 5 mil aumenta el 2%, si cuesta más de 5000 el 3%
        #*Recibir un pedido solo si en la bodega se tiene menos unidades de las indicadas en el tope minimo, en caso contrario el metodo no debe hacer nada, el metodo se llama "Hace pedido" y tiene un parametro 
        #*modificar el precio del producto utilizando la siguiente politica, si el producto es de drogueria o papeleria debe dispminuir un 10%, si es de supermercado debe aumentar un 5%, el metodo se va allamar "Cambiar Valor Unitario"
        #*Vender una cierta cantidad de productos cuyo nombre es igual a el recibido como parametro, el metodo retorna el numeor de unidades efectivamente vendidas 
        #*Supongas el nombre que se recuibe como paramentro correspónde a uno de los productos de la tienda, utilice el metodo vender de la clase producto como parte de su solucion. El metodo se va a llamar "vender producto" y recibe 2 parametros: nombre de producto y cantidad
        #*Calcular el numeor de productos de papeleria que se venden en la tienda, el metodo se llama "Cuantos Papeleria"
