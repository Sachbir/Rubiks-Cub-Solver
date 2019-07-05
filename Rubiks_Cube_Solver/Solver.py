from RubiksCube import RubiksCube
from Action import Action
import random


# noinspection PyCallByClass,PyTypeChecker
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

    def find_cubelet(self, color_1, color_2, color_3=None):

        for cubelet in self.cube.cubelets:
            if color_3 is None and cubelet.sides.count(Face.Blank) != 4:
                continue
            if (color_1 in cubelet.sides and color_2 in cubelet.sides and
                    (color_3 is None or color_3 in cubelet.sides)):
                return cubelet

    def put_bottom_edge_in(self, side_color):

        bottom_edge = self.find_cubelet(Face.White, side_color)

        index_of_cubelet = self.cube.cubelets.index(bottom_edge)

        if index_of_cubelet > 17:   # bottom layer
            face_center = index_of_cubelet - 9
            face_color = self.cube.cubelets[face_center].sides
            if side_color in face_color:    # correct spot
                return
            if face_center == 10:
                Action.B(self.cube)
                Action.B(self.cube)
            elif face_center == 12:
                Action.L(self.cube)
                Action.L(self.cube)
            elif face_center == 14:
                Action.R(self.cube)
                Action.R(self.cube)
            else:
                Action.F(self.cube)
                Action.F(self.cube)
        elif 8 < index_of_cubelet < 18:     # middle layer
            if index_of_cubelet == 9:
                Action.L(self.cube)
                Action.U(self.cube)
                Action.L_prime(self.cube)
            elif index_of_cubelet == 11:
                Action.R_prime(self.cube)
                Action.U(self.cube)
                Action.R(self.cube)
            elif index_of_cubelet == 15:
                Action.L_prime(self.cube)
                Action.U(self.cube)
                Action.L(self.cube)
            else:
                Action.R(self.cube)
                Action.U(self.cube)
                Action.R_prime(self.cube)

        index_of_cubelet = self.cube.cubelets.index(bottom_edge)

        if index_of_cubelet < 9:
            while True:
                face_center = index_of_cubelet + 9
                face_color = self.cube.cubelets[face_center].sides
                if side_color in face_color:
                    break
                Action.U(self.cube)
                index_of_cubelet = self.cube.cubelets.index(bottom_edge)

            if face_center == 10:
                Action.B(self.cube)
                Action.B(self.cube)
            elif face_center == 12:
                Action.L(self.cube)
                Action.L(self.cube)
            elif face_center == 14:
                Action.R(self.cube)
                Action.R(self.cube)
            else:
                Action.F(self.cube)
                Action.F(self.cube)

    def fix_edge(self):

        Action.F(self.cube)
        Action.D_prime(self.cube)
        Action.L(self.cube)
        Action.D(self.cube)

    def down_cross(self):

        r.put_bottom_edge_in(Face.Blue)
        r.put_bottom_edge_in(Face.Red)
        r.put_bottom_edge_in(Face.Green)
        r.put_bottom_edge_in(Face.Orange)

        for i in range(4):
            cubelet = self.cube.cubelets[25]
            if cubelet.sides[5] != Face.White:
                self.fix_edge()
            self.turn_cube_v_cw()

r = RubiksCubeSolver()
r.mix_cube(100)

r.cube.print_cube()
