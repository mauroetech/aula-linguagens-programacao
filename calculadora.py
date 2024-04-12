Faça um programa em pythvalor1 = 0  # Inicializa valor1 com 0 para entrar no loop
while valor1 != -1:
    valor1 = int(input("Digite o primeiro valor (ou -1 para sair): "))
    
    if valor1 == -1:
        break
    
    operador = input("Digite o operador (+, -, *, /): ")
    if operador == '-1':
        break
    valor2 = int(input("Digite o segundo valor: "))
    if valor2 == -1:
        break
    if operador == "+":
        soma = valor1 + valor2
        print("Resultado da Soma:", soma)
    elif operador == "-":
        subtracao = valor1 - valor2
        print("Resultado da Subtracao:", subtracao)
    elif operador == "*":
        multiplicacao = valor1 * valor2
        print("Resultado da multiplicacao:", multiplicacao)
    elif operador == "/":
        if valor2 == 0:
            print("Erro! Divisão por zero.")
        else:
            divisao = valor1 / valor2
            print("Resultado da divisao:", divisao)
    else:
        print("Operador inválido. Tente novamente.")
