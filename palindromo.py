texto = input("Digite um texto: ").lower()  # Converter para minúsculas para ignorar diferenças de maiúsculas/minúsculas
texto = texto.replace(" ", "")  # Remover espaços
texto = texto.replace(",", "")  # Remover vírgulas
texto = texto.replace(".", "")  # Remover pontos

# Inverter o texto
texto_invertido = texto[::-1]

if texto == texto_invertido:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
