import pygame

class Spot:
    colors = {"white": (255, 255, 255), "gray": (200, 200, 200), "red": (255, 122, 122), "redgray": (255, 189, 189)
              }
    numbers_pos = {1: (6, 4), 2: (22, 4), 3: (38, 5), 4: (6, 20), 5: (22, 20), 6: (38, 20), 7: (6, 36), 8: (22, 36),
                   9: (38, 36)}
    pygame.font.init()
    Font_big = pygame.font.SysFont("comicsans", 70)
    Font_small = pygame.font.SysFont("comicsans", 22)

    @classmethod
    def make_spots(cls, config):
        spots = []
        for i in range(9):
            row = []
            for j in range(9):
                const = True if config[i][j] != 0 else False
                row.append(Spot(50 * j, 50 * i, config[i][j], Spot.get_square(j, i), const))
            spots.append(row)
        return spots

    @staticmethod
    def get_square(x, y):
        squares = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        return squares[y // 3][x // 3]

    def __init__(self, x, y, value, sq, constant=False):
        self.x = x
        self.y = y
        self.size = 50
        self.square_id = sq
        self.value = value
        self.suspect_values = []
        self.constant = constant

    def is_pressed(self, x, y):
        if (x > self.x) and (x < self.x + self.size) and (y > self.y) and (y < self.y + self.size):
            return True
        return False

    def draw(self, window, color):
        pygame.draw.rect(window, Spot.colors[color], (self.x, self.y, self.size, self.size))
        if self.value != 0:
            number = Spot.Font_big.render(str(self.value), 1, (0, 0, 0))
            window.blit(number, (self.x + 12, self.y + 4))
        if self.suspect_values:
            for number in self.suspect_values:
                value = Spot.Font_small.render(str(number), 1, (0, 0, 0))
                window.blit(value, (self.x + Spot.numbers_pos[number][0], self.y + Spot.numbers_pos[number][1]))

    def is_collide(self, spots):
        for row in spots:
            for spot in row:
                if not (spot.x == self.x and spot.y == self.y):
                    if spot.value == self.value and self.value != 0:
                        if spot.x == self.x or spot.y == self.y or spot.square_id == self.square_id:
                            return True
        return False
