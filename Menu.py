import pygame
from Game import Game
from Button import Button


class Menu:
    win_width = 450
    win_height = 600
    window = pygame.display.set_mode((win_width, win_height))
    Font = pygame.font.SysFont("comicsans", 160)
    pygame.init()

    @classmethod
    def main_menu(cls):

        buttons = Button.main_menu_buttons()
        run = True
        while run:
            run = Game.is_run()
            choice = cls.control_menu(buttons)
            if choice == 0:
                cls.diff_menu()
            if choice == 2:
                run = False
            cls.draw_menu(cls.window, buttons, cls.Font, 'main')
            Game.update()

    @classmethod
    def diff_menu(cls):
        buttons = Button.difficult_menu_buttons()
        run = True
        choice = -1
        while run:
            Game.update()
            run = Game.is_run()
            choice = cls.control_menu(buttons)
            if choice != -1:
                if choice == 0:
                    Game.run(0, cls.window, cls.win_width)
                elif choice == 1:
                    Game.run(1, cls.window, cls.win_width)
                elif choice == 2:
                    Game.run(2, cls.window, cls.win_width)
                run = False
            cls.draw_menu(cls.window, buttons, cls.Font, 'diff')

    @staticmethod
    def control_menu(buttons):
        if pygame.mouse.get_pressed()[0]:
            for b in buttons:
                if b.is_pressed(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    return b.value
        return -1

    @staticmethod
    def draw_menu(window, buttons, font, mode):
        window.fill((255, 255, 255))
        for b in buttons:
            b.draw(window)
        if mode == 'main':
            caption = font.render("Sudoku", 1, (0, 0, 0))
            window.blit(caption, (20, 40))
