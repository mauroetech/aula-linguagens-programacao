peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Classificação do IMC
if imc < 18.5:
    classificacao = "Baixo peso"
elif 18.5 <= imc < 25:
    classificacao = "Peso normal"
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Seu IMC é {imc:.2f} e sua classificação é: {classificacao}")


