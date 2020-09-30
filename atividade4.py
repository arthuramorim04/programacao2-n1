# Decorator é um padrao pra indexar dinamicamente outras funções, classes e subclasses
#
#

import datetime


class N1:
    def calc(function):
        def calc():
            inicio = datetime.datetime.now()
            function()
            fim = datetime.datetime.now()
            tempo = fim - inicio
            print("\ntempo: ", tempo)

        return calc()

    @calc
    def inputNumeros(self):
        n1 = int(input("Digite o primeiro valor"))
        n2 = int(input("Digite o segundo valor"))
        n3 = int(input("Digite o terceiro valor"))
        n4 = int(input("Digite o quarto valor"))

        soma = n1 + n2 + n3 + n4
        print("\nsoma: ", soma)


N1().inputNumeros()
