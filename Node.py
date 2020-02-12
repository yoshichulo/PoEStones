from Puzzle import Puzzle

class Node:
    def __init__(self, puzzle, parent, node_id, action):
        self.puzzle = puzzle
        self.parent = parent
        self.node_id = node_id
        self.action = action

    def __str__(self):
        return self.puzzle.board, self.action