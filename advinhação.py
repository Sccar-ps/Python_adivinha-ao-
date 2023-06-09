def jogar_advinhaçao
import random

print("****************************************")
print("Bem vindo ao jogo de Advinhação", end="!")
print("****************************************")

numero_secreto = random.randrange(101)
total_tentativa = 3
rodada = 1

for rodada in range(1, total_tentativa + 1):
    print("Tentativa {} : {}".format(rodada, total_tentativa))

    chute_str = input("Digite um número: ")
 if (chute_str > 110):
     print("O numero é menor q 111!")
  continue

    chute_str = int(chute_str)
    x = (numero_secreto + chute_str) * 2
    y = (numero_secreto - chute_str) * 3
    print("Você digitou", chute_str)

    if numero_secreto == chute_str:
        print("!------- VOCE GANHOU -------!")
        break
    else:
        print("Você errou")
        if chute_str >= numero_secreto:
            print("Soma do erro mais o numero x2 é", x)
            print("Tente novamente")
            print("--------------------------------")
        else:
            print("A diferença x 3 é", y)
            print("Tente novamente")
            print("--------------------------------")
    rodada = rodada + 1
