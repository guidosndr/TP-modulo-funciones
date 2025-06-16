# FUNCIONES PARA CALCULADORA DE INDICES CORPORALES:


def calcular_IMC(peso: float, altura: float):
    return peso / (altura ** 2)



def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float):
    imc = calcular_IMC(peso, altura)
    return 1.2 * imc + 0.23 * edad - 5.4 - valor_genero



def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: int):
    return 10 * peso + 6.25 * altura * 100 - 5 * edad + valor_genero 



def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: int, valor_actividad: float):
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    return tmb * valor_actividad



def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: int):
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    inferior = tmb * 0.80
    superior = tmb * 0.85
    return f"Para adelgazar es recomendado que consumas entre: {inferior:.2f} y {superior:.2f} calorías al día."
