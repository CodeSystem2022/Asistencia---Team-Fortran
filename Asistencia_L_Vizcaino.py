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