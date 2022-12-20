from enum import Enum

SOLUCAO = "12345678_"


class Acao(Enum):
    CIMA = 1
    BAIXO = 2
    DIREITA = 3
    ESQUERDA = 4


class Nodo:
    def __init__(self, estado: str, pai, acao: Acao, custo: int):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

    def expande(self):
        raise NotImplementedError

    def printAllProperties(self):
        print("#####################")
        print(self.estado)
        print(self.pai)
        print(self.acao)
        print(self.custo)


def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """

    posicao_branco = estado.find('_')
    if posicao_branco < 0:
        raise Exception("Estado inválido")

    acoes_possiveis = []
    if posicao_branco > 2:
        acoes_possiveis.append(
            (Acao.CIMA, obtemEstadoResultante(estado, Acao.CIMA)))
    if posicao_branco < 6:
        acoes_possiveis.append(
            (Acao.BAIXO, obtemEstadoResultante(estado, Acao.BAIXO)))
    if posicao_branco not in [0, 3, 6]:
        acoes_possiveis.append(
            (Acao.ESQUERDA, obtemEstadoResultante(estado, Acao.ESQUERDA)))
    if posicao_branco not in [2, 5, 8]:
        acoes_possiveis.append(
            (Acao.DIREITA, obtemEstadoResultante(estado, Acao.DIREITA)))

    return acoes_possiveis


def obtemEstadoResultante(estado: str, acao: Acao):
    '''Retorna o estado resultante ao executar a ação  especificada.'''
    # Converte string em lista p/ que seja possível trocar caracteres de lugar
    lista_estado = list(estado)
    pos_atual_branco = estado.index('_')
    # Troca o branco de lugar com a nova posição que deve assumir
    if acao == Acao.CIMA:
        nova_pos_branco = pos_atual_branco - 3
        lista_estado[pos_atual_branco], lista_estado[nova_pos_branco] = estado[nova_pos_branco], '_'
    elif acao == Acao.BAIXO:
        nova_pos_branco = pos_atual_branco + 3
        lista_estado[pos_atual_branco], lista_estado[nova_pos_branco] = estado[nova_pos_branco], '_'
    elif acao == Acao.ESQUERDA:
        nova_pos_branco = pos_atual_branco - 1
        lista_estado[pos_atual_branco], lista_estado[nova_pos_branco] = estado[nova_pos_branco], '_'
    elif acao == Acao.DIREITA:
        nova_pos_branco = pos_atual_branco + 1
        lista_estado[pos_atual_branco], lista_estado[nova_pos_branco] = estado[nova_pos_branco], '_'
    else:
        raise Exception("Acao invalida")

    # Converte novamente em string e a retorna
    return "".join(lista_estado)


def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    sucessores = sucessor(nodo.estado)
    nodos = []
    for estado, acao in sucessores:
        novoFilho = Nodo(acao, nodo, estado, nodo.custo + 1)
        nodos.append(novoFilho)
    return nodos


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    movimentos = []
    solucao = busca_grafo(estado, 'bfs')
    if solucao is not None:
        for nodo in solucao:
            movimentos.append(nodo.acao)
        print(movimentos)
        return movimentos
    return None


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    movimentos = []
    solucao = busca_grafo(estado, 'dfs')
    if solucao is not None:
        for nodo in solucao:
            movimentos.append(nodo.acao)
        print(movimentos)
        return movimentos
    return None

def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

    ###########################################


def empilha_solucao(nodo):
    nodos_solucao = []
    while nodo.pai != None:
        nodos_solucao.insert(0, nodo)
        nodo = nodo.pai
    return nodos_solucao


def busca_grafo(estado: str, type):
    nodoInicial = Nodo(estado, None, None, 0)
    fronteira = [nodoInicial]
    expandidos = set()
    while True:
        if len(fronteira) == 0:
            return None
        if type == 'bfs':
            nodoAtual = fronteira.pop()
        elif type == 'dfs':
            nodoAtual = fronteira.pop(0)


        if nodoAtual.estado == SOLUCAO:
            print("Nodos expandidos: ", len(expandidos))
            return empilha_solucao(nodoAtual)
        if nodoAtual.estado not in expandidos:
            proximos_nodos = expande(nodoAtual)
            expandidos.add(nodoAtual.estado)
            for proximo_nodo in proximos_nodos:
                if proximo_nodo.estado not in expandidos:
                    fronteira.insert(0, proximo_nodo)
        print (nodoAtual.estado)


######

# Validações
estadoInicial = "5_6814327"
dfs(estadoInicial)

