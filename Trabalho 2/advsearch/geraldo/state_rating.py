from ..othello.gamestate import GameState
from ..othello.board import Board

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

    return piecesDiff * piecesWeight + validMovesyDiff * validMovesWeight
