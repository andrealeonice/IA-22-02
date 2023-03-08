# Inteligência Artificial | 2022/2 | Turma A | Trabalho 3

## Participantes
 - Andrea Leonice Pereira dos Santos | 00275624
 - Eduardo Raupp Peretto | 00313439

## Bibliotecas
  A biblioteca random foi utilizada na implementação
 
## Parâmetros Algoritmo Genético
* Gerações (g): 350
* Nº de Indivíduos da população (n): 100
* Tamanho do Torneio (k): 50
* Probabilidade de Mutação (m): 0.5
* Número de Indivíduos no Elitismo (e): 10


## Parâmetros Regressão Linear 
  * Theta 0: 0.2
  * Theta 1: 0.1
  * Alfa:  0.01
  * Nºde Iterações: 6000

   Erro Médio Quadrático: 8.527708190982551

## Implementação
 Para o problema das 8 rainhas foi necessário criar mais 3 novas funções:
*  _populate(n):_ Cria uma população com n individuos
* _elitism(p,e):_ Retorna os indivíduos do elitismo
* _participants(p, n, k):_ Seleciona randomicamente os individuos que participarão do torneio
* _check(p):_Esta função é responsável por executar os parâmetros de avaliação do fitness
