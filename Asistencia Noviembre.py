#Ejercicio 7: Juego adivina un número
#REalizar un juego para adivinar un número. Para ello se debe
#generar un número aleatorio entre 1 - 100, y luego ir pidiendo
#nuemeros indicando "es mayor" o "es menor" según sea mayor o menor
#con respecto a N. EL proceso termina cuando el usuario acierta
#y alli se debe mostrar el número de intentos

import random
print("\t Juego adivina el número")
aleatorio = random.randint(0, 100) #Toma de 0 a 100 literal. generamos un numero aletorio
contador = 0
while True:
numero = int(input("Digite un numero: "))
contador += 1
if numero > aleatorio:
print("\t No es el numero, digite un número menor: ")
elif numero < aleatorio:
print("\t No es el numero, digite un número mayor")
else:
print(f"FELICIDADES, acabas de adivinar el número {aleatorio}")
break #rompe asi sale del ciclo
print(f"\n Número de intentos: {contador}")
