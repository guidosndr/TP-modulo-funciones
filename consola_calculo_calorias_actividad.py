import calculadora_indices as calc

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su género (M/F): ")

print("Seleccione su nivel de actividad física:")
print("1 - Poco o ningún ejercicio")
print("2 - Ejercicio ligero (1-3 días a la semana)")
print("3 - Ejercicio moderado (3-5 días a la semana)")
print("4 - Deportista (6-7 días a la semana)")
print("5 - Atleta (entrena 2 veces por día)")

opcion = int(input("Opción: "))
valores = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
valor_actividad = valores.get(opcion, 1.2)

valor_genero = 5 if genero.upper() == 'M' else -161

resultado = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
print(f"Su gasto calórico en actividad es de: {resultado:.2f} calorías por día")
