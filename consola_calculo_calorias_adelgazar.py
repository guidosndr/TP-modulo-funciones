import calculadora_indices as calc

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su género (M/F): ")

valor_genero = 5 if genero.upper() == 'M' else -161

mensaje = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
print(mensaje)
