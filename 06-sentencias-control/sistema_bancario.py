
salir_sistema_txt = input("Desea salir (si/no): ")
salir_sistema = salir_sistema_txt.strip().lower() == "si"

if not salir_sistema:
    print("Continuamos en el sistema")
else:
    print("Saliendo del sistema...")