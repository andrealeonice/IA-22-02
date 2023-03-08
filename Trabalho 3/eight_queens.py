from random import random, randint


def evaluate(individual):
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 10.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """
    nAttack = 0
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            if individual[i] == individual[j]:
                nAttack += 1
            elif abs(individual[i] - individual[j]) == abs(i - j):
                nAttack += 1
    return nAttack


def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """
    # raise NotImplementedError  # substituir pelo seu codigo
    allConflicts = []

    for i in participants:
        allConflicts.append(evaluate(i))
    x = allConflicts.index(min(allConflicts))
    return participants[x]


def crossover(parent1, parent2, index):
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:list
    :param index:int
    :return:list,list
    """
    # raise NotImplementedError  # substituir pelo seu codigo
    newParent1 = parent1[0:index] + parent2[index:]
    newParent2 = parent2[0:index] + parent1[index:]

    return newParent1, newParent2


def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    # raise NotImplementedError  # substituir pelo seu codigo
    if random() < m:
        individual[randint(0, 7)] = randint(1, 8)

    return individual


def populate(n):
    population = []
    for i in range(n):
        aux = []
        for j in range(8):
            aux.append(randint(1, 8))
        population.append(aux)

    return population


def elitism(p, e):
    aux = p.copy()
    for i in range(e):
        nP = tournament(aux)
        aux.remove(tournament(aux))
    return nP


def participants(p, n, k):
    selected = []
    for i in range(k):
        selected.append(p[randint(0, n - 1)])
    return selected


def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:int - número de indivíduos no elitismo
    :return:list - melhor individuo encontrado
    """
    # raise NotImplementedError  # substituir pelo seu codigo
    p = populate(n)
    pL = []
    for gen in range(g):
        pL.append(elitism(p, e))

        while (n > len(pL)):
            p1 = tournament(participants(p, n, k))
            p2 = tournament(participants(p, n, k))
            o1, o2 = crossover(p1, p2, randint(0, 7))
            pL.append(mutate(o1, m))
            pL.append(mutate(o2, m))

#       p = pL.copy()
    #check(p)
    return tournament(p)

#def check (p):
#    conflicts = []
#    for i in p:
#        conflicts.append(evaluate(i))
#    print(min(conflicts), max(conflicts), sum(conflicts)/len(p))




