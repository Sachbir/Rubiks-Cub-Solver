from enum import Enum
from Cubelet import Cubelet


# noinspection PyMethodParameters,PyPep8Naming
class Action(Enum):

    def U(cube):
        cube.rotate_face_cw(cube.get_up_cubelets(), Cubelet.turn_u_cw, cube.set_up_cubelets)

    def U_prime(cube):
        cube.rotate_face_ccw(cube.get_up_cubelets(), Cubelet.turn_u_ccw, cube.set_up_cubelets)

    def F(cube):
        cube.rotate_face_cw(cube.get_front_cubelets(), Cubelet.turn_f_cw, cube.set_front_cubelets)

    def F_prime(cube):
        cube.rotate_face_ccw(cube.get_front_cubelets(), Cubelet.turn_f_ccw, cube.set_front_cubelets)

    def R(cube):
        cube.rotate_face_cw(cube.get_right_cubelets(), Cubelet.turn_r_cw, cube.set_right_cubelets)

    def R_prime(cube):
        cube.rotate_face_ccw(cube.get_right_cubelets(), Cubelet.turn_r_ccw, cube.set_right_cubelets)

    def B(cube):
        cube.rotate_face_cw(cube.get_back_cubelets(), Cubelet.turn_f_ccw, cube.set_back_cubelets)

    def B_prime(cube):
        cube.rotate_face_ccw(cube.get_back_cubelets(), Cubelet.turn_f_cw, cube.set_back_cubelets)

    def L(cube):
        cube.rotate_face_cw(cube.get_left_cubelets(), Cubelet.turn_r_ccw, cube.set_left_cubelets)

    def L_prime(cube):
        cube.rotate_face_ccw(cube.get_left_cubelets(), Cubelet.turn_r_cw, cube.set_left_cubelets)

    def D(cube):
        cube.rotate_face_cw(cube.get_down_cubelets(), Cubelet.turn_u_ccw, cube.set_down_cubelets)

    def D_prime(cube):
        cube.rotate_face_ccw(cube.get_down_cubelets(), Cubelet.turn_u_cw, cube.set_down_cubelets)
