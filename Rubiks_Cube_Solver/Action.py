from Cubelet import Cubelet


# noinspection PyMethodParameters,PyPep8Naming
class Action:

    cube = None

    # Letter is the side in question
    # i denotes inverse (counter-clockwise rotation)

    @staticmethod
    def U():
        Action.cube.rotate_face_cw(Action.cube.get_up_cubelets(), Cubelet.turn_u_cw, Action.cube.set_up_cubelets)

    @staticmethod
    def Ui():
        Action.cube.rotate_face_ccw(Action.cube.get_up_cubelets(), Cubelet.turn_u_ccw, Action.cube.set_up_cubelets)

    @staticmethod
    def F():
        Action.cube.rotate_face_cw(Action.cube.get_front_cubelets(), Cubelet.turn_f_cw, Action.cube.set_front_cubelets)

    @staticmethod
    def Fi():
        Action.cube.rotate_face_ccw(Action.cube.get_front_cubelets(), Cubelet.turn_f_ccw,
                                    Action.cube.set_front_cubelets)

    @staticmethod
    def R():
        Action.cube.rotate_face_cw(Action.cube.get_right_cubelets(), Cubelet.turn_r_cw, Action.cube.set_right_cubelets)

    @staticmethod
    def Ri():
        Action.cube.rotate_face_ccw(Action.cube.get_right_cubelets(), Cubelet.turn_r_ccw,
                                    Action.cube.set_right_cubelets)

    @staticmethod
    def B():
        Action.cube.rotate_face_cw(Action.cube.get_back_cubelets(), Cubelet.turn_f_ccw, Action.cube.set_back_cubelets)

    @staticmethod
    def Bi():
        Action.cube.rotate_face_ccw(Action.cube.get_back_cubelets(), Cubelet.turn_f_cw, Action.cube.set_back_cubelets)

    @staticmethod
    def L():
        Action.cube.rotate_face_cw(Action.cube.get_left_cubelets(), Cubelet.turn_r_ccw, Action.cube.set_left_cubelets)

    @staticmethod
    def Li():
        Action.cube.rotate_face_ccw(Action.cube.get_left_cubelets(), Cubelet.turn_r_cw, Action.cube.set_left_cubelets)

    @staticmethod
    def D():
        Action.cube.rotate_face_cw(Action.cube.get_down_cubelets(), Cubelet.turn_u_ccw, Action.cube.set_down_cubelets)

    @staticmethod
    def Di():
        Action.cube.rotate_face_ccw(Action.cube.get_down_cubelets(), Cubelet.turn_u_cw, Action.cube.set_down_cubelets)

    @staticmethod
    def Y():
        Action.Ui()
        Action.cube.rotate_face_ccw(Action.cube.get_up_middle(), Cubelet.turn_u_ccw, Action.cube.set_up_middle)
        Action.D()

    @staticmethod
    def Yi():
        Action.U()
        Action.cube.rotate_face_cw(Action.cube.get_up_middle(), Cubelet.turn_u_cw, Action.cube.set_up_middle)
        Action.Di()
