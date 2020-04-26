class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


# Chamamos estas classes pequenas, cujos objetos nem precisam ser instanciados, de Mixins. Elas são bastante
# utilizadas em Python no caso de precisarmos compartilhar algum comportamento que não é o mais importante desta
# classe.
class Hipster:  # class MIXINS classes
    def __str__(self):
        return f'Hipster, {self.nome}.'


class Junior(Alura):
    pass


# aqui herdamos duas classes, e em caso de decisao de qual metodo usar, será usado o da esquerda para a direita
class Pleno(Caelum, Alura):
    pass


class Senior(Alura, Caelum, Hipster):
    pass


joao = Junior("joao")
joao.busca_perguntas_sem_resposta()
joao.mostrar_tarefas()

carlos = Pleno('carlos')
carlos.busca_perguntas_sem_resposta()
carlos.mostrar_tarefas()

luan = Senior('luan')
print(luan)
