from RubiksCube import RubiksCube
from Action import Action
from Face import Face
from Cubelet import Cubelet
import random


# noinspection PyCallByClass,PyTypeChecker
class Solver:

    cube = RubiksCube()

    Action.cube = cube
    actions = [Action.U, Action.Ui,
               Action.F, Action.Fi,
               Action.R, Action.Ri,
               Action.B, Action.Bi,
               Action.L, Action.Li,
               Action.D, Action.Di]

    @staticmethod
    def mix_cube(count):

        for i in range(count):
            action = random.choice(Solver.actions)
            action()

    @staticmethod
    def solve():

        Solver.down_cross()
        Solver.place_down_corners()
        Solver.orient_down_corners()
        Solver.position_side_edges()
        Solver.position_up_cross()
        Solver.orient_up_cross()
        Solver.position_up_corners()
        Solver.orient_up_corners()

    @staticmethod
    def find_cubelet(color_1, color_2, color_3=None):

        for cubelet in Solver.cube.cubelets:
            if color_3 is None and cubelet.sides.count(Face.BLANK) != 4:
                continue
            if (color_1 in cubelet.sides and color_2 in cubelet.sides and
                    (color_3 is None or color_3 in cubelet.sides)):
                return cubelet

    @staticmethod
    def put_bottom_edge_in(side_color):

        bottom_edge = Solver.find_cubelet(Face.White, side_color)

        index_of_cubelet = Solver.cube.cubelets.index(bottom_edge)

        if index_of_cubelet > 17:   # bottom layer
            face_center = index_of_cubelet - 9
            face_color = Solver.cube.cubelets[face_center].sides
            if side_color in face_color:    # correct spot
                return
            if face_center == 10:
                Action.B()
                Action.B()
            elif face_center == 12:
                Action.L()
                Action.L()
            elif face_center == 14:
                Action.R()
                Action.R()
            else:
                Action.F()
                Action.F()
        elif 8 < index_of_cubelet < 18:     # middle layer
            if index_of_cubelet == 9:
                Action.L()
                Action.U()
                Action.Li()
            elif index_of_cubelet == 11:
                Action.Ri()
                Action.U()
                Action.R()
            elif index_of_cubelet == 15:
                Action.Li()
                Action.U()
                Action.L()
            else:
                Action.R()
                Action.U()
                Action.Ri()

        index_of_cubelet = Solver.cube.cubelets.index(bottom_edge)

        if index_of_cubelet < 9:
            while True:
                face_center = index_of_cubelet + 9
                face_color = Solver.cube.cubelets[face_center].sides
                if side_color in face_color:
                    break
                Action.U()
                index_of_cubelet = Solver.cube.cubelets.index(bottom_edge)

            if face_center == 10:
                Action.B()
                Action.B()
            elif face_center == 12:
                Action.L()
                Action.L()
            elif face_center == 14:
                Action.R()
                Action.R()
            else:
                Action.F()
                Action.F()

    @staticmethod
    def orient_down_edge_algorithm():

        Action.F()
        Action.Di()
        Action.L()
        Action.D()

    @staticmethod
    def down_cross():

        r.put_bottom_edge_in(Face.Blue)
        r.put_bottom_edge_in(Face.Red)
        r.put_bottom_edge_in(Face.Green)
        r.put_bottom_edge_in(Face.Orange)

        for i in range(4):
            cubelet = Solver.cube.cubelets[25]
            if cubelet.sides[5] != Face.White:
                Solver.orient_down_edge_algorithm()
            Action.Yi()

    @staticmethod
    def turn_cube_cw():

        Action.U()
        Solver.cube.rotate_face_cw(Solver.cube.get_up_middle(), Cubelet.turn_u_cw, Solver.cube.set_up_middle)
        Action.Di()

    @staticmethod
    def turn_cube_ccw():

        Action.Ui()
        Solver.cube.rotate_face_ccw(Solver.cube.get_up_middle(), Cubelet.turn_u_ccw, Solver.cube.set_up_middle)
        Action.D()

    @staticmethod
    def place_down_corner_algorithm():

        Action.R()
        Action.U()
        Action.Ri()
        Action.Ui()

    @staticmethod
    def place_down_corners():

        Solver.place_down_corner(Face.Blue, Face.Red)
        Action.Yi()
        Solver.place_down_corner(Face.Red, Face.Green)
        Action.Yi()
        Solver.place_down_corner(Face.Green, Face.Orange)
        Action.Yi()
        Solver.place_down_corner(Face.Orange, Face.Blue)
        Action.Yi()

    @staticmethod
    def place_down_corner(color1, color2):

        down_corner = Solver.find_cubelet(Face.White, color1, color2)
        index_of_cubelet = Solver.cube.cubelets.index(down_corner)

        # In the bottom layer
        if index_of_cubelet > 17:

            count = 0

            while index_of_cubelet != 26:
                Action.D()
                count += 1
                index_of_cubelet = Solver.cube.cubelets.index(down_corner)

            Solver.place_down_corner_algorithm()

            for i in range(count):
                Action.Di()

            Solver.place_down_corner_algorithm()

            return

        # In the top layer
        count = 0
        while index_of_cubelet != 8:
            Action.U()
            count += 1
            index_of_cubelet = Solver.cube.cubelets.index(down_corner)

        Solver.place_down_corner_algorithm()

    @staticmethod
    def orient_down_corners():

        for i in range(4):
            corner_cubelet = Solver.cube.cubelets[26]
            while corner_cubelet.sides[5] != Face.White:
                Solver.place_down_corner_algorithm()
                Solver.place_down_corner_algorithm()
            Action.D()

    @staticmethod
    def position_side_edge_algorithm():

        Action.Ui()
        Action.Fi()
        Action.U()
        Action.F()
        Action.U()
        Action.R()
        Action.Ui()
        Action.Ri()

    @staticmethod
    def position_side_edges():

        Solver.position_side_edge(Face.Blue, Face.Red)
        Action.Yi()

        Solver.position_side_edge(Face.Red, Face.Green)
        Action.Yi()

        Solver.position_side_edge(Face.Green, Face.Orange)
        Action.Yi()

        Solver.position_side_edge(Face.Orange, Face.Blue)
        Action.Yi()

    @staticmethod
    def position_side_edge(color1, color2):

        edge_cubelet = Solver.find_cubelet(color1, color2)
        index_of_cubelet = Solver.cube.cubelets.index(edge_cubelet)

        if 8 < index_of_cubelet < 18:
            count = 0
            while index_of_cubelet != 17:
                Action.Yi()
                index_of_cubelet = Solver.cube.cubelets.index(edge_cubelet)
                count += 1
            Solver.position_side_edge_algorithm()
            for i in range(count):
                Action.Y()

        index_of_cubelet = Solver.cube.cubelets.index(edge_cubelet)

        if index_of_cubelet < 9:
            while index_of_cubelet != 5:
                Action.U()
                index_of_cubelet = Solver.cube.cubelets.index(edge_cubelet)

            Solver.position_side_edge_algorithm()

        if edge_cubelet.sides[1] != color1:
            # re-orient
            Solver.position_side_edge_algorithm()
            Action.U()
            Action.U()
            Solver.position_side_edge_algorithm()

    @staticmethod
    def position_up_cross_algorithm():

        Action.F()
        Action.U()
        Action.R()
        Action.Ui()
        Action.Ri()
        Action.Fi()

    @staticmethod
    def position_up_cross():

        cross_cubelets = [Solver.cube.cubelets[1],
                          Solver.cube.cubelets[5],
                          Solver.cube.cubelets[7],
                          Solver.cube.cubelets[3]]

        while True:

            # Cross
            flag = True
            for cubelet in cross_cubelets:
                if cubelet.sides[0] != Face.Yellow:
                    flag = False
                    break
            if flag:
                return

            # Dot
            if (cross_cubelets[0].sides[0] != Face.Yellow and
                    cross_cubelets[1].sides[0] != Face.Yellow and
                    cross_cubelets[2].sides[0] != Face.Yellow and
                    cross_cubelets[3].sides[0] != Face.Yellow):
                Solver.position_up_cross_algorithm()

            # Vertical line
            if cross_cubelets[0].sides[0] == cross_cubelets[2].sides[0] == Face.Yellow:
                Action.U()

            # L in wrong orientation
            if cross_cubelets[0].sides[0] == cross_cubelets[1].sides[0] == Face.Yellow:
                Action.Ui()
            elif cross_cubelets[2].sides[0] == cross_cubelets[3].sides[0] == Face.Yellow:
                Action.U()

            Solver.position_up_cross_algorithm()

    @staticmethod
    def orient_up_cross_algorithm():

        Action.U()
        Action.R()
        Action.U()
        Action.Ri()
        Action.U()
        Action.R()
        Action.Ui()
        Action.Ui()
        Action.Ri()

    @staticmethod
    def orient_up_cross():

        counter = 0

        while True:
            while Solver.cube.cubelets[1].sides[3] != Face.Green:
                Action.U()

            cross_edges = [Solver.cube.cubelets[1].sides[3],
                           Solver.cube.cubelets[3].sides[4],
                           Solver.cube.cubelets[7].sides[1],
                           Solver.cube.cubelets[5].sides[2]]
            if cross_edges == [Face.Green, Face.Orange, Face.Blue, Face.Red]:
                break

            index_blue = cross_edges.index(Face.Blue)

            # Vertical line
            if cross_edges[(index_blue + 2) % 4] == Face.Green:
                Solver.orient_up_cross_algorithm()

            if cross_edges[0] == ((cross_edges[1].value + 1) % 4 + 1):
                Action.Ui()
            elif cross_edges[0] == ((cross_edges[1].value + 1) % 4 + 1):
                Action.U()

            if counter == 3:
                counter = 0
                Action.U()

            Solver.orient_up_cross_algorithm()

            counter += 1

    @staticmethod
    def position_up_corners_algorithm():

        Action.U()
        Action.R()
        Action.Ui()
        Action.Li()
        Action.U()
        Action.Ri()
        Action.Ui()
        Action.L()

    # noinspection PyPep8Naming
    #
    @staticmethod
    def position_up_corners():

        while True:
            while Solver.cube.cubelets[7].sides[1] != Face.Blue:
                Action.U()

            YBR = Solver.find_cubelet(Face.Yellow, Face.Blue, Face.Red)
            YGR = Solver.find_cubelet(Face.Yellow, Face.Green, Face.Red)
            YGO = Solver.find_cubelet(Face.Yellow, Face.Green, Face.Orange)
            YBO = Solver.find_cubelet(Face.Yellow, Face.Blue, Face.Orange)

            if (Solver.cube.cubelets.index(YBR) == 8 and
                    Solver.cube.cubelets.index(YGR) == 2 and
                    Solver.cube.cubelets.index(YGO) == 0 and
                    Solver.cube.cubelets.index(YBO) == 6):
                break

            if Solver.cube.cubelets.index(YGR) == 2:
                Action.Ui()
            elif Solver.cube.cubelets.index(YGO) == 0:
                Action.U()
                Action.U()
            elif Solver.cube.cubelets.index(YBO) == 6:
                Action.U()

            Solver.position_up_corners_algorithm()

    @staticmethod
    def orient_up_corner_algorithm():

        Action.Ri()
        Action.Di()
        Action.R()
        Action.D()

    @staticmethod
    def orient_up_corners():

        for i in range(4):
            cubelet = Solver.cube.cubelets[8]
            while cubelet.sides[0] != Face.Yellow:
                Solver.orient_up_corner_algorithm()
            Action.U()


r = Solver()
r.mix_cube(200)
r.cube.print_cube()

print("\n\n")

r.solve()
r.cube.print_cube()
