class Square:

    TOTAL_CARDS = 4
    WIDTH = 4
    HEIGHT = 4

    def __init__(self, top_left_card, top_right_card, bottom_right_card, bottom_left_card):
        self.__pattern = self.__create_pattern(top_left_card, top_right_card, bottom_right_card, bottom_left_card)

    def is_pattern_valid(self):
        lines = [*self.__get_rows(), *self.__get_columns(), *self.__get_diagonals()]
        for line in lines:
            if (len(set([l.value for l in line])) != self.WIDTH):
                return False
        return True

    def __create_pattern(self, top_left_card, top_right_card, bottom_right_card, bottom_left_card):
        return [top_left_card.top_left, top_left_card.top_right, top_right_card.top_left, top_right_card.top_right,
                top_left_card.bottom_left, top_left_card.bottom_right,  top_right_card.bottom_left, top_right_card.bottom_right,
                bottom_left_card.top_left, bottom_left_card.top_right, bottom_right_card.top_left, bottom_right_card.top_right,
                bottom_left_card.bottom_left, bottom_left_card.bottom_right,  bottom_right_card.bottom_left, bottom_right_card.bottom_right,
                ]

    def __get_cell(self, i, j):
        return self.__pattern[(i * self.WIDTH) + j]

    def __get_rows(self):
        return [[self.__get_cell(i, j) for j in range(0, self.WIDTH)] for i in range(0, self.HEIGHT)]

    def __get_columns(self):
        return [[self.__get_cell(i, j) for i in range(0, self.WIDTH)] for j in range(0, self.HEIGHT)]

    def __get_diagonals(self):
        return [
            [self.__get_cell(0, 0), self.__get_cell(1, 1), self.__get_cell(2, 2), self.__get_cell(3, 3)],
            [self.__get_cell(3, 0), self.__get_cell(2, 1), self.__get_cell(1, 2), self.__get_cell(0, 3)]
        ]