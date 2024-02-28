class CuentaCorriente:
    """----------------------------------
    #Atributos
    -------------------------------------"""
    saldo= 0

    """----------------------------------
    Metodos
    -------------------------------------"""
    def ConsultarSaldo(self):
        #Aquiva el codigo del metodo
        return self.saldo
    
    def ConsignarValor(self,saldo):
        nSaldo = self.saldo + ""
        self.saldo = nSaldo
        return "ingrese un valor" + ""
    
    def RetirarValor(self,saldo):
        nSaldo = self.saldo + ""
        self.saldo = nSaldo
        return "ingrese valor a retirar" + ""
