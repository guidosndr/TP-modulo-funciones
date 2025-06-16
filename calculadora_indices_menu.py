import os

while True:
    print("\n¿Qué desea calcular?")
    print("1 - IMC")
    print("2 - Porcentaje de grasa corporal")
    print("3 - Calorías en reposo")
    print("4 - Calorías con actividad física")
    print("5 - Calorías para adelgazar")
    print("0 - Salir")

    opcion = input("Ingrese una opción (0-5): ")
    if opcion == "1":
        os.system("python consola_calculo_imc.py")
    elif opcion == "2":
        os.system("python consola_calculo_porcentaje_grasa.py")
    elif opcion == "3":
        os.system("python consola_calculo_calorias_reposo.py")
    elif opcion == "4":
        os.system("python consola_calculo_calorias_actividad.py")
    elif opcion == "5":
        os.system("python consola_calculo_calorias_adelgazar.py")
    elif opcion == "0":
        print("Programa finalizado")
        break
    else:
        print("Opción no válida. Por favor, intentá de nuevo.")
