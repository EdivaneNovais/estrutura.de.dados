import numpy as np


class Pilha:

    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __pilha_cheia(self):#so vai ter acesso ao topo da pilha
        if self.__topo == self.__capacidade - 1:
            return True
        else:
            return False

    def __pilha_vazia(self):
        if self.__topo == - 1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print('A pilha está cheia')
        else:
            self.__topo += 1#incrementa o topo
            self.__valores[self.__topo] = valor

    def desempilhar(self):# não recebe parametro pois sempre vai desempilhar o topo
        if self.__pilha_vazia():
            print('A pilha está vazia')
        else:
            self.__topo -= 1#decrementa o topo

    def ver_topo(self):
        if self.__topo != -1:#quando a pilha esta vazia
            return self.__valores[self.__topo]
        else:
            return - 1


pilha = Pilha(5)
print(pilha.ver_topo())

pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
pilha.empilhar(1)
pilha.empilhar(6)
print(pilha.ver_topo())
print()

pilha.desempilhar()
pilha.desempilhar()
print(pilha.ver_topo())
