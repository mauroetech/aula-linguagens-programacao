texto = input("Digite um texto: ").lower()  # Converter para min�sculas para ignorar diferen�as de mai�sculas/min�sculas
texto = texto.replace(" ", "")  # Remover espa�os
texto = texto.replace(",", "")  # Remover v�rgulas
texto = texto.replace(".", "")  # Remover pontos

# Inverter o texto
texto_invertido = texto[::-1]

if texto == texto_invertido:
    print("� um pal�ndromo!")
else:
    print("N�o � um pal�ndromo.")
