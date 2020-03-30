
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property # cria um getter
    def nome(self):
        return self.__nome.title()

    @nome.setter  # cria um setter
    def nome(self):
        return self.__nome

