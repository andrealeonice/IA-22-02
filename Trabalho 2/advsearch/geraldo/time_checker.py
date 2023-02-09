from ..othello.gamestate import GameState
from ..othello.board import Board
import time

time_limit = 4.8

def has_reached_time_limit(start_time) -> bool:
    processing_time = time.process_time() - start_time

    return processing_time >= time_limit