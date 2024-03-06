class CuentaCorriente:
    #Aqui van datos de la simulacion
    '''----------------------------
    # Atributos
    ----------------------------'''
    saldo= ""
    '''----------------------------
    # Metodo
    ----------------------------'''
    def __init__(self):
        self.saldo= 200
    def ConsultarSaldo(self):
        #Aqui va el codigo del metodo
        print("Su saldo es:",self.saldo)
def main():
    objetoJuan= CuentaCorriente()
    objetoJuan.ConsultarSaldo()
    
if __name__== "__main__": 
    main()