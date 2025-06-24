print("*** Sentencia elif ***")

edad = int(input("Tu edad: "))

if edad < 13:
    print(f"Eres un niño. Tienes {edad} años")  
elif 13 <= edad < 18:
    print(f"Eres un adolescentes. Tienes {edad} años") 
else:
    print(f"Eres mayor de edad. Tienes {edad} años")  