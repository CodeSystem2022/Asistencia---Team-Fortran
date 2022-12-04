"""
!Apellido y nombre
codigo
-------------------
"""



# MORALES CASTRO DANISA

class Persona:
    contador_personas = 0   # Variable de clase

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1  # vamos incrementando
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} = {self.nombre} {self.edad}]'


persona1 = Persona('Ariel', 40)
print(persona1)
persona2 = Persona('Osvaldo', 45)
print(persona2)
persona3 = Persona('Liliana', 35)
print(persona3)
Persona.generar_siguiente_valor()
persona4 = Persona('Natalia', 35)
print(persona4)
print(f'Valor contador personas: {Persona.contador_personas}')

#--------------------------------------------------------------------------------------------------------------


#FACUNDO PEREYRA


class MiClase:
    # Variable de clase, este atributo dara a cada objeto el mismo valor
    variable_clase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia): #Variable de instancia
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)
def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)

print(MiClase.variable_clase)

miClase1 = MiClase('Esta es una variable de instancia')
print(miClase1.variable_instancia)
print(miClase1.variable_clase)
miClase2 = MiClase("Esta es otra prueba de variable de instancia")
print(miClase2.variable_instancia)
print(miClase2.variable_clase)
MiClase.variable_clase2 = 'Valor de variable de clase 2'
print(MiClase.variable_clase2)
print(miClase1.variable_clase2)
print(miClase2.variable_clase2)

MiClase.metodo_estatico()

MiClase.metodo_clase()


miObjeto1 = MiClase('variable de instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()

#--------------------------------------------------------------------------------------------------------------

# CALISAYA FERNANDO DANIEL

class Empleado:  # No hereda sino solo de la clase object
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f'Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]'

    def mostrar_detalles(self):
        return self.__str__()


#--------------------------------------------------------------------------------------------------------------
