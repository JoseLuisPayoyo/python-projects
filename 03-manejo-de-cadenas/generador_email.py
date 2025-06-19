# Crea un programa para generar un email a partir de los siguentes datos:
# - Nombre
# - Empresa
# - Dominio
# unir todo y mostrar

print("*** Generador de Email *** ")
nombre = input("Nombre: ").lower().strip().replace(" ", ".")
print(f"Nombre de usuario normalizado: {nombre}")

empresa = input("Empresa: ").lower().replace(" ", "")

dominio = input("Dominio: ").lower()

email = f"{nombre}@{empresa}{dominio}"
print(email)

