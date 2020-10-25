import pygame


class Mark:
    x_cor = 4
    y_cor = 4

    @classmethod
    def draw(cls, window):
        pygame.draw.polygon(window, (0, 255, 0), [(cls.x_cor * 50, cls.y_cor * 50), (
            (cls.x_cor + 1) * 50, cls.y_cor * 50), ((cls.x_cor + 1) * 50, (cls.y_cor + 1) * 50),
                                                  (cls.x_cor * 50, (cls.y_cor + 1) * 50)], 8)

    @classmethod
    def move_up(cls):
        if cls.y_cor > 0:
            cls.y_cor -= 1

    @classmethod
    def move_down(cls):
        if cls.y_cor < 8:
            cls.y_cor += 1

    @classmethod
    def move_right(cls):
        if cls.x_cor < 8:
            cls.x_cor += 1

    @classmethod
    def move_left(cls):
        if cls.x_cor > 0:
            cls.x_cor -= 1
