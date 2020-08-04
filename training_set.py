from state import State
import numpy as np 
import os
import chess.pgn 

def get_dataset(num_samples = None):
    X, Y = [], []
    gn = 0
    values = {'1/2-1/2':0, '0-1':-1, '1-0':1}
    for fn in os.listdir('data'):
        pgn = open(os.path.join('data', fn))
        while 1:
            try:
                #Parse and extract each individual game from the pgn file, handles headers/ no headers
                game = chess.pgn.read_game(pgn) 
            except Exception:
                break
            #Developed value notation: 0 means draw, -1 means black won, 1 means white and * means ongoing game (who cares)
            res = game.headers["Result"]
            if res not in values:
                continue
            value = values[res]
            # print(value)
            board = game.board()
            #Iterate through all moves and play them on the board 
            for i, move in enumerate(game.mainline_moves()):
                board.push(move)
                ser = State(board).serialize()
                X.append(ser)
                Y.append(value)
            print("parsing game %d, got %d examples" % (gn, len(X)))
            if num_samples is not None and len(X) > num_samples:
                return X,Y
            gn+=1
    return X,Y

import h5py 


if __name__ == "__main__":
    X, Y = get_dataset(1E5)
    np.savez("processed/dataset_100K.npz", X, Y)
    # h5 = h5py.File('processed/trainme.h5', 'w')
    # h5.create_dataset('X', X)


