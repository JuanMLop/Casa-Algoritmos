from cuentaCorriente import CuentaCorriente
from cuentaAhorros import CuentaAhorros
from CDT import CDT

class SimuladorBancario:
    '''----------------------------
    #Atributos
    ----------------------------'''
    cedula=""
    nombre=""
    mesActual= ""
    tiposDeClientes = "vip"

    """----------------------------
    # Asociaciones
    ----------------------------"""
    corriente= CuentaCorriente()
    ahorros= CuentaAhorros()
    cdt= CDT()
    '''----------------------------
    # Metodos
    ----------------------------'''

    def __init__(self, tiposDeClientes):
        self.tiposDeClientes= tiposDeClientes
    
    def ConsignarCorriente(self, monto):
    # Aqui va el codigo del medoto
        self.corriente.ConsignarValor(monto)
    
    def CalcularSaldo(self):
    # Aqui va el codigo del medoto
        return  self.ahorros.ConsultarSaldo() + self.corriente.ConsultarSaldo()
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
        saldoAhorros = self.ahorros.ConsultarSaldo()
        self.corriente.saldo += saldoAhorros
        self.ahorros.saldo = 0

    def ConsultarSaldoCuentaCorriente(self):
    # Aqui va el codigo del medoto
        return "Tu saldo es:"+self.corriente.ConsultarSaldo()
    
    def RetirarTodo (self):
    # Aqui va el codigo del medoto
        #saldoCorriente = self.ahorros.RetirarValor()
        #saldoAhorros = self.corriente.RetirarValor()
        #return saldoCorriente - saldoAhorros
    
        total= self.CalcularSaldo()
        self.corriente.RetirarValor(self.corriente.ConsultarSaldo())
        self.ahorros.RetirarValor(self.ahorros.ConsultarSaldo())
        return "Retiraste total:" + total
    
    def DuplicarAhorros (self):

        #saldo= self.corriente.RetirarValor-(self.corriente.RetirarValor)
        self.ahorros.saldo*= 2


    def CambiarTipoDecliente (self, Cliente):
        nCliente= self.tiposDeClientes
        return "Su cliente es:" + nCliente
     

    

    
