import hashlib
from copy import deepcopy


class Puzzle:
    def __init__(self, array):
        self.board = array

    def to_str(self):
        return ''.join(str(i) for p in self.board for i in p)
    
    def print_board(self):
        print(self.board)

    def hash(self):
        return hashlib.md5(self.to_str().encode()).hexdigest()

    def add_barrier(self):
        for row in self.board:
            row.insert(0, 0)
            row.insert(4,0)
        self.board.insert(0, [0,0,0,0,0])
        self.board.append([0,0,0,0,0])

    def remove_barrier(self):
        aux_board = list()
        for r in self.board[1:4]:
            aux_board.append(r[1:4])
        self.board = aux_board

    def action(self, x, y):
        aux_puzzle = deepcopy(self)
        aux_puzzle.add_barrier()
        aux_puzzle.change_values(x, y)
        aux_puzzle.remove_barrier()
        return aux_puzzle

    def change_values(self, x, y):
        self.board[x][y] = 1 - self.board[x][y]
        self.board[x-1][y] = 1 - self.board[x-1][y]
        self.board[x+1][y] = 1 - self.board[x+1][y]
        self.board[x][y+1] = 1 - self.board[x][y+1]
        self.board[x][y-1] = 1 - self.board[x][y-1]
