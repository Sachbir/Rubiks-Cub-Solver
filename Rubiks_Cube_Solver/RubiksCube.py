from Cubelet import Cubelet
from Face import Face


class RubiksCube:

    def __init__(self):

        # arranged left to right, back to front, top to bottom
        self.cubelets = [Cubelet()
                         for i in range(27)]

    def initialize_cube(self):

        for i in range(0, 9):
            self.cubelets[i].up = Face.Yellow

        for i in range(19, 27):
            self.cubelets[i].up = Face.White

        for i in range(0, 27, 3):
            self.cubelets[i].left = Face.Orange

        for i in range(2, 27, 3):
            self.cubelets[i].right = Face.Red

        for i in range(0, 3):
            self.cubelets[i].back = Face.Green
        for i in range(9, 12):
            self.cubelets[i].back = Face.Green
        for i in range(18, 21):
            self.cubelets[i].back = Face.Green

        for i in range(6, 9):
            self.cubelets[i].back = Face.Blue
        for i in range(15, 18):
            self.cubelets[i].back = Face.Blue
        for i in range(24, 27):
            self.cubelets[i].back = Face.Blue
