from ..othello.gamestate import GameState
from ..othello.board import Board


def bord_scores():
    scores = {(0, 0): 120, (0, 1): -20, (0, 2): 20, (0, 3): 5, (0, 4): 5, (0, 5): 20, (0, 6): -20, (0, 7): 120,
              (1, 0): -20, (1, 1): -40, (1, 2): -5, (1, 3): -5, (1, 4): -5, (1, 5): -5, (1, 6): -40, (1, 7): -20,
              (2, 0): 20, (2, 1): -5, (2, 2): 15, (2, 3): 3, (2, 4): 3, (2, 5): 15, (2, 6): -5, (2, 7): 20,
              (3, 0): 5,(3, 1): -5, (3, 2): 3, (3, 3): 3, (3, 4): 3, (3, 5): 3, (3, 6): -5, (3, 7): 5,
              (4, 0): 5, (4, 1): -5,(4, 2): 3, (4, 3): 3, (4, 4): 3, (4, 5): 3, (4, 6): -5, (4, 7): 5,
              (5, 0): 20, (5, 1): -5, (5, 2): 15,(5, 3): 3, (5, 4): 3, (5, 5): 15, (5, 6): -5, (5, 7): 20,
              (6, 0): -20, (6, 1): -40, (6, 2): -5, (6, 3): -5, (6, 4): -5, (6, 5): -5, (6, 6): -40, (6, 7): -20,
              (7, 0): 120, (7, 1): -20, (7, 2): 20, (7, 3): 5, (7, 4): 5, (7, 5): 20, (7, 6): -20, (7, 7): 120}

    return scores


def rate_state(state: GameState) -> int:
    playerColor = state.player
    opponentColor = state.board.opponent(playerColor)

    # Rate by the difference of pieces from the opponent

    numPieces = state.board.piece_count[playerColor]
    opponentPieces = state.board.piece_count[opponentColor]
    piecesDiff = numPieces - opponentPieces
    piecesWeight = 0.4

    # Rate by the number of valid moves

    numValidMovesPlayer = len(state.legal_moves())
    numValidMovesOpponent = len(GameState(state.board, opponentColor).legal_moves())
    validMovesyDiff = numValidMovesPlayer - numValidMovesOpponent
    validMovesWeight = 0.6

    #Rate by board scores


    return piecesDiff * piecesWeight + validMovesyDiff * validMovesWeight
