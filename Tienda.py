from producto import producto

class Tienda:

    """----------------------------------
    #Atributos
    ------------------------------------"""

    __producto1 = None
    __producto2 = None
    __producto3 = None
    __producto4 = None
    __dineroEnCaja = 0.0

    """-------------------------------------------
    #Metodos
    ----------------------------------------------"""
    def __init__(self):
        self.__producto1 = Producto("Papeleria", "Lapiz", 550.0, 18, 5)
        self.__producto2 = Producto("Papeleria", "Borrador")
        self.__producto3 = Producto("SuperMercado", "KiloCafe",)
        self.__producto4 = Producto("Drogueria", "Desinfectante", )

    def getProducto1(self):
        return self.__producto1
    


    Vender una cierta cantidad de productos cuyo nombre es igual a el recibido como parametro, el metodo retorna el numeor de unidades efectivamente vendidas 
    Supongas el nombre que se recuibe como paramentro correspónde a uno de los productos de la tienda, utilice el metodo vender de la clase producto como parte de su solucion. El metodo se va a llamar "vender producto" y recibe 2 parametros: nombre de producto y cantidad
    Calcular el numeor de productos de papeleria que se venden en la tienda, el metodo se llama "Cuantos Papeleria"
