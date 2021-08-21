class GreatSquare:

    TOTAL_CARDS = 9
    WIDTH = 6
    HEIGHT = 6

    def __init__(self, top_left_card, top_middle_card, top_right_card,
                 center_right_card, center_middle_card, center_left_card,
                 bottom_left_card, bottom_middle_card, bottom_right_card):

        self.__pattern = self.__create_pattern(top_left_card, top_middle_card, top_right_card,
                                               center_right_card, center_middle_card, center_left_card,
                                               bottom_left_card, bottom_middle_card, bottom_right_card)

        self.__id = [top_left_card.id, top_middle_card.id, top_right_card.id,
                     center_right_card.id, center_middle_card.id, center_left_card.id,
                     bottom_left_card.id, bottom_middle_card.id, bottom_right_card.id]

    def is_pattern_valid(self):
        if (len(set(self.__id)) != self.TOTAL_CARDS):
            return False
        lines = [*self.__get_rows(), *self.__get_columns()]
        return self.__is_line_set_colors(lines, self.WIDTH)

    def __is_line_set_colors(self, lines, length):
        for line in lines:
            if (len(set([l.value for l in line])) != length):
                return False
        return True

    def __create_pattern(self, top_left_card, top_middle_card, top_right_card,
                         center_right_card, center_middle_card, center_left_card,
                         bottom_left_card, bottom_middle_card, bottom_right_card):

        return [top_left_card.top_left, top_left_card.top_right, top_middle_card.top_left, top_middle_card.top_right, top_right_card.top_left, top_right_card.top_right,
                top_left_card.bottom_left, top_left_card.bottom_right, top_middle_card.bottom_left, top_middle_card.bottom_right, top_right_card.bottom_left, top_right_card.bottom_right,

                center_left_card.top_left, center_left_card.top_right, center_middle_card.top_left, center_middle_card.top_right, center_right_card.top_left,  center_right_card.top_right,
                center_left_card.bottom_left, center_left_card.bottom_right, center_middle_card.bottom_left, center_middle_card.bottom_right, center_right_card.bottom_left,  center_right_card.bottom_right,

                bottom_left_card.top_left, bottom_left_card.top_right, bottom_middle_card.top_left, bottom_middle_card.top_right, bottom_right_card.top_left, bottom_right_card.top_right,
                bottom_left_card.bottom_left, bottom_left_card.bottom_right, bottom_middle_card.bottom_left, bottom_middle_card.bottom_right,  bottom_right_card.bottom_left, bottom_right_card.bottom_right,
                ]

    def __get_cell(self, i, j):
        return self.__pattern[(i * self.WIDTH) + j]

    def __get_rows(self):
        return [[self.__get_cell(i, j) for j in range(0, self.WIDTH)] for i in range(0, self.HEIGHT)]

    def __get_columns(self):
        return [[self.__get_cell(i, j) for i in range(0, self.HEIGHT)] for j in range(0, self.WIDTH)]

    def __get_diagonals(self):
        return [
            [self.__get_cell(0, 0), self.__get_cell(1, 1), self.__get_cell(
                2, 2), self.__get_cell(3, 3), self.__get_cell(4, 4), self.__get_cell(5, 5)],
            [self.__get_cell(5, 0), self.__get_cell(4, 1), self.__get_cell(
                3, 2), self.__get_cell(2, 3), self.__get_cell(1, 4), self.__get_cell(0, 5)],
        ]
