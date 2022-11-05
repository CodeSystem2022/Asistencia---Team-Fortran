"""
!Apellido y nombre
codigo
------------------- 
"""
"""




# HIDALGO GABRIEL

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
#--------------------------------------------------------------------------------------------------------------



# CALISAYA FERNANDO

class Aritmetica:
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    def sumar(self):
        return self.operandoA + self.operandoB
    def resta(self):
        return self.operandoA - self.operandoB
    def multiplicar(self):
        return self.operandoA * self.operandoB
    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(49, 7)
print(f'La suma de los números es: {aritmetica1.sumar()}')
print(f'la resta de los números es: {aritmetica1.resta()}')
print(f'La multiplicación de los números es: {aritmetica1.multiplicar()}')
print(f'La división de los números es: {aritmetica1.dividir():.2f}')

# -------------------------------------------------------------------------------------------------------------



# MORALES CASTRO DANISA

class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho, alto y profundidad,
    con un método calcular_volumen que tendría la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese valores.
    """

    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad

ancho = int(input("Digite el ancho del cubo: "))
altura = int(input("Digite la altura del cubo: "))
profundidad = int(input("Digite la profundidad del cubo: "))

cubo1 = Cubo(ancho, altura, profundidad)
print(f"El volumen del cubo es: {cubo1.calcular_volumen()}")

#-------------------------------------------------------------------------------------------------------------



# PEREYRA FACUNDO

class Persona:  # Esta clase hereda de la clase Object
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad


class Empleado(Persona):  # Esta clase es hija de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo


empleado1 = Empleado('Ariel', 40, 75000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

empleado2 = Empleado('Liliana', 38, 70000)
empleado2.nombre = 'Natalia'
empleado2.edad = 35
empleado2.sueldo = 75000
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

# -------------------------------------------------------------------------------------------------------------



# VIZCAINO GISELA

class Aritmetica:
    """
    El nombre de este tipo de comentario es: DocString
    esto es documentacion de la clase en python
    Vamos a hacer en esta clase algunas operaciones de: suma, resta, multiplicacion y mas
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    #METODO PARA SUMAR
    def sumar(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(7, 9) #Le pasamos los argumentos para los operando
print(f'La suma de los numeros es: {aritmetica1.sumar()}') 
print(f'La resta de los numeros es: {aritmetica1.resta()}')
print(f'La multiplicacion de los numeros es: {aritmetica1.multiplicar()}')
print(f'La division de los numeros es: {aritmetica1.dividir():.2f}')

#--------------------------------------------------------------------------------------------------------
