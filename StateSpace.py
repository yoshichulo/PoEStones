from Puzzle import Puzzle
from Node import Node


class StateSpace:
    def __init__(self, states):
        self.states = states
        self.counter = 1

    def print_states(self):
        for p in self.states:
            print(p)

    def generate_successors(self, n):
        for i in range(1, 4):
            for j in range(1, 4):
                if i != 2 and j != 2:
                    p = n.puzzle.action(i,j)
                    self.states.append(Node(p, n, self.counter, self.action_string(i,j)))
                    self.counter += 1
    
    def get_new(self):
        if len(self.states) != 0:
            return self.states.pop()
    
    def action_string(self, x, y):
        return "x: {} ; y: {}".format(x,y)