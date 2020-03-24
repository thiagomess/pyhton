import random


def jogar():
    print("**************************")
    print("Bem vindo ao game de forca")
    print("**************************")

    palavras = ["maça", "banana", "morango", "laranja", "tangerina", "caqui", "pessego", "melancia"]
    random.shuffle(palavras)

    palavra_secreta = palavras[0].upper()
    letras_acertadas = ["_" for letra in
                        palavra_secreta]  # podemos criar um for dentro na inicializacao(list comprehension )

    enforcou = False
    acertou = False
    tentativas = 6

    print(letras_acertadas)
    while not enforcou and not acertou:
        chute = input("Digite uma  letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas -= 1
            print("Você errou, restam {} tentativas".format(tentativas))

        acertou = "_" not in letras_acertadas  # caso nao tenha mais "_" seta true
        enforcou = tentativas == 0
        print(letras_acertadas)

    if acertou:
        print("Parabens, você acertou a palavra!!")
    else:
        print("Não foi dessa vez, tente novamente")

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()

# List Comprehension para filtrar numeros pares em uma lista
# inteiros = [1,3,4,5,7,8,9]
# pares = [x for x in inteiros if x % 2 == 0]
