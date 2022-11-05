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