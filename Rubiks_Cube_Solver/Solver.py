from RubiksCube import RubiksCube
from Action import Action
import random


class RubiksCubeSolver:

    actions = [Action.U, Action.U_prime,
               Action.F, Action.F_prime,
               Action.R, Action.R_prime,
               Action.B, Action.B_prime,
               Action.L, Action.L_prime,
               Action.D, Action.D_prime]

    def __init__(self):

        self.cube = RubiksCube()

    def mix_cube(self, count):

        for i in range(count):
            action = random.choice(RubiksCubeSolver.actions)
            action(self.cube)


r = RubiksCubeSolver()
r.mix_cube(100)

r.cube.print_cube()
