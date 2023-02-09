from ..othello.gamestate import GameState
from ..othello.board import Board

def rate_state(state: GameState) -> int:
    playerColor = state.player
    opponentColor = state.board.opponent(playerColor)

    # Rate by the difference of pieces from the opponent
    
    numPieces = state.board.piece_count[playerColor]
    opponentPieces = state.board.piece_count[opponentColor]
    piecesDiff = numPieces - opponentPieces
    piecesWeight = 0.2

    # Rate by the number of valid moves

    numValidMovesPlayer = len(state.legal_moves())
    numValidMovesOpponent = len(GameState(state.board, opponentColor).legal_moves())
    validMovesyDiff = numValidMovesPlayer - numValidMovesOpponent
    validMovesWeight = 0.3

    #Rate by the corners

    numCornersPlayer=0
    numCornersOpponent=0

    if (state.board.is_legal((0,0),playerColor)):
        numCornersPlayer += 5
    elif (state.board.is_legal((0,0),opponentColor)):
        numCornersOpponent+=5
    if (state.board.is_legal((7,7),playerColor)):
        numCornersPlayer += 5
    elif (state.board.is_legal((7,7),opponentColor)):
        numCornersOpponent += 5
    if (state.board.is_legal((0, 7), playerColor)):
        numCornersPlayer += 5
    elif (state.board.is_legal((0, 7), opponentColor)):
        numCornersOpponent += 5
    if (state.board.is_legal((7, 0), playerColor)):
        numCornersPlayer += 5
    elif (state.board.is_legal((7, 0), opponentColor)):
        numCornersOpponent += 5

    cornnersDiff = numCornersPlayer - numCornersOpponent
    validCornersWeight = 0.5

    return piecesDiff * piecesWeight + validMovesyDiff * validMovesWeight + cornnersDiff * validCornersWeight
