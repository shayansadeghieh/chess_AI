from state import State
import numpy as np 
import os
import chess.pgn 

for fn in os.listdir('data'):
    pgn = open(os.path.join('data', fn))
    while 1:
        try:
            #Parse and extract each individual game from the pgn file, handles headers/ no headers
            game = chess.pgn.read_game(pgn) 
        except Exception:
            break
        print(game.headers['Result'])
        #Developed value notation: 0 means draw, -1 means black won, 1 means white and * means ongoing game (who cares)
        value = {'1/2-1/2':0, '0-1':-1, '1-0':1, '*': 'who_cares'}[game.headers["Result"]]
        print(value)
        board = game.board()
        print(board)
        #Iterate through all moves and play them on the board 
        for i, move in enumerate(game.mainline_moves()):
            board.push(move)
            print(value, State(board).serialize())
        exit(0)
    break
