class CDT:
    #Simulacion de un cdt
    valorInversion=""
    interesMensual=""
    mesApertura= "" 
    '''----------------------------
    #Atributos
    ----------------------------'''
    valorInversion=""
    interesMensual=""
    mesApertura= "" 
    saldo= ""
    '''----------------------------
    # Metodo
    ----------------------------'''
    def ConsignarValor(self, saldo):
        #Aqui va el codigo del metodo
        self.saldo = self.saldo+ ""
        return self.saldo
        print ("Su CDT fue actualizado exitosamente") 
    def ConsultarSaldo(self, saldo):
        return("Nuevo saldo:",self.saldo)
    def Interes(self, saldo):
        #Aqui va el codigo del metodo
        nSaldo= self.saldo * 0,0
        nSaldo= self.saldo + nSaldo
        self.saldo= nSaldo
        return "Su saldo mas los intereses es de:" + self.saldo
