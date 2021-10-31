class Button:

    def __init__(self, x, y, x1, y1, value, mode):
        self.x = x
        self.y = y
        self.width = x1
        self.height = y1
        self.value = value
        self.mode = mode

    def is_pressed(self, x, y):
        return self.x < x < self.x + self.width and self.y < y < self.y + self.height
