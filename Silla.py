from Pasajero import pasajero
from enum import Enum
class silla:
    class clase(Enum):
        __EJECUTIVA=1
        __ECONOMICA=2
    class ubicacion(Enum):
        __VENTANA=1
        __CENTRO=2
        __PASILLO=3
    def __init__(self,pNumero,pClase,pUbicacion):
        self.numero=self,pNumero
        self.clase=self.pClase
        self.ubicacion=pUbicacion
        self.pasajero=None
    def asignarSilla(self,pPasajero):
        self.pasajero=pPasajero
    def desAsignarPasajero(self):
        self.pasajero=None
    def sillaAsignada(self):
        if self.pasajero is None:
            print("La silla esta desocupada")
        else:
            print("La silla esta ocupada")
    def darNumero(self):
        return self.numero
