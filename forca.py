
def jogar():
    print("**************************")
    print("Bem vindo ao game de forca")
    print("**************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        print("jogando...")

        chute = input("Digite qual letra? ")
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if chute.lower() == letra.lower():
                print("Encontrado a letra {} na posição {}".format(letra, index))
            index = index + 1



    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
