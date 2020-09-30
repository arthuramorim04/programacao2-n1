class N1:

    def aplicacao(self):
        print("iniciando a aplicacao")

        run = True

        while run:
            try:
                val = float(input("Informe uma nota de 0 até 10"))
                if val >= 0.0 and val <= 10.0:
                    print("valor correto")
                    run = False
                else:
                    print("Valor invalido")
            except:
                print("valor invalido")


N1().aplicacao()
