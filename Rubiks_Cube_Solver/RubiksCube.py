from Cubelet import Cubelet
from Face import Face


class RubiksCube:

    def __init__(self):

        # arranged left to right, back to front, top to bottom
        self.cubelets = [Cubelet()
                         for i in range(27)]
        self.initialize_cube()

    def initialize_cube(self):

        for i in range(0, 9):
            self.cubelets[i].sides[0] = Face.Yellow

        for cubelet in self.get_front_cubelets():
            cubelet.sides[1] = Face.Blue

        for cubelet in self.get_right_cubelets():
            cubelet.sides[2] = Face.Red

        for i in range(0, 27, 9):
            for j in range(3):
                self.cubelets[i + j].sides[3] = Face.Green

        for i in range(0, 27, 3):
            self.cubelets[i].sides[4] = Face.Orange

        for i in range(18, 27):
            self.cubelets[i].sides[5] = Face.White

    def print_cube(self):

        print("\nUp")
        for i in range(0, 9):
            print(self.cubelets[i].sides[0])

        print("\nFront")
        for cubelet in self.get_front_cubelets():
            print(cubelet.sides[1])

        print("\nRight")
        for cubelet in self.get_right_cubelets():
            print(cubelet.sides[2])

        print("\nBack")
        for cubelet in self.get_back_cubelets():
            print(cubelet.sides[3])

        print("\nLeft")
        for i in range(0, 27, 3):
            print(self.cubelets[i].sides[4])

        print("\nDown")
        for i in range(18, 27):
            print(self.cubelets[i].sides[5])

    @staticmethod
    def rotate_face_cw(cubelets, turn, side_to_set):

        for cubelet in cubelets:
            turn(cubelet)

        temp = cubelets[0]
        cubelets[0] = cubelets[6]
        cubelets[6] = cubelets[8]
        cubelets[8] = cubelets[2]
        cubelets[2] = temp

        temp = cubelets[1]
        cubelets[1] = cubelets[3]
        cubelets[3] = cubelets[7]
        cubelets[7] = cubelets[5]
        cubelets[5] = temp

        side_to_set(cubelets)

    @staticmethod
    def rotate_face_ccw(cubelets, turn, side_to_set):

        for cubelet in cubelets:
            turn(cubelet)

        temp = cubelets[0]
        cubelets[0] = cubelets[2]
        cubelets[2] = cubelets[8]
        cubelets[8] = cubelets[6]
        cubelets[6] = temp

        temp = cubelets[1]
        cubelets[1] = cubelets[5]
        cubelets[5] = cubelets[7]
        cubelets[7] = cubelets[3]
        cubelets[3] = temp

        side_to_set(cubelets)



    def get_up_cubelets(self):

        up_cubelets = []

        for i in range(0, 9):
            up_cubelets.append(self.cubelets[i])

        return up_cubelets

    def set_up_cubelets(self, cubelets):

        index = 0

        for i in range(0, 9):
            self.cubelets[i] = cubelets[index]
            index += 1

    def get_front_cubelets(self):

        front_cubelets = []

        for i in range(6, 27, 9):
            for j in range(3):
                front_cubelets.append(self.cubelets[i + j])

        return front_cubelets

    def set_front_cubelets(self, cubelets):

        index = 0

        for i in range(6, 27, 9):
            for j in range(3):
                self.cubelets[i + j] = cubelets[index]
                index += 1

    def get_right_cubelets(self):

        right_cubelets = []

        for i in range(8, 27, 9):
            for j in range(3):
                right_cubelets.append(self.cubelets[i - 3 * j])

        return right_cubelets

    def set_right_cubelets(self, cubelets):

        index = 0

        for i in range(8, 27, 9):
            for j in range(3):
                self.cubelets[i - 3 * j] = cubelets[index]
                index += 1

    def get_back_cubelets(self):

        back_cubelets = []

        for i in range(2, 27, 9):
            for j in range(3):
                cub = self.cubelets[i - j]
                back_cubelets.append(cub)

        return back_cubelets

    def set_back_cubelets(self, cubelets):

        index = 0

        for i in range(2, 27, 9):
            for j in range(3):

                self.cubelets[i - j] = cubelets[index]
                index += 1

    def get_left_cubelets(self):

        left_cubelets = []

        for i in range(0, 27, 9):
            for j in range(3):
                left_cubelets.append(self.cubelets[i + 3 * j])

        return left_cubelets

    def set_left_cubelets(self, cubelets):

        index = 0

        for i in range(0, 27, 3):
            self.cubelets[i] = cubelets[index]
            index += 1

    def get_down_cubelets(self):

        down_cubelets = []

        for i in range(24, 17, -3):
            for j in range(3):
                cub = self.cubelets[i + j]
                down_cubelets.append(cub)

        return down_cubelets

    def set_down_cubelets(self, cubelets):

        index = 0

        for i in range(24, 17, -3):
            for j in range(3):
                self.cubelets[i + j] = cubelets[index]
                index += 1
