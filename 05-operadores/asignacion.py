texto = "Hola"

a, b, c = 10, 20, 30
print(f"A: {a}, B: {b}, C:{c}")

# asignacion encaenada
a = b = c = 10
print(f"A: {a}, B: {b}, C:{c}")

# intercambio de valores sin variable auxiliar
x, y = 5, 10
print(f"x = {x}, y = {y}")

# cambiamos los valores
x, y = y, x
print(f"x = {x}, y = {y}")

# recibir multiples valores por separado
nombre, apellido = input("Nombre y apellido separados por comas: ").split(",")
print(f"Nombre: {nombre.strip()}\nApellido: {apellido.strip()}")