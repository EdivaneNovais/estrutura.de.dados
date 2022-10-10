import re


def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

print(fatorial(6))
print(fatorial(3))
print(fatorial(4))

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente -1)

print(potencia(2, 4))