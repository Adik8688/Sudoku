import pygame


class Button:
    Font = pygame.font.SysFont("comicsans", 70)

    # instrukcja do napisów
    # scor_e = pygame.font.SysFont("comicsans", 50).render("Score: " + str(score1), 1, (255, 255, 255))
    # self.window.blit(scor_e, (30, 705))
    @classmethod
    def main_menu_buttons(cls):
        buttons = []
        for i in range(3):
            buttons.append(Button(100, 200 + i * 125, 250, 100, i, 'main'))
        return buttons
    @classmethod
    def difficult_menu_buttons(cls):
        buttons = []
        for i in range(4):
            buttons.append(Button(100, 75 + i * 125, 250, 100, i, 'diff'))
        return buttons

    def __init__(self, x, y, x1, y1, value, mode):
        self.x = x
        self.y = y
        self.width = x1
        self.height = y1
        self.value = value
        self.mode = mode

    def is_pressed(self, x, y):
        if x > self.x and x < self.x + self.width and y > self.y and y < self.y + self.height:
            return True
        return False

    def draw(self, window):
        pygame.draw.rect(window, (200, 200, 200), (self.x, self.y, self.width, self.height))
        if self.mode == 'main':
            if self.value == 0:
                caption = Button.Font.render("Start", 1, (0, 0, 0))
                window.blit(caption, (self.x + 65, self.y + 30))
            elif self.value == 1:
                caption = Button.Font.render("Options", 1, (0, 0, 0))
                window.blit(caption, (self.x + 30, self.y + 30))
            elif self.value == 2:
                caption = Button.Font.render("Exit", 1, (0, 0, 0))
                window.blit(caption, (self.x + 75, self.y + 30))
        if self.mode == 'diff':
            if self.value == 0:
                caption = Button.Font.render("Easy", 1, (0, 0, 0))
                window.blit(caption, (self.x + 65, self.y + 30))
            elif self.value == 1:
                caption = Button.Font.render("Middle", 1, (0, 0, 0))
                window.blit(caption, (self.x + 45, self.y + 30))
            elif self.value == 2:
                caption = Button.Font.render("Hard", 1, (0, 0, 0))
                window.blit(caption, (self.x + 65, self.y + 30))
            elif self.value == 3:
                caption = Button.Font.render("Back", 1, (0, 0, 0))
                window.blit(caption, (self.x + 65, self.y + 30))
