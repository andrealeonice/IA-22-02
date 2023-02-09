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
    Returns a move from the list of possible ones
    :param state: the game state to play from
    :return: (int, int)
    """
    value, move = max_value(state, -sys.maxsize, sys.maxsize, (-1, -1), time.process_time())
    return move

