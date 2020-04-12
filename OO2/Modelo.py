class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property  # cria um getter
    def nome(self):
        return self.__nome.title()

    @nome.setter  # cria um setter
    def nome(self, nome):
        self.__nome = nome

    @property  # cria um getter
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property  # cria um getter
    def nome(self):
        return self.__nome.title()

    @nome.setter  # cria um setter
    def nome(self, nome):
        self.__nome = nome

    @property  # cria um getter
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1




vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes} ')

greys = Serie("grey's anatomy", 2004, 16)
greys.dar_like()
print(f'Nome: {greys.nome} - Ano: {greys.ano} - Temporadas: {greys.temporadas} - Likes: {greys.likes}')


