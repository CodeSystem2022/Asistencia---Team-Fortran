class Vehiculo:
    """
    Definir una clase padre llamada Vehiculo y dos clases hijas llamadas
    Auto y Bisicletas, las cuales heredan de la clase padre Vehiculo. La clase
    padre debe tener los siguientes atributos y métodos:

    Vehiculo (clase padre)
    -Atributos(color, ruedas)
    -Métodos(__init__(color, ruedas) y __str__())

    Auto(clase hija de Vehiculo)
    -Atributos(velocidad (km/hs))
    -Métodos(__init__(color, rueda, velocidad) y __str__())

    Bisicleta(clase hija de Vehiculo)
    -Atributo(tipo(urbano/montaña/etc.))
    -Método(__init__(color, rueda y tipo) y __str__())

    Crear un objeto de cada clase
    """
    #Clase padre creado, con su metodo inicializador init
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    #Tambien con su metodo str
    def __str__(self):
        return f'Color: '+self.color+', Ruedas: '+ str(self.ruedas)

#Creamos la clase hija de Vehiculo, Auto
class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        #Traer de clase padre
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__()+', Velocidad(km/hs): '+str(self.velocidad)

#Creamos la clase hija de Vehiculo, Bisicleta
class Bisicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__()+', Tipo: '+self.tipo

# Primer objeto de la clase padre Vehiculo
vehiculo = Vehiculo('Blanco', 4)
print(vehiculo)

# Segundo objeto, pero ahora de la clase Auto
auto = Auto('Amarillo', 4, 120)
print(auto)

# Tercer objeto, pero ahora de la clase Bisicleta
bisicleta = Bisicleta('Azul', 2, 'Urbana')
print(bisicleta)