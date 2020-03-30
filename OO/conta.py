class Conta:
    # forma de chamar essa classe no console: from OO.conta import Conta

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

    # método privado
    def __verifica_valor_saque(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    @property  # cria um getter
    def saldo(self):
        return self.__saldo

    @property  # cria um getter
    def titular(self):
        return self.__titular

    @property  # cria um getter
    def limite(self):
        return self.__limite

    @limite.setter  # cria um setter e obrigatoriamente deve ter um @property com esse nome,
    def limite(self, limite):
        self.__limite = limite

    # Método estatico
    @staticmethod
    def codigo_banco():
        return "0001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237', 'Itaú': '341'}
