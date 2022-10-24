# Ejercicio06:Crear una función para sumar los vaores recibidos de tipo
# númericos,utilizando argumentos variables *args como parametros de la
# Función y agregar como reultado la suma de todos lo valores pasados
# como argumentos.
def sumar_valor(*args):  # Recibimos una cantidad de parametros indefinidos
    resultado = 0
    # Iteramos cada elemento
    for valor in args:
        resultado += valor
        return resultado


# Llamamos a la función
print(sumar_valor(2, 6, 9))
