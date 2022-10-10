import numpy as np

def bubble_sort(vetor):
    n = len(vetor)
    for i in range(n):#percorre todo o tamanho do vetor
        for j in range(0, n - i - 1):
            if vetor[j] > vetor[j + 1]:
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp
    return vetor

print(bubble_sort(np.array([15, 34, 8, 3])))

def selection_sort(vetor):
    n = len(vetor)

    for i in range(n):
        id_minimo = i
        for j in range(i + 1, n):
            if vetor[id_minimo] > vetor[j]:
                id_minimo = j
        temp = vetor[i]
        vetor[i] = vetor[id_minimo]
        vetor[id_minimo] = temp

    return vetor

print(selection_sort(np.array([15, 34, 8, 3])))


def insertion_sort(vetor):
    n = len(vetor)
    for i in range(1, n):#comeca na posicao 1 pois ele comeca comprando o segundo elemento com o primeiro
        marcado = vetor[i]
        j = i - 1
        while j >= 0 and marcado < vetor[j]:#procura o menor
            vetor[j + 1] = vetor[j]#copia da posicao posterior que recebe a posicao atual
            j -= 1
        vetor[j + 1] = marcado
    return vetor

print(insertion_sort(np.array([15, 34, 8, 3])))

def shell_sort(vetor):
    intervalo = len(vetor) // 2
    while intervalo > 0:
        for i in range(intervalo, len(vetor)):
            temp = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo
            vetor[j] = temp
        intervalo //= 2

    return vetor

print(shell_sort(np.array([15, 34, 8, 3])))


def merge_sort(vetor):
    if len(vetor) > 1:
        divisao = len(vetor) // 2
        esquerda = vetor[:divisao].copy()
        direita = vetor[divisao:].copy()

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1
    return vetor


print(merge_sort(np.array([15, 34, 8, 3])))

#algoritmo quick sort
def particao(vetor, inicio, final):
    pivo = vetor[final]
    i = inicio - 1

    for j in range(inicio, final):
        if vetor[j] <= pivo:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
        vetor[i + 1], vetor[final] = vetor[final], vetor[i + 1]
        return i + 1

def quick_sort(vetor, inicio, final):
    if inicio < final:
        posicao = particao(vetor, inicio, final)
        #esquerda
        quick_sort(vetor, inicio, posicao - 1)
        #direita
        quick_sort(vetor, posicao + 1, final)
    return vetor

vetor = (np.array([15, 34, 8, 3]))
quick_sort(vetor, 0, len(vetor) - 1)
#bubble sorte tem como parâmetro um vetor nao ordenado, preciso saber a quantidade de elementos no vetor
#preciso de duas estrutura de repeticao para percorrer os elementos
#um for que ira percorrer os elementos internamente, ate os que ja foram ordenados
#um for que vai percorrer os elementos que sobraram e nao foram ordenados
#tres passos para relaizar a troca