class ModelEx1:
    def __init__(self, month, num):
        self.month = month
        self.num = num


class ModelEx1P2:
    def __init__(self, model1, media):
        self.model1 = model1
        self.num = media


class N1:

    def bubble_sort(self, lista):
        elements = len(lista) - 1
        ordenado = False
        while not ordenado:
            ordenado = True
            for i in range(elements):
                obj1 = lista[i]
                obj2 = lista[i + 1]
                if obj1.num > obj2.num:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    ordenado = False
        return lista

    def calc_media(self, list):

        n1Class = N1()

        sizeList = len(list)
        print(sizeList)
        media = 0
        index = 0
        for item in list:
            media = media + item.num

        media = media / len(list)
        print("Media: " + str(media))

        min = list[0]
        max = list[sizeList - 1]

        print("Minimo\n mes:" + str(min.month) + "\nnum: " + str(min.num))
        print("Maximo\n mes:" + str(max.month) + "\nnum: " + str(max.num))

        listAux = []

        for item in list:
            valor = item.num - media
            print(abs(valor))
            modelAux = ModelEx1P2(item, abs(valor))
            listAux.append(modelAux)

        listOrdernada = n1Class.bubble_sort(listAux)

        obj = listOrdernada[0]
        print("\n\nValor mais proximo da média")
        print("Mes" + str(obj.model1.month))
        print("Num" + str(obj.model1.num))

    def printList(self, list):
        var = list

        for obj in var:
            print(obj.month)
            print(obj.num)

    def exercicio_1(self):
        n1Class = N1()
        list = []
        run = True
        while run == True:
            month = input("Informe o mes: ")
            num = int(input("Informe a quantidade de rebeldes presos"))

            obj = ModelEx1(month, num)
            list.append(obj)

            opc = input("Deseja inserir um novo registro? <S> ou <N> ")

            if opc.upper() != 'S':
                run = False

        for item in list:
            print("-" * 30)
            print("mes:" + str(item.month))
            print("quantidade: " + str(item.num))
            print("-" * 30)

        newList = n1Class.bubble_sort(list)

        for item in newList:
            print("-" * 30)
            print("mes:" + str(item.month))
            print("quantidade: " + str(item.num))
            print("-" * 30)

        n1Class.calc_media(newList)

    def aplicacao(self):
        print("iniciando aplicacao")
        n1Class = N1()
        n1Class.exercicio_1()


N1().aplicacao()
