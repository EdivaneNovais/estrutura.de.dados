from ast import Return
import numpy as np


class Pilha:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = np.chararray(self.capacidade, unicode=True)#array de chars

    def __pilha_cheia(self):#so vai ter acesso ao topo da pilha
        if self.topo == self.capacidade - 1:
            return True
        else:
            return False

    def pilha_vazia(self):
        if self.topo == - 1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print('A pilha está cheia')
        else:
            self.topo += 1#incrementa o topo
            self.valores[self.topo] = valor

    def desempilhar(self):# não recebe parametro pois sempre vai desempilhar o topo
        if self.pilha_vazia():
            print('A pilha está vazia')
            Return -1
        else:
            valor = self.valores[self.topo]
            self.topo -= 1#decrementa o topo
            return valor

    def ver_topo(self):
        if self.topo != -1:#quando a pilha esta vazia
            return self.valores[self.topo]
        else:
            return - 1

expressao = str(input('Digite uma expressão: '))
pilha = Pilha(len(expressao))

for i in range(len(expressao)):
    caracter_fechamento = expressao[i]
    if caracter_fechamento == '{' or caracter_fechamento == '[' or caracter_fechamento == '(':
        pilha.empilhar(caracter_fechamento)
    elif caracter_fechamento == '}' or caracter_fechamento == ']' or caracter_fechamento == ')':
        if not pilha.pilha_vazia():
            caracter_abertura = str(pilha.desempilhar())
            if (caracter_fechamento == '}' and caracter_abertura != '{') or (caracter_fechamento == ']' and caracter_abertura != '[') or (caracter_fechamento == ')' and caracter_abertura != '('):
                print(f'Erro: {caracter_fechamento}, na posição, {i}')
                break
            else:
                print(f'Erro: {caracter_fechamento}, na posição,  {i}')
if not pilha.pilha_vazia():
    print('Erro!')
