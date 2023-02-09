# Inteligência Artificial | 2022/2 | Turma A | Trabalho 2

## Participantes
 - Andrea Leonice Pereira dos Santos | 00275624
 - Eduardo Raupp Peretto | 00313439

## Implementação 
 Optamos por implementar o algoritmo da Poda alfa-beta, a estrutura da implementação está divida nos seguintes arquivos:
 - _state_rating.py_. Possui a implementação das funções de avaliação, retornando o valor final das análises feitas
 - _pruning.py_. Contém as funções de poda, avaliando através dos possíveis próximos movimentos os valores de alfa e beta, assim como determina o próximo movimento do agente. 
 - _time_checker.py_. Checa o tempo que o servidor está aguardando a jogada do agente, o limite estabelecido é de 4.8 segundos.
 - _agente.py_. Faz a execução da jogada.
 
## Bibliotecas
  Nenhuma biblioteca adicional foi utilizada na implementação
 
## Função de Avalialção 
  Foram implementadas 3 tipos de avaliações para as jogadas do agente e seu oponente:
  1. Análise da quantidade de peças do oponente 
     Baseada na diferença da quantidade de peças que o agente e o seu oponente possuem no tabuleiro
  2. Análise da quantidade de jogadas válidas
     Baseada na diferença da quantidade de jogadas válidas entre o agente e o oponente
  3. Anáise baseada no peso de cada posição do tabuleiro
     Baseada na atruiuição de pesos para as posições estratégicas do tabuleiro, como por exemplo, conquistar uma quina é uma grande vantagem em relação ao seu oponente, por isso possui o maior peso em relação a outras posições.
   <p align="center">
  <img src="https://user-images.githubusercontent.com/44913456/217960638-65a89d99-d793-454f-9967-caa417c233ad.png" />
</p>
     
 Para cada avaliação foram atribuias porcentagens representando sua influência na tomada de decisáo do próximo movimento.

## Estratégia de Parada 
 

## Melhorias
 
 
## Decisões de projeto e dificuldades encontradas
 A nossa dificuldade foi determinar o valor das porcentagens de cada função de avaliação de forma que pudesse melhorar a tomada de decisão do algoritmo. 
 
## Bibliografia
  https://www.ic.unicamp.br/~rocha/teaching/2011s2/mc906/seminarios/2011s2-mc906-seminario-04.pdf
  https://www.ultraboardgames.com/othello/tips.php
 
