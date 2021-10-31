import random


class Generator:
    def __init__(self, lvl):
        self.lvl = lvl
        self.grid = Generator.get_seed()
        self.grid_solved = self.grid.copy()
        self.mod_grid()

    def get_grid(self):
        return self.grid, self.grid_solved

    @staticmethod
    def get_seed():
        # n = random.randint(0, 19)
        n = 0
        file = open("Seeds")
        for i, line in enumerate(file):
            if i == n:
                # 1234 5676 4566... -> [[1, 2, 3, 4], [5, 6, 7, 6]......
                seed = list(map(list, line.split()))
                for x, row in enumerate(seed):
                    seed[x] = list(map(int, row))
        return seed

    def mod_grid(self):
        self.change_columns()
        self.change_rows()
        self.perm_nums()
        self.fill_with_zeros()

    def fill_with_zeros(self):
        n = 5 + self.lvl
        for row in self.grid:
            while row.count(0) < n:
                row[random.randint(0, 8)] = 0

    def change_rows(self):
        for i in range(3):
            for _ in range(5):
                row1 = random.randint(0 + i * 3, 2 + i * 3)
                row2 = random.randint(0 + i * 3, 2 + i * 3)
                self.grid[row1], self.grid[row2] = self.grid[row2], self.grid[row1]
        for i in range(5):
            sq1 = random.randint(0, 2)
            sq2 = random.randint(0, 2)
            for j in range(3):
                self.grid[sq1 * 3 + j], self.grid[sq2 * 3 + j] = self.grid[sq2 * 3 + j], self.grid[sq1 * 3 + j]

    def change_columns(self):
        for i in range(3):
            for _ in range(5):
                column1 = random.randint(0 + i * 3, 2 + i * 3)
                column2 = random.randint(0 + i * 3, 2 + i * 3)
                for j in range(9):
                    self.grid[j][column1], self.grid[j][column2] = self.grid[j][column2], self.grid[j][column1]
        for _ in range(5):
            sq1 = random.randint(0, 2)
            sq2 = random.randint(0, 2)
            for j in range(3):
                for i in range(9):
                    self.grid[i][sq1 * 3 + j], self.grid[i][sq2 * 3 + j] = self.grid[i][sq2 * 3 + j], self.grid[i][
                        sq1 * 3 + j]

    def perm_nums(self):
        for _ in range(5):
            a, b = random.randint(1, 9), random.randint(1, 9)
            for row in self.grid:
                for spot in row:
                    if spot == a:
                        spot = b
                    elif spot == b:
                        spot = a
