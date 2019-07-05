from Face import Face


class Cubelet:

    # 0 indicates a blank face; 1-6 indicate sides
    # U, F, R, B, L, D

    def __init__(self):

        self.up = self.front = self.right = self.back = self.left = self.down = Face.Blank

    def turn_u_cw(self):

        temp = self.back

        self.back = self.left
        self.left = self.front
        self.front = self.right
        self.right = temp

    def turn_u_ccw(self):

        temp = self.back

        self.back = self.right
        self.right = self.front
        self.front = self.left
        self.left = temp

    def turn_f_cw(self):

        temp = self.up

        self.up = self.left
        self.left = self.down
        self.down = self.right
        self.right = temp

    def turn_f_ccw(self):

        temp = self.up

        self.up = self.right
        self.right = self.down
        self.down = self.left
        self.left = temp

    def turn_r_cw(self):
        temp = self.up

        self.up = self.front
        self.front = self.down
        self.down = self.back
        self.back = temp

    def turn_r_ccw(self):
        temp = self.up

        self.up = self.back
        self.back = self.down
        self.down = self.front
        self.front = temp
