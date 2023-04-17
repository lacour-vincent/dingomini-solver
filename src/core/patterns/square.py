from operator import itemgetter


class Square:
    TOTAL_CARDS = 4
    WIDTH = 4
    HEIGHT = 4

    def __init__(self, cards):
        self.hash = hash(frozenset(cards.items()))
        self.__pattern = self.__create_pattern(cards)
        self.__id = [card.id for card in cards.values()]

    def is_pattern_valid(self):
        if len(set(self.__id)) != self.TOTAL_CARDS:
            return False
        lines = [
            *self.__get_rows(),
            *self.__get_columns(),
            *self.__get_diagonals(),
        ]
        return self.__is_line_set_colors(lines, self.WIDTH)

    def __is_line_set_colors(self, lines, length):
        for line in lines:
            if len(set([cell.value for cell in line])) != length:
                return False
        return True

    def __create_pattern(self, cards):
        tl, tr, bl, br = itemgetter("top_left", "top_right", "bottom_left", "bottom_right")(cards)
        return [
            tl.top_left,
            tl.top_right,
            tr.top_left,
            tr.top_right,
            tl.bottom_left,
            tl.bottom_right,
            tr.bottom_left,
            tr.bottom_right,
            bl.top_left,
            bl.top_right,
            br.top_left,
            br.top_right,
            bl.bottom_left,
            bl.bottom_right,
            br.bottom_left,
            br.bottom_right,
        ]

    def __get_cell(self, i, j):
        return self.__pattern[(i * self.WIDTH) + j]

    def __get_rows(self):
        return [[self.__get_cell(i, j) for j in range(0, self.WIDTH)] for i in range(0, self.HEIGHT)]

    def __get_columns(self):
        return [[self.__get_cell(i, j) for i in range(0, self.HEIGHT)] for j in range(0, self.WIDTH)]

    def __get_diagonals(self):
        return [
            [
                self.__get_cell(0, 0),
                self.__get_cell(1, 1),
                self.__get_cell(2, 2),
                self.__get_cell(3, 3),
            ],
            [
                self.__get_cell(3, 0),
                self.__get_cell(2, 1),
                self.__get_cell(1, 2),
                self.__get_cell(0, 3),
            ],
        ]
