def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return f"IMC: {imc:.2f} - Baixo peso"
    elif imc < 25:
        return f"IMC: {imc:.2f} - Peso adequado"
    elif imc < 30:
        return f"IMC: {imc:.2f} - Sobrepeso"
    elif imc < 35:
        return f"IMC: {imc:.2f} - Obesidade grau I"
    elif imc < 40:
        return f"IMC: {imc:.2f} - Obesidade grau II"
    else:
        return f"IMC: {imc:.2f} - Obesidade grau III"

try:
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    resultado = calcular_imc(peso, altura)
    print(resultado)
except ValueError:
    print("Por favor, digite valores numéricos válidos.")
