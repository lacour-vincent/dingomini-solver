from PIL import Image, ImageDraw
from core.color import Color

image = Image.new('RGBA', (200, 200))
draw = ImageDraw.Draw(image)
draw.ellipse((20, 180, 180, 20), fill='blue', outline='blue')
draw.point((100, 100), 'red')
image.save('test.png')


class Drawer:

    CELL_SIZE = 50

    def __init__(self, pattern):
        self.pattern = pattern
        self.width = self.CELL_SIZE * (pattern.WIDTH + 1)
        self.height = self.CELL_SIZE * (pattern.HEIGHT + 1)

    def draw_and_save_solutions(self, solutions):
        for index, solution in enumerate(solutions):
            im = Image.new('RGB', (self.width, self.height), "white")
            draw = ImageDraw.Draw(im)
            self.__draw_card(solution[0], 0, 0, draw)
            self.__draw_card(solution[1], 3 * self.CELL_SIZE, 0, draw)
            self.__draw_card(solution[2], 3 * self.CELL_SIZE, 3 * self.CELL_SIZE, draw)
            self.__draw_card(solution[3], 0, 3 * self.CELL_SIZE, draw)
            im.save(F"solutions/solution-{index}.jpg", quality=95)
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
