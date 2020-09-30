alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


class N1:

    def decodifica(self, text):
        print("decodificando")
        result = ''
        var = text.split(',')
        for char in var:
            var = char.strip()
            if var == '0':
                result = result + ' '
            else:
                try:
                    index = int(char)
                    char = alfabeto[index - 1]
                    result = result + char
                except:
                    print("valor invalido")
        print(result)

    def aplicacao(self):
        print("iniciando aplicao")
        text = input("Digite sua mensagem codificada separando os valores por (',') : ")
        N1().decodifica(text)


N1().aplicacao()
