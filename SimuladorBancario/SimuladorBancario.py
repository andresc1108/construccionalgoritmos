from CuentaCorriente import CuentaCorriente
from CuentaAhorro import CuentaAhorro


class SimuladorBancario:
    """----------------------
    #Atributos
    -------------------------"""
    Cedula= 0
    Nombre= 0
    MesActual= 0

    """-------------------------------
    #Asociaciones
    ----------------------------------"""
    CuentaCorriente = CuentaCorriente()
    CuentaAhorro = CuentaAhorro()

    """------------------------------
    #Metodos
    ----------------------------------"""

    def CalcularSaldoTotal(self):
        #Aqui va el codigo
        return "Este es el saldo total: "+self.CuentaCorriente.Saldocorriente()+ self.CuentaAhorro.ConsultarSaldo()
    
    def ConsignarCuentaCorriente(self.saldo):
        #Aqui va el codigo
        return self.sald

    def TrasferirSaldoCuentaCorrienteCuentaAhorro(self.)


