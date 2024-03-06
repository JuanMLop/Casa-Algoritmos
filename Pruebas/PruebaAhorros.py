class CuentaAhorros:
    #simulacion cuenta de ahorros
    '''----------------------------
    #Atributos
    ----------------------------'''
    saldo= ""
    interesesMensuales= ""
    '''----------------------------
    # Metodo
    ----------------------------'''
    def __init__(self):
        self.saldo=0
        self.interesesMensuales=0
    def ConsignarValor(self):
        #Aqui va el codigo del metodo
        a=input("Ingrese valor a cosignar:")
        self.saldo = self.saldo+int(a)     
    def RetiraValor(self):
        r=input("Valor a retirar:")
        self.saldo = self.saldo-int(r)
    def InteresMensual(self):
        #Aqui va el codigo del metodo
        i=input("Interes mensual:")
        self.inteteres = self.saldo * float(i)
        self.saldo = self.saldo + self.inteteres
        print("Nuevo saldo:",self.saldo)
    def ConsultarSaldo(self):
        print("Nuevo saldo:",self.saldo)
def main():
    objetoJuan= CuentaAhorros()
    objetoJuan.ConsignarValor()
    objetoJuan.RetiraValor()
    objetoJuan.ConsultarSaldo()
    objetoJuan.InteresMensual()


if __name__== "__main__":
    main()