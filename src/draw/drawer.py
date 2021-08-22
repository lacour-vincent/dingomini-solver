from PIL import Image, ImageDraw
from core.color import Color


class Drawer:

    CELL_SIZE = 50

    def save_small_rectangle_solutions(self, pattern, solutions):
        width = self.CELL_SIZE * (pattern.WIDTH + 1)
        height = self.CELL_SIZE * (pattern.HEIGHT)
        for index, solution in enumerate(solutions):
            im = Image.new('RGB', (width, height), "white")
            draw = ImageDraw.Draw(im)
            self.__draw_card(solution["left"], 0, 0, draw)
            self.__draw_card(solution["right"], 3 * self.CELL_SIZE, 0, draw)
            im.save(F"solutions/small_rectangle/solution-{index}.jpg", quality=95)
            im.close()

    def save_square_solutions(self, pattern, solutions):
        width = self.CELL_SIZE * (pattern.WIDTH + 1)
        height = self.CELL_SIZE * (pattern.HEIGHT + 1)
        for index, solution in enumerate(solutions):
            im = Image.new('RGB', (width, height), "white")
            draw = ImageDraw.Draw(im)
            self.__draw_card(solution["top_left"], 0, 0, draw)
            self.__draw_card(solution["top_right"], 3 * self.CELL_SIZE, 0, draw)
            self.__draw_card(solution["bottom_left"], 0, 3 * self.CELL_SIZE, draw)
            self.__draw_card(solution["bottom_right"], 3 * self.CELL_SIZE, 3 * self.CELL_SIZE, draw)
            im.save(F"solutions/square/solution-{index}.jpg", quality=95)
            im.close()

    def save_rectangle_solutions(self, pattern, solutions):
        width = self.CELL_SIZE * (pattern.WIDTH + 2)
        height = self.CELL_SIZE * (pattern.HEIGHT + 1)
        for index, solution in enumerate(solutions):
            im = Image.new('RGB', (width, height), "white")
            draw = ImageDraw.Draw(im)
            self.__draw_card(solution["top_left"], 0, 0, draw)
            self.__draw_card(solution["top_middle"], 3 * self.CELL_SIZE, 0, draw)
            self.__draw_card(solution["top_right"], 6 * self.CELL_SIZE, 0, draw)
            self.__draw_card(solution["bottom_left"], 0, 3 * self.CELL_SIZE, draw)
            self.__draw_card(solution["bottom_middle"], 3 * self.CELL_SIZE, 3 * self.CELL_SIZE, draw)
            self.__draw_card(solution["bottom_right"], 6 * self.CELL_SIZE, 3 * self.CELL_SIZE, draw)
            im.save(F"solutions/rectangle/solution-{index}.jpg", quality=95)
            im.close()

    def save_great_square_solutions(self, pattern, solutions):
        width = self.CELL_SIZE * (pattern.WIDTH + 2)
        height = self.CELL_SIZE * (pattern.HEIGHT + 2)
        for index, solution in enumerate(solutions):
            im = Image.new('RGB', (width, height), "white")
            draw = ImageDraw.Draw(im)
            self.__draw_card(solution["top_left"], 0, 0, draw)
            self.__draw_card(solution["top_middle"], 3 * self.CELL_SIZE, 0, draw)
            self.__draw_card(solution["top_right"], 6 * self.CELL_SIZE, 0, draw)
            self.__draw_card(solution["center_left"], 0, 3 * self.CELL_SIZE, draw)
            self.__draw_card(solution["center_middle"], 3 * self.CELL_SIZE, 3 * self.CELL_SIZE, draw)
            self.__draw_card(solution["center_right"], 6 * self.CELL_SIZE, 3 * self.CELL_SIZE, draw)
            self.__draw_card(solution["bottom_left"], 0, 6 * self.CELL_SIZE, draw)
            self.__draw_card(solution["bottom_middle"], 3 * self.CELL_SIZE, 6 * self.CELL_SIZE, draw)
            self.__draw_card(solution["bottom_right"], 6 * self.CELL_SIZE, 6 * self.CELL_SIZE, draw)
            im.save(F"solutions/great_square/solution-{index}.jpg", quality=95)
            im.close()

    def __draw_card(self, card, x, y, drawer):
        drawer.rectangle((x, y, x + self.CELL_SIZE, y + self.CELL_SIZE),
                         fill=self.__get_color(card.top_left), outline="black")
        drawer.rectangle((x + self.CELL_SIZE, y, x + 2 * self.CELL_SIZE, y + self.CELL_SIZE),
                         fill=self.__get_color(card.top_right), outline="black")
        drawer.rectangle((x + self.CELL_SIZE, y + self.CELL_SIZE, x + 2 * self.CELL_SIZE, y + 2 * self.CELL_SIZE),
                         fill=self.__get_color(card.bottom_right), outline="black")
        drawer.rectangle((x, y + self.CELL_SIZE, x + self.CELL_SIZE, y + 2 * self.CELL_SIZE),
                         fill=self.__get_color(card.bottom_left), outline="black")

    def __get_color(self, color):
        if color.value is Color.YELLOW.value:
            return "yellow"
        if color.value is Color.GREEN.value:
            return "green"
        if color.value is Color.BLUE.value:
            return "blue"
        if color.value is Color.GRAY.value:
            return "gray"
        if color.value is Color.PINK.value:
            return "pink"
        if color.value is Color.RED.value:
            return "red"
        return "black"
