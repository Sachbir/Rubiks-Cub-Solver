from Face import Face


class Cubelet:

    # 0 indicates a blank face; 1-6 indicate sides
    # U, F, R, B, L, D

    def __init__(self):

        self.up = self.front = self.right = self.back = self.left = self.down = Face.Blank

