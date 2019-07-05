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

        for i in range(6, 27, 9):
            for j in range(3):
                self.cubelets[i + j].front = Face.Blue

        for i in range(2, 27, 3):
            self.cubelets[i].right = Face.Red

        for i in range(0, 27, 9):
            for j in range(3):
                self.cubelets[i + j].back = Face.Green

        for i in range(0, 27, 3):
            self.cubelets[i].left = Face.Orange

        for i in range(19, 27):
            self.cubelets[i].down = Face.White

    def print_cube(self):

        print("\nTop")
        for i in range(0, 9):
            print(self.cubelets[i].up)

        print("\nFront")
        for i in range(6, 9):
            print(self.cubelets[i].front)
        for i in range(15, 18):
            print(self.cubelets[i].front)
        for i in range(24, 27):
            print(self.cubelets[i].front)

        print("\nRight")
        for i in range(2, 27, 3):
            print(self.cubelets[i].right)

        print("\nBack")
        for i in range(0, 3):
            print(self.cubelets[i].back)
        for i in range(9, 12):
            print(self.cubelets[i].back)
        for i in range(18, 21):
            print(self.cubelets[i].back)

        print("\nLeft")
        for i in range(0, 27, 3):
            print(self.cubelets[i].left)

        print("\nDown")
        for i in range(19, 27):
            print(self.cubelets[i].down)

    def swap_cubelets(self, w, x, y, z):

        temp = self.cubelets[w]
        self.cubelets[w] = self.cubelets[x]
        self.cubelets[x] = self.cubelets[y]
        self.cubelets[y] = self.cubelets[z]
        self.cubelets[z] = temp

    def turn_r(self):

        for i in range(2, 27, 3):
            self.cubelets[i].turn_r()

        self.swap_cubelets(2, 8, 26, 20)
        self.swap_cubelets(5, 17, 23, 11)

    def turn_r_inv(self):

        for i in range(2, 27, 3):
            self.cubelets[i].turn_r_inv()

        self.swap_cubelets(2, 20, 26, 8)
        self.swap_cubelets(5, 11, 23, 17)
