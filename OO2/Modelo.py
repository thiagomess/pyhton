# informações sobre classes abstratas https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos/task/42183

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

    # ao usuar o __str__ ele sabera formatar a string, seria algo como toString
    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self.likes} '


class Filme(Programa):  # Recebe a classe mae por parametro
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)  # sobescreve o metodo init da classe mae
        self.duracao = duracao

    # sobescreve da classe mae
    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Duração: {self.duracao} min - Likes: {self.likes} '


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    # sobescreve da classe mae
    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self.likes} '


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):  # Este método define algo que é iterável (Duck Typing)
        return self._programas[item]

    def __len__(self):  # Este metodo magico transforma o item em sized
        return len(self._programas)

    # No Python Data Model, todo objeto em Python pode se comportar de forma a ser compatível e mais próximo à
    #  linguagem, e de toda a ideia idiomática dela.


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
greys = Serie("grey's anatomy", 2004, 16)
panico = Filme("Panico", 1996, 100)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_like()
panico.dar_like()
demolidor.dar_like()
greys.dar_like()

filmes_e_series = [vingadores, greys, demolidor, panico]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')
print(f'Existe ou não? {demolidor in playlist_fim_de_semana}')

for programa in playlist_fim_de_semana:
    print(programa)
