import time
import sys
from typing import Tuple
import random
from ..othello.board import Board, from_string
from ..othello.gamestate import GameState
from .pruning import max_value

def movimento_chega_no_estado_objetivo(estado: GameState, estado_objetivo: Board, movimento):
    possivel_estado = from_string(estado.board.__str__())
    possivel_estado.process_move(movimento, estado.player)

    return possivel_estado.__str__() == estado_objetivo.__str__()


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """ 
    decision = {
        'move': (-1, -1),
    }

    valor = max_value(state, -sys.maxsize, sys.maxsize, decision, time.process_time())

    return decision['move']

