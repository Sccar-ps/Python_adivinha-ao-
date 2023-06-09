import adivinhacao
import forca
print("Bem vindo ao Jogo")


print("*********************************")
print("          Escolha um jogo")
print("*********************************")

print("1- Forca  2-Advinhação")
escolha_jogo = int(input("-->"))

if escolha_jogo == 1:
    forca.jogar()
elif escolha_jogo >= 2  :
    adivinhacao.jogar()