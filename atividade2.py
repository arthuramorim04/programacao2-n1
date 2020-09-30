listFuncionarios = []

class Funcionario:

    def __init__(self, nome, idade, salario, cargo):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.cargo = cargo

class N1:

    def printList(self, list):

        for funcionario in list:
            print("Funcionario")
            print("Nome: ", funcionario.nome)
            print("Idade: ", funcionario.idade)
            print("Cargo: ", funcionario.cargo)
            print("Salario: ", funcionario.salario)


    def cadastra(self):
        nome = input("Nome:")
        idade = int(input("idade:"))
        salario = float(input("salario:"))
        cargo = ''

        run = True

        while run:
            opc = input("\nEscolha o cargo do funcionario: \n1.Programador\n2.Analista")

            if opc == '1':
                salario = salario + 20
                cargo = "Programador"
                run = False
            else:
                if opc == '2':
                    salario = salario + 30
                    cargo = "Analista"
                    run = False
                else:
                    print("\nOpção invalida")

        funcionario = Funcionario(nome,idade,salario,cargo)

        listFuncionarios.append(funcionario)


    def aplicacao(self):
        print("iniciando aplicacao")
        n2Class = N1()
        run = True

        while run:
            n2Class.cadastra()
            opc = input("Cadastrar outro? <S> ou <N>")
            if opc.upper() != 'S':
                run = False

        n2Class.printList(listFuncionarios)


N1().aplicacao()
