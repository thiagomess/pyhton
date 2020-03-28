
class Data:

    def __init__(self, dia=1, mes=1, ano=9999):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    # Doc Format https://mkaz.blog/code/python-string-format-cookbook/
    def formatada(self):
        # print("{}/{}/{}".format(self.dia, self.mes, self.ano))
        print(f"{self.dia:02d}/{self.mes:02d}/{self.ano}") # novo jeito de fazer o format > V3.7

