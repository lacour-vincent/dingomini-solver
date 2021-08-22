from operator import itemgetter


class SmallRectangle:

    TOTAL_CARDS = 2
    WIDTH = 4
    HEIGHT = 2

    def __init__(self, cards):
        self.hash = hash(frozenset(cards.items()))
        self.__pattern = self.__create_pattern(cards)
        self.__id = [card.id for card in cards.values()]

    def is_pattern_valid(self):
        if (len(set(self.__id)) != self.TOTAL_CARDS):
            return False
        row_lines = [*self.__get_rows()]
        if (not self.__is_line_set_colors(row_lines, self.WIDTH)):
            return False
        lines = [*self.__get_columns()]
        return self.__is_line_set_colors(lines, self.HEIGHT)

    def __is_line_set_colors(self, lines, length):
        for line in lines:
            if (len(set([l.value for l in line])) != length):
                return False
        return True

    def __create_pattern(self, cards):
        l, r = itemgetter('left', "right")(cards)

        return [l.top_left, l.top_right, r.top_left, r.top_right,
                l.bottom_left, l.bottom_right, r.bottom_left, r.bottom_right]

    def __get_cell(self, i, j):
        return self.__pattern[(i * self.WIDTH) + j]

    def __get_rows(self):
        return [[self.__get_cell(i, j) for j in range(0, self.WIDTH)] for i in range(0, self.HEIGHT)]

    def __get_columns(self):
        return [[self.__get_cell(i, j) for i in range(0, self.HEIGHT)] for j in range(0, self.WIDTH)]
