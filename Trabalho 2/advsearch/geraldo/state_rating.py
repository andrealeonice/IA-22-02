from ..othello.gamestate import GameState
from ..othello.board import Board

def rate_state(state: GameState) -> int:

    # Number of pieces
    color = state.player
    opponentColor = state.board.opponent(color)
    numPieces = state.board.piece_count[color]
    piecesWeight = 0.7

    # Number of valid moves
    validMovesyDiff = len(state.legal_moves()) - len(state.legal_moves())
    validMovesWeight = 0.3

    return numPieces * piecesWeight + validMovesyDiff * validMovesWeight
