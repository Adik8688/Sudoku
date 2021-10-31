class Spot:
    # pygame.font.init()
    # Font_big = pygame.font.SysFont("comicsans", 70)
    # Font_small = pygame.font.SysFont("comicsans", 22)

    def __init__(self, x, y, value, sq, immutable=False):
        self.x = x
        self.y = y
        self.size = 50
        self.square_id = sq
        self.value = value
        self.suspected_values = []
        self.immutable = immutable
        self.numbers_cor = {1: (6, 4), 2: (22, 4), 3: (38, 5), 4: (6, 20), 5: (22, 20), 6: (38, 20), 7: (6, 36),
                            8: (22, 36), 9: (38, 36)}

    @staticmethod
    def get_square(x, y):
        squares = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        return squares[y // 3][x // 3]

    def is_pressed(self, x, y):
        if (x > self.x) and (x < self.x + self.size) and (y > self.y) and (y < self.y + self.size):
            return True
        return False

    def is_collide(self, spots):
        for row in spots:
            for spot in row:
                if not (spot.x == self.x and spot.y == self.y):
                    if spot.value == self.value and self.value != 0:
                        if spot.x == self.x or spot.y == self.y or spot.square_id == self.square_id:
                            return True
        return False
