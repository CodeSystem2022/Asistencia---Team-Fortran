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



# VIZCAINO LUCAS
class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")

    @property #Decorador
    def nombre(self): #Metodo Getter
        print("Estamos utilizando el metodo get")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):# Metodo setter
        print("Estamos utilizando el metodo set")
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __del__(self):
        print(f"Persona2: {self._nombre} {self._apellido} {self._edad}")

if __name__ == "__main__":
    persona1 = Persona2("Ariel", "Betancud", 41)
    print(persona1.nombre) #Llamamos al metodo getter
    persona1.nombre = "Juan Pedro" #Llamamos al metodo setter
    print(persona1.nombre)
    print(persona1.mostrar_detalles())#Llamamos al metodo mostrar detalles
#Atributo read-only seria la edad porque no tiene metodo set
    print(persona1.edad)

    persona2 =  Persona2("Flor", "Martines", 33)
    print(persona2.nombre)
    persona2.nombre = "Alexa"
    persona2.apellido = "Martinez"
    persona2.edad = 32
    print(persona2.mostrar_detalles())

    persona3 = Persona2("Alex", "Rosas", 22)
    persona3.nombre = "Alexander"
    persona3.apellido = "Rosario"
    persona3.edad = 21
    print(persona3.mostrar_detalles())

    persona4 = Persona2("Lucas", "Betancud", 32)
    persona4.nombre = "Luca"
    persona4.apellido = "Betancudd"
    persona4.edad = 31
    print(persona4.mostrar_detalles())

    print(__name__)
    
#--------------------------------------------------------------------------------------------------------
    
    
    
# MORALES GASTON
    
    class Rectangulo:
    """
    Crear una class llamada Rectangulo, debe tener  2 atributas: altura y base
    el nombre del metodo sera calcular area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas
    por el usuario y los objetos deben ser tres.
    """
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.base * self.altura

base = init(input("Digite el numero para la base del rectangulo: "))
altura = init(input("Digite el numero para la altura del rectangulo: "))
rectangulo1 = rectangulo(base, altura)
print(f"El area del rectangulo es: {rectangulo1.calcular_area()}")

#--------------------------------------------------------------------------------------------------------


