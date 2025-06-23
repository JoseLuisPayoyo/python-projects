# pedir nombre, apellido y año de nacimiento
# de nombre y apellido las dos primeras letras y a mayusculas
# de año los dos ultimos
# mas valor de 4 digitos aleatorios

from random import randint

print(" *** Sistema generador de ID unico *** ")
nombre_inicial = input("Cual es tu nombre: ")
apellido_inicial = input("Cual es tu apellido: ")
anio_nacimiento_inicial = input("Año de nacimiento (YYYY): ")

nombre = nombre_inicial.strip().upper()[0:2]
apellido = apellido_inicial.strip().upper()[0:2]
anio_nacimiento = anio_nacimiento_inicial.strip()[2:]
id = randint(1000, 9999)

id_unico = f"{nombre}{apellido}{anio_nacimiento}{id}"

print(f"\nHola {nombre_inicial}")
print(f"\tTu nuevo numero de identifiacion (ID) generado es:")
print(f"\t{id_unico}")
print("\tFelicidades!")