from Face import Face


class Cubelet:

    # 0 indicates a blank face; 1-6 indicate sides
    # U, F, R, B, L, D

    def __init__(self):

        self.up = self.front = self.right = self.back = self.left = self.down = Face.Blank

    def turn_r(self):

        if self.up == Face.Blank:
            x = 0

        temp = self.up

        self.up = self.front
        self.front = self.down
        self.down = self.back
        self.back = temp

    def turn_r_inv(self):

        temp = self.up

        self.up = self.back
        self.back = self.down
        self.down = self.front
        self.front = temp
