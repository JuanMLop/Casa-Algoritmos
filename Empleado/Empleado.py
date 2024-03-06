from Fecha import Fecha

class Empleado:

    #Aqui va el codigo

    '''----------------------------
    #Atributos
    ----------------------------'''
    nombre= ""  
    apellido= ""
    numeroHijosEmpleado= ""
    '''----------------------------
    # 1= Masculino y 2= Femenino
    ----------------------------'''
    sexo= ""
    salario= ""
    """----------------------------
    # Asociaciones
    ----------------------------"""
    fechaNacimiento=Fecha()
    fechaIngreso=Fecha()
    

    '''----------------------------
    # Metodos
    ----------------------------'''
    def __init__(self, nombre, apellido, sexo, salario):
        self.nombre = nombre
        self.apellido =apellido
        self.sexo = sexo
        self.salario = salario

    def CambiarSalario(self, nuevoSalario):
    # Aqui va el codigo del medoto
        return 0
    def CambiarEmpleado(self, nNombre, nApellido, nSexo, nSalrio):
    # Aqui va el codigo del medoto
        return  None
    def ConsultarSalario(self):
    # Aqui va el codigo del medoto
        return self.salario
    def ConsultarNombre(self):
    # Aqui va el codigo del medoto
        return self.nombre
    def ConsultarApellido(self):
    # Aqui va el codigo del medoto
        return self.apellido
    def ConsultarNombreCompleto(self):
    # Aqui va el codigo del medoto
        return self.nombre +" "+ self.apellido
    def AumentoSalario(self):
    # Aqui va el codigo del medoto
        nSalario= self.salario * 0.05
        nSalario= nSalario + self.salario
        self.salario= nSalario
        return "El nuevo salario es de: " + self.salario
    def DuplicarSalraio(self):
    # Aqui va el codigo del medoto
        #forma1
        #self.salario = self.salario*2
        #forma2
        self.salario *= 2
    def SalarioAnual(self):
    # Aqui va el codigo del medoto
        # Forma 1 
        aSalario = self.salario * 12
        return aSalario
        # Forma 2
        # return self.salario*12
    def ConsultarDiaCumpleños(self):
        return "El dia de su cumpleaños es:"+self.fechaNacimiento.ConsultarDia()
    def CalcularImpuesto(self):
        #Forma 1
        return self.SalarioAnual() * 0.195
        #Forma 2
        #total= self.SalarioAnual()
        #return (total*19.5)/ 100
    def ConsultarNumeroDeHijos (self):  
        return self.numeroHijosEmpleado
    def AuxilioEducativoEmpleadoHijos(self):
        auxEmpleado= self.salario * 0.05(self.numeroHijosEmpleado)
        return auxEmpleado

    def AuxilioEmpleadoParametro (self, porcentaje):
        auxSalarioParametro= self.salario * porcentaje / 100 (self.numeroHijosEmpleado)
        return auxSalarioParametro
    
    def DiferenciaSalarial (self, sNuevoEmpleado):
        diferencia= self.salario - sNuevoEmpleado
        return diferencia
    
        
    

    
