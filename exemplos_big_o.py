lista = [1, 2, 3, 4,5 ]

def constante(n):
    print(n[0])

def linear(n):
    for i in n:
        print(i)

def quadatic(n):
    for i in n:
        for j in n:
            print(i, j)

def combination(n):
    print(n[0])
    for i in range(5):
        print('test', i)
    for i in n:
        print(i)
    for i in n:
        print(i)

constante(lista)
linear(lista)
quadatic(lista)
combination(lista)