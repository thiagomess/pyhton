import random


def jogar():
    imprime_mensagem_inicial()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = incializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 7

    while not enforcou and not acertou:
        chute = chute_jogador()

        if chute in palavra_secreta:
            altera_letra_pelo_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            tentativas -= 1
            desenha_forca(tentativas)

        acertou = "_" not in letras_acertadas  # caso nao tenha mais "_" seta true
        enforcou = tentativas == 0
        print(letras_acertadas)

    if acertou:
        print("Parabéns, você acertou a palavra!!")
    else:
        print("Poxa não foi desta vez, a palavra era {}".format(palavra_secreta))


def imprime_mensagem_inicial():
    print("**************************")
    print("Bem vindo ao game de forca")
    print("**************************")


def carrega_palavra_secreta(nome_arquivo="palavras.txt"):  # parametro é opcional
    # with open("palavras.txt") as arquivo: #Essa é outra forma de abrir o arquivo, mesmo caso haja exceção,
    # o arquivo é fechado automaticamente
    try:
        arquivo = open(nome_arquivo, "r")
        palavras = []

        for linha in arquivo:
            palavras.append(linha.strip())
        arquivo.close()
    except:
        palavras = ["maça", "banana", "morango", "laranja", "tangerina", "caqui", "pessego", "melancia"]
    random.shuffle(palavras)
    palavra_secreta = palavras[0].upper()

    return palavra_secreta


def incializa_letras_acertadas(palavra):
    return ["_" for letra in
            palavra]  # podemos criar um for dentro na inicializacao(list comprehension )


def chute_jogador():
    chute = input("Digite uma  letra? ")
    chute = chute.strip().upper()
    return chute


def altera_letra_pelo_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 0:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()

# List Comprehension para filtrar numeros pares em uma lista
# inteiros = [1,3,4,5,7,8,9]
# pares = [x for x in inteiros if x % 2 == 0]
