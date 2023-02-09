from typing import List
from ..othello.gamestate import GameState
from ..othello.board import Board, from_string
from .state_rating import rate_state
from .time_checker import has_reached_time_limit

def max_value(state: GameState, alpha: int, beta: int, currentMove, initial_time):
    newMove = currentMove
    if has_reached_time_limit(initial_time):
        return rate_state(state), newMove

    for board, move in possible_next_moves(state):
        value = min_value(GameState(board, state.player), alpha, beta, newMove, initial_time)
        alpha = max(alpha, value)
        newMove = move
        if alpha >= beta:
            break

    return alpha, newMove


def min_value(state: GameState, alpha: int, beta: int, move, initial_time) -> int:
    if has_reached_time_limit(initial_time):
        return rate_state(state)

    for board, move in possible_next_moves(state):
        value, move = max_value(GameState(board, state.player), alpha, beta, move, initial_time)
        beta = min(beta, value)
        if beta <= alpha:
            break

    return beta

def possible_next_moves(state: GameState) -> List[Board]:
    next_moves = []
    for move in state.legal_moves():
        nextState = from_string(state.board.__str__())
        nextState.process_move(move, state.player)
        next_moves.append((nextState, move))
    return next_moves
