class Conta:

    # Construtor e inicialização dos parametros
    # self é a referência que sabe encontrar o objeto construído em memória.
    # Colocando o parametro "limite = 1000.0", o valor fica default
    # None é igual a null no python
    def __init__(self, numero, titular, saldo, limite=1000.0):
        print("Construindo objeto")
        self.__numero = numero  # com __ o atributo se torna privado
        self.__titular = titular  # com __ o atributo se torna privado
        self.__saldo = saldo  # com __ o atributo se torna privado
        self.__limite = limite  # com __ o atributo se torna privado

    def extrato(self):
        print(
            "O {} possuí saldo de R$ {} e limite especial de R$ {}".format(self.__titular, self.__saldo, self.__limite))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if self.__verifica_valor_saque(valor):
            self.__saldo -= valor
        else:
            print("O valor do saque é superior ao valor disponível")

    def transfere(self, valor, destino):
        if self.__verifica_valor_saque(valor):
            self.saca(valor)
            destino.deposita(valor)
        else:
            print("O valor da transferência é superior ao valor disponível")


    def __verifica_valor_saque(self, valor):
        total_disponivel = self.__saldo + self.__limite
        if valor <= total_disponivel:
            return True
        else:
            return False
