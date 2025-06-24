# sistema que ofrezca descuentos dependiendo de lo que gasta y si es o no miembro
# 1. Si ha comprado mas de 1000 y es miembro, 10% descuento
# 2. Si solo es miembro, 5% descuento

print("*** Sistema de descuentos ***")
cantidad_gastada = float(input("Cual es el importe de tu cuenta: "))
isMiembro = input("Eres miembro de la tienda (si/no): ")
descuento = 0.0;

if isMiembro == "si":
    if cantidad_gastada >= 1000:
        descuento = 0.1
        print("\nFelicidades, has obtenido un descuento del 10%")
    else:
        descuento = 0.05
        print("\nFelicidades, has obtenido un descuento del 5%")
else:
    print("\nNo has obtenido un descuento")
    
print(f"Cantidad de la compra: ${cantidad_gastada}")
print(f"Cantidad de descuento: ${cantidad_gastada * descuento}")
print(f"Cantidad final de la compra: ${cantidad_gastada - (cantidad_gastada * descuento)}")
