from    Punto import Punto
from Color import Color

class Triangulo:
    #Aqui va el codigo

    '''----------------------------
    #Atributos
    ----------------------------'''
    punto1 = ""  
    punto2 = ""
    punto3 = ""
    colorRelleno= ""
    colorLinea= ""
    """----------------------------
    # Asociaciones
    ----------------------------"""
    color= Color()
    punto= Punto()
    '''----------------------------
    # Metodos
    ----------------------------'''
    def ConsultarPunto1(self):
        return self.punto1
    def ConsultarPunto2(self):
        return self.punto2
    def ConsultarPunto3(self):
        return self.punto3
    

