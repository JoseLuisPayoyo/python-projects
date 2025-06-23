nombre = input("Nombre: ")
edad = int(input("Edad: "))
salario = float(input("Salario: "))
isJefe = input("Eres jefe (Si/No): ")

# convertimos a boolean si es jefe o no
isJefe = isJefe.lower() == "si"

# imprimir valores
print("\nDatos del empleado")
print(f"Nombre: {nombre} \nEdad: {edad} \nSalario: {salario:.2f} \nEs jefe?: {isJefe}")