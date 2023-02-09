from typing import List
from ..othello.gamestate import GameState
from ..othello.board import Board, from_string
from .state_rating import rate_state
from .time_checker import has_reached_time_limit

def max_value(state: GameState, alpha: int, beta: int, decision, start_time) -> int:
    if has_reached_time_limit(start_time):
        return rate_state(state)

    for board, move in possible_next_moves(state):
        v = min_value(GameState(board, state.player), alpha, beta, decision, start_time)
        alpha = max(alpha, v)
        if beta < alpha:
            return alpha
        else:
            decision['move'] = move

    return alpha


def min_value(state: GameState, alpha: int, beta: int, decision, start_time) -> int:
    if has_reached_time_limit(start_time):
        return rate_state(state)

    for board, move in possible_next_moves(state):
        v = max_value(GameState(board, state.player), alpha, beta, decision, start_time)
        beta = min(beta, v)
        if alpha > beta:
            return beta

    return beta

def possible_next_moves(state: GameState) -> List[Board]:
    next_moves = []
    for move in state.legal_moves():
        nextState = from_string(state.board.__str__())
        nextState.process_move(move, state.player)
        next_moves.append((nextState, move))
    return next_moves
