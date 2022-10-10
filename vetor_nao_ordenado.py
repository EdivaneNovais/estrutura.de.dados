import numpy as np

class VetorNaoOrdenado:
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
        if self.ultima_posicao == self.capacidade -1:
            print('Capacidade máxima atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):#percorre o vetor inteiro
            if valor == self.valores[i]:
                return i
        return -1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1

vetor = VetorNaoOrdenado(7)
vetor.insere(2)
vetor.insere(8)
vetor.insere(3)
vetor.insere(6)
vetor.insere(5)
vetor.imprime()
print()


print(vetor.pesquisar(5))
print(vetor.pesquisar(7))


print()
vetor.excluir(5)
vetor.imprime()