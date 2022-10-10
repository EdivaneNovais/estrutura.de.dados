import timeit
import time


for i in range(5):
    print('Recursão')


def recursao(i):
    print('Recursão')
    i += 1
    if i == 5:
        return#para a recursão
    else:
        return recursao(i)

print(10* '-')
recursao(0)

def soma1(n):
    soma = 0
    for i in range(n + 1):#range comeca no 0
        soma += i
    return soma

print(10* '-')
print(soma1(5))

def soma2(n):
    if n == 0:
        return 0
    return n + soma2(n - 1)

print(soma2(5))
