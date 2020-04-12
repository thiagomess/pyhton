class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0

    @property  # cria um getter
    def nome(self):
        return self._nome.title()

    @nome.setter  # cria um setter
    def nome(self, nome):
        self._nome = nome

    @property  # cria um getter
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1


class Filme(Programa): # Recebe a classe mae por parametro
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # sobescreve o metodo init da classe mae
        self.duracao = duracao

    def imprime(self):
        print(f'Nome: {self.nome} - Ano: {self.ano} - Duração: {self.duracao} - Likes: {self.likes} ')


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f'Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self.likes} ')


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
vingadores.imprime()

greys = Serie("grey's anatomy", 2004, 16)
greys.dar_like()
greys.imprime()
