import calculadora_indices as calc

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su género (M/F): ")
es_hombre = genero.upper() == 'M'
valor_genero = 10.8 if es_hombre else 0
porcentaje = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
print(f"Su porcentaje de grasa corporal es: {porcentaje:.2f}%")
