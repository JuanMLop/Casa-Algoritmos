class CuentaCorriente:
    #Aqui van datos de la simulacion
    '''----------------------------
    # Atributos
    ----------------------------'''
    saldo= ""
    '''----------------------------
    # Metodo
    ----------------------------'''
    
    def ConsultarSaldo (self):
        # Aqui va el codigo del medoto
        return self.saldo
    
    def ConsignarValor (self, monto):
        nSaldo= self.saldo + monto
        self.saldo= nSaldo
        # Aqui va el codigo del medoto
        

    def RetirarValor (self, monto):
        cobrar= monto * 0.01
        self.saldo= self.saldo - cobrar
        return self.saldo
        # Aqui va el codigo del medoto
        
    
