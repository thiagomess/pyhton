class Conta:

    # Construtor e inicialização dos parametros
    # self é a referência que sabe encontrar o objeto construído em memória.
    # Colocando o parametro "limite = 1000.0", o valor fica default
    # None é igual a null no python
    def __init__(self, numero, titular, saldo, limite=1000.0):
        print("Construindo objeto")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("O {} possuí saldo de R$ {} e limite especial de R$ {}".format(self.titular, self.saldo, self.limite))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        total_disponivel = self.saldo + self.limite
        if valor <= total_disponivel:
            self.saldo -= valor
        else:
            print("O valor do saque é superior o valor disponível")
