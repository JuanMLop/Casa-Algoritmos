class CDT:
    #Simulacion de un cdt
    '''----------------------------
    #Atributos
    ----------------------------'''
    valorInversion=""
    interesMensual=""
    mesApertura= "" 
    '''----------------------------
    # Metodo
    ----------------------------'''
    def __init__(self):
        self.valorInversion=0
        self.interesMensual=0
        self.mesApertura=0
        self.saldo=0
        self.inteteres=0
    
    def ConsignarValor(self):
        #Aqui va el codigo del metodo
        a=input("Valor de la inversion:")
        self.saldo = self.saldo+int(a)
        print ("Su CDT fue actualizado exitosamente") 
        
    def ConsultarSaldo(self):
        print("Nuevo saldo:",self.saldo)
    
    def Interes(self):
        i=input("Interes mensual:")
        self.inteteres = self.saldo * float(i)
        self.saldo = self.saldo + self.inteteres
        print("Su saldo con intereses es:",self.saldo)

def main():
    objetoJuan= CDT()
    objetoJuan.ConsignarValor()
    objetoJuan.ConsultarSaldo()
    objetoJuan.Interes()
    


if __name__== "__main__":
    main()