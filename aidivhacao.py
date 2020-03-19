import random

print("*******************************")
print("Bem vindo ao game de advinhação")
print("*******************************")

numero_secreto = random.randrange(1, 101) #gera um numero inteiro de 1 a 100. Iniciando em 1
total_de_tentativas = 3

print(numero_secreto)
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas)) # usando o format, popula o {} com o valor https://docs.python.org/3/library/string.html#formatexamples
    # print(f"Tentativa {rodada} de {total_de_tentativas}")  #caso adicione o f fora da string é possivel utilizar assim
    chute_str = input("Digite o seu número: ")
    chute = int(chute_str)
    print("Você digitou: ", chute)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100")
        continue #pula o laço para a proxima iteração

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou")
        break
    else:
        if maior:
            print("Você errou! O seu chute foi maior do que o número secreto")
        elif menor:
            print("Você errou! O seu chute foi menor do que o número secreto")

print("Fim do jogo")
