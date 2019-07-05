from RubiksCube import RubiksCube
from Action import Action
from Face import Face
from Cubelet import Cubelet
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

    def turn_cube_v_cw(self):

        Action.U(self.cube)
        self.cube.rotate_face_cw(self.cube.get_up_middle(), Cubelet.turn_u_cw, self.cube.set_up_middle)
        Action.D_prime(self.cube)

    def turn_cube_v_ccw(self):

        Action.U_prime(self.cube)
        self.cube.rotate_face_ccw(self.cube.get_up_middle(), Cubelet.turn_u_ccw, self.cube.set_up_middle)
        Action.D(self.cube)

    def R_U_Ri_Ui(self):

        Action.R(self.cube)
        Action.U(self.cube)
        Action.R_prime(self.cube)
        Action.U_prime(self.cube)

    def place_down_corners(self):

        self.place_a_down_corner(Face.Blue, Face.Red)
        self.turn_cube_v_cw()
        self.place_a_down_corner(Face.Red, Face.Green)
        self.turn_cube_v_cw()
        self.place_a_down_corner(Face.Green, Face.Orange)
        self.turn_cube_v_cw()
        self.place_a_down_corner(Face.Orange, Face.Blue)
        self.turn_cube_v_cw()

    def place_a_down_corner(self, color1, color2):

        down_corner = self.find_cubelet(Face.White, color1, color2)
        index_of_cubelet = self.cube.cubelets.index(down_corner)

        # In the bottom layer
        if index_of_cubelet > 17:

            count = 0

            while index_of_cubelet != 26:
                Action.D(self.cube)
                count += 1
                index_of_cubelet = self.cube.cubelets.index(down_corner)

            self.R_U_Ri_Ui()

            for i in range(count):
                Action.D_prime(self.cube)

            self.R_U_Ri_Ui()

            return

        # In the top layer
        count = 0
        while index_of_cubelet != 8:
            Action.U(self.cube)
            count += 1
            index_of_cubelet = self.cube.cubelets.index(down_corner)

        self.R_U_Ri_Ui()

    def orient_down_corners(self):

        for i in range(4):
            corner_cubelet = self.cube.cubelets[26]
            while corner_cubelet.sides[5] != Face.White:
                self.R_U_Ri_Ui()
                self.R_U_Ri_Ui()
            Action.D(self.cube)
r = RubiksCubeSolver()
r.mix_cube(100)
r.down_cross()
r.place_down_corners()
r.orient_down_corners()

r.cube.print_cube()
