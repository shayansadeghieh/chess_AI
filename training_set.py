from state import State
import numpy as np 
import os
import chess.pgn 

def get_dataset(num_samples = None):
    X, Y = [], []
    gn = 0
    for fn in os.listdir('data'):
        pgn = open(os.path.join('data', fn))
        while 1:
            try:
                #Parse and extract each individual game from the pgn file, handles headers/ no headers
                game = chess.pgn.read_game(pgn) 
            except Exception:
                break
            #Developed value notation: 0 means draw, -1 means black won, 1 means white and * means ongoing game (who cares)
            value = {'1/2-1/2':0, '0-1':-1, '1-0':1, '*': 'who_cares'}[game.headers["Result"]]
            # print(value)
            board = game.board()
            #Iterate through all moves and play them on the board 
            for i, move in enumerate(game.mainline_moves()):
                board.push(move)
                ser = State(board).serialize()[:,:,0]
                X.append(ser)
                Y.append(value)
            print("parsing game %d, got %d examples" % (gn, len(X)))
            if num_samples is not None and len(X) > num_samples:
                return X,Y
            gn+=1
    return X,Y 

if __name__ == "__main__":
    X, Y = get_dataset(num_samples = 1000)

