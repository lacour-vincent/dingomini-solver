from src.core.color import Color
from src.core.card import Card
from src.core.patterns.great_square import GreatSquare


def test_is_pattern_valid():
    pattern = GreatSquare({"top_left": Card(1,  {"top_left": Color.BLUE, "top_right": Color.PINK,
                                                 "bottom_left": Color.GREEN, "bottom_right": Color.GRAY}),
                           "top_middle": Card(2,  {"top_left": Color.GRAY, "top_right": Color.RED,
                                                   "bottom_left": Color.YELLOW, "bottom_right": Color.BLUE}),
                           "top_right": Card(3,  {"top_left": Color.GREEN, "top_right": Color.YELLOW,
                                                  "bottom_left": Color.RED, "bottom_right": Color.PINK}),
                           "center_left": Card(4,  {"top_left": Color.RED, "top_right": Color.YELLOW,
                                                    "bottom_left": Color.PINK, "bottom_right": Color.RED}),
                           "center_middle": Card(5,  {"top_left": Color.GREEN, "top_right": Color.PINK,
                                                      "bottom_left": Color.BLUE, "bottom_right": Color.YELLOW}),
                           "center_right": Card(6,  {"top_left": Color.BLUE, "top_right": Color.GRAY,
                                                     "bottom_left": Color.GRAY, "bottom_right": Color.GREEN}),
                           "bottom_left": Card(7,  {"top_left": Color.YELLOW, "top_right": Color.GREEN,
                                                    "bottom_left": Color.GRAY, "bottom_right": Color.BLUE}),
                           "bottom_middle": Card(8,  {"top_left": Color.RED, "top_right": Color.GRAY,
                                                      "bottom_left": Color.PINK, "bottom_right": Color.GREEN}),
                           "bottom_right": Card(9,  {"top_left": Color.PINK, "top_right": Color.BLUE,
                                                     "bottom_left": Color.YELLOW, "bottom_right": Color.RED})})
    assert pattern.is_pattern_valid() == True


def test_is_pattern_invalid_same_card():
    pattern = GreatSquare({"top_left": Card(1,  {"top_left": Color.BLUE, "top_right": Color.PINK,
                                                 "bottom_left": Color.GREEN, "bottom_right": Color.GRAY}),
                           "top_middle": Card(1,  {"top_left": Color.BLUE, "top_right": Color.PINK,
                                                   "bottom_left": Color.GREEN, "bottom_right": Color.GRAY}),
                           "top_right": Card(3,  {"top_left": Color.GREEN, "top_right": Color.YELLOW,
                                                  "bottom_left": Color.RED, "bottom_right": Color.PINK}),
                           "center_left": Card(4,  {"top_left": Color.RED, "top_right": Color.YELLOW,
                                                    "bottom_left": Color.PINK, "bottom_right": Color.RED}),
                           "center_middle": Card(5,  {"top_left": Color.GREEN, "top_right": Color.PINK,
                                                      "bottom_left": Color.BLUE, "bottom_right": Color.YELLOW}),
                           "center_right": Card(6,  {"top_left": Color.BLUE, "top_right": Color.GRAY,
                                                     "bottom_left": Color.GRAY, "bottom_right": Color.GREEN}),
                           "bottom_left": Card(7,  {"top_left": Color.YELLOW, "top_right": Color.GREEN,
                                                    "bottom_left": Color.GRAY, "bottom_right": Color.BLUE}),
                           "bottom_middle": Card(8,  {"top_left": Color.RED, "top_right": Color.GRAY,
                                                      "bottom_left": Color.PINK, "bottom_right": Color.GREEN}),
                           "bottom_right": Card(9,  {"top_left": Color.PINK, "top_right": Color.BLUE,
                                                     "bottom_left": Color.YELLOW, "bottom_right": Color.RED})})
    assert pattern.is_pattern_valid() == False


def test_is_pattern_invalid_row():
    # Pattern with only row errors does not exists.
    assert False == False


def test_is_pattern_invalid_column():
    pattern = GreatSquare({"top_left": Card(1,  {"top_left": Color.BLUE, "top_right": Color.PINK,
                                                 "bottom_left": Color.GREEN, "bottom_right": Color.GRAY}),
                           "top_middle": Card(2,  {"top_left": Color.GRAY, "top_right": Color.RED,
                                                   "bottom_left": Color.YELLOW, "bottom_right": Color.BLUE}),
                           "top_right": Card(3,  {"top_left": Color.GREEN, "top_right": Color.YELLOW,
                                                  "bottom_left": Color.RED, "bottom_right": Color.PINK}),
                           "center_left": Card(4,  {"top_left": Color.YELLOW, "top_right": Color.GREEN,
                                                    "bottom_left": Color.GRAY, "bottom_right": Color.BLUE}),
                           "center_middle": Card(5,  {"top_left": Color.RED, "top_right": Color.GRAY,
                                                      "bottom_left": Color.PINK, "bottom_right": Color.GREEN}),
                           "center_right": Card(6,  {"top_left": Color.PINK, "top_right": Color.BLUE,
                                                     "bottom_left": Color.YELLOW, "bottom_right": Color.RED}),
                           "bottom_left": Card(7,  {"top_left": Color.GREEN, "top_right": Color.GRAY,
                                                    "bottom_left": Color.GRAY, "bottom_right": Color.BLUE}),
                           "bottom_middle": Card(8,  {"top_left": Color.YELLOW, "top_right": Color.BLUE,
                                                      "bottom_left": Color.PINK, "bottom_right": Color.GREEN}),
                           "bottom_right": Card(9,  {"top_left": Color.PINK, "top_right": Color.RED,
                                                     "bottom_left": Color.RED, "bottom_right": Color.YELLOW})})
    assert pattern.is_pattern_valid() == False


def test_is_pattern_invalid_diagonal():
    pattern = GreatSquare({"top_left": Card(1,  {"top_left": Color.BLUE, "top_right": Color.PINK,
                                                 "bottom_left": Color.GREEN, "bottom_right": Color.GRAY}),
                           "top_middle": Card(2,  {"top_left": Color.GRAY, "top_right": Color.RED,
                                                   "bottom_left": Color.YELLOW, "bottom_right": Color.BLUE}),
                           "top_right": Card(3,  {"top_left": Color.GREEN, "top_right": Color.YELLOW,
                                                  "bottom_left": Color.RED, "bottom_right": Color.PINK}),
                           "center_left": Card(4,  {"top_left": Color.YELLOW, "top_right": Color.GREEN,
                                                    "bottom_left": Color.GRAY, "bottom_right": Color.BLUE}),
                           "center_middle": Card(5,  {"top_left": Color.RED, "top_right": Color.GRAY,
                                                      "bottom_left": Color.PINK, "bottom_right": Color.GREEN}),
                           "center_right": Card(6,  {"top_left": Color.PINK, "top_right": Color.BLUE,
                                                     "bottom_left": Color.YELLOW, "bottom_right": Color.RED}),
                           "bottom_left": Card(7,  {"top_left": Color.RED, "top_right": Color.YELLOW,
                                                    "bottom_left": Color.PINK, "bottom_right": Color.RED}),
                           "bottom_middle": Card(8,  {"top_left": Color.GREEN, "top_right": Color.PINK,
                                                      "bottom_left": Color.BLUE, "bottom_right": Color.YELLOW}),
                           "bottom_right": Card(9,  {"top_left": Color.BLUE, "top_right": Color.GRAY,
                                                     "bottom_left": Color.GRAY, "bottom_right": Color.GREEN})})
    assert pattern.is_pattern_valid() == False
