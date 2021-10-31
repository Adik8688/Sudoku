import pygame
from Button import Button

WIN_WIDTH = 450
WIN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Menu:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font = pygame.font.SysFont("comicsans", 160)
        self.but_font = pygame.font.SysFont("comicsans", 70)

    def main_menu(self):
        buttons = self.get_menu_buttons()
        run = True
        while run:
            run = self.is_run()
            choice = self.handling_menu(buttons)
            if choice == 0:
                return 0
            if choice == 2:
                run = False
            self.draw_menu(buttons, self.font, 'main')
            self.update()
        return 2

    @staticmethod
    def get_menu_buttons():
        return [Button(100, 200 + i * 125, 250, 100, i, 'main') for i in range(3)]

    @staticmethod
    def get_diff_buttons():
        return [Button(100, 75 + i * 125, 250, 100, i, 'diff') for i in range(4)]

    def draw_menu(self, buttons, font, mode):
        self.window.fill(WHITE)

        for b in buttons:
            self.draw_buttons(b)

        if mode == 'main':
            caption = font.render("Sudoku", 1, BLACK)
            self.window.blit(caption, (20, 40))

    def draw_buttons(self, button):
        pygame.draw.rect(self.window, (200, 200, 200), (button.x, button.y, button.width, button.height))
        if button.mode == 'main':
            if button.value == 0:
                caption = self.but_font.render("Start", 1, BLACK)
                self.window.blit(caption, (button.x + 65, button.y + 30))
            elif button.value == 1:
                caption = self.but_font.render("Options", 1, BLACK)
                self.window.blit(caption, (button.x + 30, button.y + 30))
            elif button.value == 2:
                caption = self.but_font.render("Exit", 1, BLACK)
                self.window.blit(caption, (button.x + 75, button.y + 30))
        if button.mode == 'diff':
            if button.value == 0:
                caption = self.but_font.render("Easy", 1, BLACK)
                self.window.blit(caption, (button.x + 65, button.y + 30))
            elif button.value == 1:
                caption = self.but_font.render("Middle", 1, BLACK)
                self.window.blit(caption, (button.x + 45, button.y + 30))
            elif button.value == 2:
                caption = self.but_font.render("Hard", 1, BLACK)
                self.window.blit(caption, (button.x + 65, button.y + 30))
            elif button.value == 3:
                caption = self.but_font.render("Back", 1, BLACK)
                self.window.blit(caption, (button.x + 65, button.y + 30))

    @staticmethod
    def is_run():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    @staticmethod
    def update():
        pygame.time.delay(60)
        pygame.time.Clock().tick(60)
        pygame.display.update()

    def diff_menu(self):
        buttons = self.get_diff_buttons()
        run = True
        choice = -1
        while run:
            self.update()
            run = self.is_run()
            choice = self.handling_menu(buttons)

            if choice != -1:
                run = False
            self.draw_menu(buttons, self.font, 'diff')

        if choice != -1:
            return choice

    @staticmethod
    def handling_menu(buttons):
        if pygame.mouse.get_pressed()[0]:
            for b in buttons:
                if b.is_pressed(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    return b.value
        return -1
