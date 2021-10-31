class Mark:
    def __init__(self):
        self.x_cor = 4
        self.y_cor = 4

    def move_up(self):
        if self.y_cor > 0:
            self.y_cor -= 1

    def move_down(self):
        if self.y_cor < 8:
            self.y_cor += 1

    def move_right(self):
        if self.x_cor < 8:
            self.x_cor += 1

    def move_left(self):
        if self.x_cor > 0:
            self.x_cor -= 1
