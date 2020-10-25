import pygame
from Spot import Spot
from Generator import Generator
from Mark import Mark
from Grid import Grid


class Game:
    Font = pygame.font.SysFont("comicsans", 90)
    Sub_Font = pygame.font.SysFont("comicsans", 35)

    @classmethod
    def run(cls, lvl, window, width):
        pygame.init()
        sudoku = Generator(lvl)
        config = sudoku.get_grid()[0]
        spots = Spot.make_spots(config)
        pygame.display.set_caption("Sudoku by AD")
        run = True
        while run:
            run = Game.is_run()
            if Game.is_solved(spots):
                cls.end_game(window)
                run = False

            Game.control(spots)
            Game.draw_game(window, width, spots)
            Game.update()

    @staticmethod
    def control(spots):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            Mark.move_up()
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            Mark.move_down()
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            Mark.move_right()
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            Mark.move_left()
        elif pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            for y_cor, row in enumerate(spots):
                for x_cor, spot in enumerate(row):
                    if spot.is_pressed(x, y):
                        Mark.x_cor = x_cor
                        Mark.y_cor = y_cor
                        break

        if keys[pygame.K_1] or keys[pygame.K_KP1]:
            Game.put_number(keys, spots, 1)

        if keys[pygame.K_2] or keys[pygame.K_KP2]:
            Game.put_number(keys, spots, 2)

        if keys[pygame.K_3] or keys[pygame.K_KP3]:
            Game.put_number(keys, spots, 3)

        if keys[pygame.K_4] or keys[pygame.K_KP4]:
            Game.put_number(keys, spots, 4)

        if keys[pygame.K_5] or keys[pygame.K_KP5]:
            Game.put_number(keys, spots, 5)

        if keys[pygame.K_6] or keys[pygame.K_KP6]:
            Game.put_number(keys, spots, 6)

        if keys[pygame.K_7] or keys[pygame.K_KP7]:
            Game.put_number(keys, spots, 7)

        if keys[pygame.K_8] or keys[pygame.K_KP8]:
            Game.put_number(keys, spots, 8)

        if keys[pygame.K_9] or keys[pygame.K_KP9]:
            Game.put_number(keys, spots, 9)

        if keys[pygame.K_BACKSPACE]:
            Game.put_number(keys, spots, 0)

    @staticmethod
    def put_number(keys, spots, value):
        if not spots[Mark.y_cor][Mark.x_cor].constant:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                spots[Mark.y_cor][Mark.x_cor].value = 0
                if value in spots[Mark.y_cor][Mark.x_cor].suspect_values:
                    spots[Mark.y_cor][Mark.x_cor].suspect_values.remove(value)
                else:
                    spots[Mark.y_cor][Mark.x_cor].suspect_values.append(value)
            else:
                spots[Mark.y_cor][Mark.x_cor].suspect_values = []
                spots[Mark.y_cor][Mark.x_cor].value = value
                for i in range(9):
                    if value in spots[Mark.y_cor][i].suspect_values:
                        spots[Mark.y_cor][i].suspect_values.remove(value)
                    if value in spots[i][Mark.x_cor].suspect_values:
                        spots[i][Mark.x_cor].suspect_values.remove(value)
                for row in spots:
                    for spot in row:
                        if spot.square_id == spots[Mark.y_cor][Mark.x_cor].square_id:
                            if value in spot.suspect_values:
                                spot.suspect_values.remove(value)

    @staticmethod
    def draw_game(window, width, spots):
        window.fill((255, 255, 255))
        for y_cor, row in enumerate(spots):
            for x_cor, spot in enumerate(row):
                color = "white"

                if ((x_cor == Mark.x_cor or y_cor == Mark.y_cor) and not (
                        x_cor == Mark.x_cor and y_cor == Mark.y_cor)) or spot.square_id == spots[Mark.y_cor][
                    Mark.x_cor].square_id:
                    color = "gray"
                if spot.is_collide(spots):
                    if color == "gray":
                        color = "redgray"
                    else:
                        color = "red"
                spot.draw(window, color)
        Grid.draw(window, width)
        Mark.draw(window)

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

    @staticmethod
    def is_solved(spots):
        for row in spots:
            for spot in row:
                if spot.value == 0 or spot.is_collide(spots):
                    return False
        return True

    @classmethod
    def end_game(cls, window):
        pygame.draw.rect(window, (0, 0, 0), (50, 50, 350, 250))
        pygame.draw.rect(window, (255, 255, 255), (52, 52, 348, 248))
        caption = cls.Font.render("Congrats!", 1, (0, 0, 0))
        window.blit(caption, (75, 70))
        caption = cls.Sub_Font.render("Press space to continue: ", 1, (0, 0, 0))
        window.blit(caption, (75, 200))
        run = True
        while run:
            run = Game.is_run()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                run = False
            Game.update()