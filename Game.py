import pygame
from Spot import Spot
from Generator import Generator
from Mark import Mark

WIN_WIDTH = 450
WIN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (225, 122, 122)
REDGRAY = (255, 189, 189)


class Game:
    def __init__(self, lvl):
        self.lvl = lvl
        self.sudoku = Generator(lvl)

        self.font = pygame.font.SysFont("comicsans", 90)
        self.sub_font = pygame.font.SysFont("comicsans", 35)
        self.font_n_big = pygame.font.SysFont("comicsans", 70)
        self.font_n_small = pygame.font.SysFont("comicsans", 22)
        pygame.init()

        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Sudoku by AD")

        self.mark = Mark()

        config = self.sudoku.get_grid()[0]
        self.spots = self.make_spots(config)

    @staticmethod
    def make_spots(config):
        spots = []
        for i in range(9):
            row = []
            for j in range(9):
                const = True if config[i][j] != 0 else False
                row.append(Spot(50 * j, 50 * i, config[i][j], Spot.get_square(j, i), const))
            spots.append(row)
        return spots

    def run(self):
        run = True
        while run:
            run = self.is_run()
            if self.is_solved():
                self.end_game()
                run = False

            self.control()
            self.draw_game()
            self.update()

    def control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.mark.move_up()
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.mark.move_down()
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.mark.move_right()
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.mark.move_left()
        elif pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            for y_cor, row in enumerate(self.spots):
                for x_cor, spot in enumerate(row):
                    if spot.is_pressed(x, y):
                        self.mark.x_cor = x_cor
                        self.mark.y_cor = y_cor
                        break

        if keys[pygame.K_1] or keys[pygame.K_KP1]:
            self.put_number(keys, 1)

        if keys[pygame.K_2] or keys[pygame.K_KP2]:
            self.put_number(keys, 2)

        if keys[pygame.K_3] or keys[pygame.K_KP3]:
            self.put_number(keys, 3)

        if keys[pygame.K_4] or keys[pygame.K_KP4]:
            self.put_number(keys, 4)

        if keys[pygame.K_5] or keys[pygame.K_KP5]:
            self.put_number(keys, 5)

        if keys[pygame.K_6] or keys[pygame.K_KP6]:
            self.put_number(keys, 6)

        if keys[pygame.K_7] or keys[pygame.K_KP7]:
            self.put_number(keys, 7)

        if keys[pygame.K_8] or keys[pygame.K_KP8]:
            self.put_number(keys, 8)

        if keys[pygame.K_9] or keys[pygame.K_KP9]:
            self.put_number(keys, 9)

        if keys[pygame.K_BACKSPACE]:
            self.put_number(keys, 0)

    def put_number(self, keys, value):
        this_spot = self.spots[self.mark.y_cor][self.mark.x_cor]
        if not this_spot.immutable:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                this_spot.value = 0
                if value in this_spot.suspected_values:
                    this_spot.suspected_values.remove(value)
                else:
                    this_spot.suspected_values.append(value)
            else:
                this_spot.suspected_values = []
                this_spot.value = value

                for i in range(9):
                    if value in self.spots[self.mark.y_cor][i].suspected_values:
                        self.spots[self.mark.y_cor][i].suspected_values.remove(value)
                    if value in self.spots[i][self.mark.x_cor].suspected_values:
                        self.spots[i][self.mark.x_cor].suspected_values.remove(value)

                for row in self.spots:
                    for spot in row:
                        if spot.square_id == this_spot.square_id:
                            if value in spot.suspected_values:
                                spot.suspected_values.remove(value)

    def draw_game(self):
        self.window.fill(WHITE)
        self.draw_numbers()
        self.draw_grid()
        self.draw_mark()

    def draw_numbers(self):
        for y_cor, row in enumerate(self.spots):
            for x_cor, spot in enumerate(row):
                color = WHITE
                if ((x_cor == self.mark.x_cor or y_cor == self.mark.y_cor) and not (
                        x_cor == self.mark.x_cor and y_cor == self.mark.y_cor)) or spot.square_id == \
                        self.spots[self.mark.y_cor][
                            self.mark.x_cor].square_id:
                    color = GRAY
                if spot.is_collide(self.spots):
                    if color == GRAY:
                        color = REDGRAY
                    else:
                        color = RED

                self.draw_spot(spot, color)

    def draw_spot(self, spot, color):
        pygame.draw.rect(self.window, color, (spot.x, spot.y, spot.size, spot.size))
        if spot.value != 0:
            number = self.font_n_big.render(str(spot.value), 1, (0, 0, 0))
            self.window.blit(number, (spot.x + 12, spot.y + 4))

        if spot.suspected_values:
            for number in spot.suspected_values:
                value = self.font_n_small.render(str(number), 1, (0, 0, 0))
                self.window.blit(value, (spot.x + spot.numbers_cor[number][0], spot.y + spot.numbers_cor[number][1]))

    def draw_mark(self):
        pygame.draw.polygon(self.window, RED, [(self.mark.x_cor * 50, self.mark.y_cor * 50), (
            (self.mark.x_cor + 1) * 50, self.mark.y_cor * 50), ((self.mark.x_cor + 1) * 50, (self.mark.y_cor + 1) * 50),
                                               (self.mark.x_cor * 50, (self.mark.y_cor + 1) * 50)], 8)

    def draw_grid(self):
        for i in range(WIN_WIDTH // 50 + 1):
            if i % 3 == 0:
                pygame.draw.line(self.window, (0, 0, 0), (i * 50, 0), (i * 50, WIN_WIDTH), 4)
                pygame.draw.line(self.window, (0, 0, 0), (0, i * 50), (WIN_WIDTH, i * 50), 4)
            else:
                pygame.draw.line(self.window, (0, 0, 0), (i * 50, 0), (i * 50, WIN_WIDTH), 2)
                pygame.draw.line(self.window, (0, 0, 0), (0, i * 50), (WIN_WIDTH, i * 50), 2)

    @staticmethod
    def update():
        pygame.time.delay(60)
        pygame.time.Clock().tick(60)
        pygame.display.update()

    @staticmethod
    def is_run():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def is_solved(self):
        for row in self.spots:
            for spot in row:
                if spot.value == 0 or spot.is_collide(self.spots):
                    return False
        return True

    def end_game(self):
        pygame.draw.rect(self.window, BLACK, (50, 50, 350, 250))
        pygame.draw.rect(self.window, WHITE, (52, 52, 348, 248))

        caption = self.font.render("Congrats!", 1, BLACK)
        self.window.blit(caption, (75, 70))

        caption = self.sub_font.render("Press space to continue: ", 1, BLACK)
        self.window.blit(caption, (75, 200))

        run = True
        while run:
            run = Game.is_run()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                run = False
            Game.update()
