import aidivhacao
import forca
print("**************************")
print("****Escolha o seu jogo****")
print("**************************")


print("{1} Forca {2} Advinhacao")

jogo = int(input("Qual jogo? "))

if jogo == 1:
    print("Você escolheu o jogo da Forca")
    forca.jogar()
elif jogo == 2:
    print("Você escolheu o jogo da Advinhação")
    aidivhacao.jogar()