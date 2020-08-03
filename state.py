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
 
        bstate = np.zeros(64, np.uint8)
        for i in range(64):
            pp = self.board.piece_at(i)
            if pp is not None:
                print(pp)
                pass
        
        bstate = bstate.reshape(8,8)
        exit(0)

        state = np.zeros((8,8,5))


        state[:,:,0] = (bstate>>3)&1
        state[:,:,1] = (bstate>>2)&1
        state[:,:,2] = (bstate>>1)&1
        state[:,:,3] = (bstate>>0)&1

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
    