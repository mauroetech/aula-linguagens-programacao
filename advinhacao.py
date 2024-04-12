import random

numero_secreto = random.randint(1, 10)
tentativas = 3

while tentativas > 0:
    palpite = int(input("Adivinhe o n�mero entre 1 e 10: "))
    
    if palpite == numero_secreto:
        print("Parab�ns! Voc� acertou.")
        break
    elif palpite < numero_secreto:
        print("Seu palpite est� muito baixo.")
    else:
        print("Seu palpite est� muito alto.")
    
    tentativas -= 1

if tentativas == 0:
    print("Fim do jogo. O n�mero secreto era:", numero_secreto)


