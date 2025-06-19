cadena = "Hola, Mundo!"

# obtener subcadena hola [inicio:fin] sin incluir
subcadena_hola = cadena[0:4]
print(subcadena_hola)

# buscar subcadena
# find() devuelve el primer indice de la subcadena que le pasemos
posicion = cadena.find("Mundo!")
print(f"Posicion de Mundo: {posicion}")

# reemplazar subcadenas
nueva_cadena = cadena.replace("Mundo!", "a todos!")
print(nueva_cadena)

#separar subcadenas por separado
datos = "Juan, 30, Mexico"
lista = datos.split(",")
print(lista)
print(f"Nombre: {lista[0]}")
print(f"Edad: {lista[1]}")
print(f"Pais: {lista[2]}")