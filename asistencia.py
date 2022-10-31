"""
!Apellido y nombre
codigo
------------------- 
"""
"""
#Gabriel Hidalgo
codigo
------------------- 

class Persona: #Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): #Se lo llama metodo Init Dunder
        #Argumentos variables *args y **kwargs
        #Son del tipo Publico los atributos
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni  #Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): #self es igual a this
        print(f'la clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self.edad}, la dirección es: {self.args}, los datos importantes son: {self.kwargs}')



persona1 = Persona('Ariel', 'Betancud', 355855,40) # Nesecitamos enviar argumentos
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

"""
