import numpy as np

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)


class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def insere_inicio(self, valor):
        novo = No(valor)#cria o objeto
        novo.proximo = self.primeiro#proximo aponta para primeiro
        self.primeiro = novo#cabeca da lista que é o primeiro aponta para o novo

    def mostrar(self):
        if self.primeiro == None:
            print('A lista está vazia')
            return None

        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

    def pesquisa(self, valor):
        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                atual = atual.proximo
            return atual

    def excluir_inicio(self):
        if self.primeiro == None:
            print('A lista está vazia')
            return None
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo#cabeca da lista vai recebebr o proximo que passa a ser a cabeca da lista
        return temp

    def excluir_posicao(self, valor):
        if self.primeiro == None:
            print('A lista está vazia')
            return None

        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                anterior = atual
                atual = atual.proximo
        if atual == self.primeiro:#se for o primeiro elemento da lista
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo#
        return atual

no = No(2)
print(no.mostra_no())
print()
lista = ListaEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
print(lista.mostrar())
print(lista.primeiro.proximo)#endereço de memoria
print(lista.primeiro.mostra_no())
lista.excluir_inicio()
print(lista.mostrar())
print()
pesquisa = lista.pesquisa(3)
print(pesquisa.valor)
print()
lista.excluir_posicao(3)
print(lista.mostrar())