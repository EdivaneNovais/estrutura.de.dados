import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor esta vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' _ ', self.valores[i])

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):#percorre o vetor inteiro
            posicao = i
            if self.valores[i] > valor:#quer dizer que encontramos a posicao
                break
            if i == self.ultima_posicao:
                posicao = i + 1#vai percorrer todo o vetor e adicionar mais um na ultima posicao

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]#vai remanejar os elementos
            x -= 1

        self.valores[posicao] = valor #vai inserir o valor na posicao
        self.ultima_posicao += 1

    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:#vai parar quando encontrar o valor maior que esta procurando
                return -1
            if self.valores[i] == valor:
                return i
            if i == self.ultima_posicao:
                return -1

    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        while True:
            posicao_atual = int((limite_inferior + limite_superior) / 2)#busca do indice precisa ser inteiro
            #se achou na primeira tentativa
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            #se nao achou
            elif limite_inferior > limite_superior:
                return -1
            #divide os limites
            else:
                #limite inferior
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                #limite superior
                else:
                    limite_superior = posicao_atual - 1


    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]#remanejamento dos valores
            self.ultima_posicao -= 1

# vetor = VetorOrdenado(10)
# vetor.imprime()

# vetor.insere(6)
# vetor.insere(4)
# vetor.insere(3)
# vetor.insere(5)
# vetor.insere(8)

# vetor.imprime()
# print()
# print(vetor.pesquisa_linear(3))
# print(vetor.pesquisa_linear(2))
# print(vetor.pesquisa_linear(9))
# print()

# # vetor.excluir(3)
# # print(vetor.excluir(9))

# vetor.imprime()

vetor = VetorOrdenado(10)


vetor.insere(6)
vetor.insere(4)
vetor.insere(3)
vetor.insere(5)
vetor.insere(8)

vetor.imprime()

print()
print(vetor.pesquisa_binaria(5))
print(vetor.pesquisa_binaria(4))
print(vetor.pesquisa_binaria(9))
print()