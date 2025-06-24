# se pide nombre y pasos en el dia

META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04

nombre = input("Cual es tu nombre: ")
pasos = int(input("Pasos hoy: "))

calorias_quemadas = CALORIAS_POR_PASO * pasos

if pasos >= META_PASOS_DIARIOS:
    print(f"\nHas hecho {pasos}, y has cumplido la meta de {META_PASOS_DIARIOS} pasos")
    print(f"Has quemado {calorias_quemadas} kcal")
else:
    print(f"\nHas hecho {pasos}, y no has cumplido la meta de {META_PASOS_DIARIOS} pasos")
    print(f"Has quemado {calorias_quemadas} kcal")