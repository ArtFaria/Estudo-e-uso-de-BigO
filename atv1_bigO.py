import time
import random

def soma(lista):
    total = 0                 # acumula a soma
    for x in lista:           # percorre cada elemento (n passos)
        total += x            # adiciona ao acumulador (O(1))
    return total              # devolve a soma final

def busca(lista, x):
    for v in lista:           # varre a lista do início ao fim
        if v == x:            # comparação O(1)
            return True       # achou → encerra cedo (melhor caso O(1))
    return False              # não achou após percorrer tudo


def busca_binaria(lista, x):
    i, j = 0, len(lista) - 1      # intervalo de busca fechado [i, j]
    while i <= j:                  # enquanto houver intervalo válido
        m = (i + j) // 2           # meio (inteiro)
        if lista[m] == x:          # acerto
            return True
        if lista[m] < x:           # x está à direita do meio
            i = m + 1
        else:                      # x está à esquerda do meio
            j = m - 1
    return False                   # saiu do laço → não existe


def contar_ocorrencias(lista, x):
    cont = 0                    # contador
    for v in lista:             # percorre todos os elementos
        if v == x:              # compara (O(1))
            cont += 1           # soma 1 se igual
    return cont                 # total de ocorrências


def medir_tempo(func,busca_binaria):
    inicio = time.time()            # timestamp inicial
    resultado = func(busca_binaria)         # executa a função
    fim = time.time()               # timestamp final
    return resultado, fim - inicio  # devolve resultado + duração (segundos)
    print("Tempo de execução:", duracao, "segundos")



lista1 = [random.randint(0, 1000) for _ in range(10**3)]  # 1.000
lista2 = [random.randint(0, 1000) for _ in range(10**4)]  # 10.000
lista3 = [random.randint(0, 1000) for _ in range(10**5)]  # 100.000
