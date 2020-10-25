import pygame


class Grid:
    @staticmethod
    def draw(window, wid):
        for i in range(wid // 50 + 1):
            if i % 3 == 0:
                pygame.draw.line(window, (0, 0, 0), (i * 50, 0), (i * 50, wid), 4)
                pygame.draw.line(window, (0, 0, 0), (0, i * 50), (wid, i * 50), 4)
            else:
                pygame.draw.line(window, (0, 0, 0), (i * 50, 0), (i * 50, wid), 2)
                pygame.draw.line(window, (0, 0, 0), (0, i * 50), (wid, i * 50), 2)
