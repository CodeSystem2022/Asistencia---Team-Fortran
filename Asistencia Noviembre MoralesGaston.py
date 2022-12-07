class Persona:
    contador_personas = 0
    def __init__(self, nombre, edad):
        Persona.contador_personas += 1
        self.id_persona = persona.contador_personas
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"persona [{self.id_persona} = {self.nombre} {self.edad}]"

    persona1 = Persona("Ariel", 40)
    print(persona1)
    persona2 = Persona("Osvaldo", 45)
    print(persona2)
    persona3 = Persona("Liliana", 35)
    print(persona3)
    print(f"valor contador personas: {Persona.contador_personas}")