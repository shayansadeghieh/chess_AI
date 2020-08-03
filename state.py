import chess
import numpy as np

class State(object):
    def __init__(self, board=None):
        if board is None:
            self.board = chess.Board()
        else:
            self.board = board 
    
    def serialize(self):
        assert self.board.is_valid()
 
        bstate = np.zeros(64)

        state = np.zeros((8,8,5))

        for r in range(8):
            for c in range(8):
                state[r,c,0] = (bstate[r*8+c]/8)&1
                state[r,c,1] = (bstate[r*8+c]/4)&1
                state[r,c,2] = (bstate[r*8+c]/2)&1
                state[r,c,3] = (bstate[r*8+c]/1)&1

        

        #Fourth column is who's turn it is
        state[:, :, 4] = (self.board.turn*1.)

        return state
    
    def edges(self):
        return self.board.legal_moves 
    
    def value(self):
        return 0

if __name__ == "__main__":
    s = State()
    print(s.board)
    print(s.edges())
    