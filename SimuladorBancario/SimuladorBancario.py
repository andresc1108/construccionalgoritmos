from CuentaAhorro import CuentaAhorro
from CuentaCorriente import CuentaCorriente
from CDT import CDT

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
    corriente = CuentaCorriente()
    ahorro = CuentaAhorro()
    cdt = CDT()

    """------------------------------
    #Metodos
    ----------------------------------"""

  def ConsignarCuentaCorriente(self, monto):
        self.corriente.ConsignarMonto(monto)
        
    def CalcularSaldoTotal(self):
        # Forma1
        return self.corriente.ConsultarSaldo()+self.ahorros.ConsultarSaldo()

        # #Forma2
        # saldoAhorros = self.ahorros.ConsultarSaldo()
        # saldoCorriente = self.corriente.ConsultarSaldo()
        # return saldoAhorros+saldoCorriente
        
    def PasarAhorrosACorriente(self):
        # forma1
        # self.corriente.ConsignarMonto(self.ahorros.ConsultarSaldo())
        # self.ahorros.RetirarMonto(self.ahorros.ConsultarSaldo())
        
        # forma 2
        # saldoAhorros = self.ahorros.ConsultarSaldo()
        # self.ConsignarCuentaCorriente(saldoAhorros)
        # self.ahorros.RetirarMonto(self, saldoAhorros)
        
        #forma 3
        saldoAhorros = self.ahorros.ConsultarSaldo()
        self.corriente.saldo += saldoAhorros
        self.ahorros.saldo = 0

class empleado:

    """----------------
    Atributos
    -------------------"""
    TipoCliente= ""
    """-----------------------
    #1 = vip , 2 = platino y 3 = normal
    -------------------------"""
    def _init_(self, TipoCliente):
            self.TipoCliente = TipoCliente

    def CambiarTipoCliente (self, nTipoCliente):
            self.TipoCliente = nTipoCliente
            return None
        
