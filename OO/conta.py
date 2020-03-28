class Conta:

    # Construtor e inicialização dos parametros
    # self é a referência que sabe encontrar o objeto construído em memória.
    # Colocando o parametro "limite = 1000.0", o valor fica default
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        print("Construindo objeto")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
