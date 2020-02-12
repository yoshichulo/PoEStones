from Puzzle import Puzzle
from StateSpace import StateSpace
from Node import Node
import hashlib

class Problem:
    def __init__(self, initial_puzzle):
        self.puzzle = initial_puzzle
        self.solutions = ["bbb8aae57c104cda40c93843ad5e6db8", "22df3fbae18a69e9b8124faf6d1a3840"]

    def is_solved(self, p):
        return True if p.hash() in self.solutions else False

    def resolve(self):
        states = StateSpace(list())
        visited = set()
        solved = False

        p = Puzzle(self.puzzle)
        n = Node(p, None, 0, None)
        states.states.append(n)

        while not solved and len(states.states) != 0:
            n = states.get_new()
            p = n.puzzle
            
            if self.is_solved(p):
                solved = True
            else:
                if p.hash() not in visited:
                    visited.add(p.hash())
                    states.generate_successors(n)
        if solved:
            self.print_solution(n)
        else:
            print("The puzzle has no solution")
    
    def print_solution(self, node):
        sol_path = list()
        sol_path.append(node)
        while node.parent != None:
            sol_path.append(node.parent)
            node = node.parent
        sol_path.reverse()
        for n in sol_path:
            print(n.__str__())

p = Problem([[0,0,0],[0,0,0],[0,0,0]])
p.resolve()