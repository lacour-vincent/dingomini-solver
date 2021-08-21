from src.core.color import Color
from src.core.card import Card
from src.core.patterns.square import Square


def test_is_pattern_valid():
    pattern = Square({"top_left": Card(1,  {"top_left": Color.GRAY, "top_right": Color.YELLOW,
                                            "bottom_left": Color.BLUE, "bottom_right": Color.GREEN}),
                      "top_right": Card(2,  {"top_left": Color.RED, "top_right": Color.BLUE,
                                             "bottom_left": Color.GRAY, "bottom_right": Color.YELLOW}),
                      "bottom_left": Card(3,  {"top_left": Color.YELLOW, "top_right": Color.PINK,
                                               "bottom_left": Color.RED, "bottom_right": Color.BLUE}),
                      "bottom_right": Card(4,  {"top_left": Color.BLUE, "top_right": Color.GREEN,
                                                "bottom_left": Color.YELLOW, "bottom_right": Color.PINK})})
    assert pattern.is_pattern_valid() == True


def test_is_pattern_invalid_same_card():
    pattern = Square({"top_left": Card(1,  {"top_left": Color.GRAY, "top_right": Color.YELLOW,
                                            "bottom_left": Color.BLUE, "bottom_right": Color.GREEN}),
                      "top_right": Card(1,  {"top_left": Color.RED, "top_right": Color.BLUE,
                                             "bottom_left": Color.GRAY, "bottom_right": Color.YELLOW}),
                      "bottom_left": Card(3,  {"top_left": Color.YELLOW, "top_right": Color.PINK,
                                               "bottom_left": Color.RED, "bottom_right": Color.BLUE}),
                      "bottom_right": Card(4,  {"top_left": Color.BLUE, "top_right": Color.GREEN,
                                                "bottom_left": Color.YELLOW, "bottom_right": Color.PINK})})
    assert pattern.is_pattern_valid() == False


def test_is_pattern_invalid_row():
    pattern = Square({"top_left": Card(1,  {"top_left": Color.PINK, "top_right": Color.GRAY,
                                            "bottom_left": Color.BLUE, "bottom_right": Color.GREEN}),
                      "top_right": Card(2,  {"top_left": Color.GRAY, "top_right": Color.GREEN,
                                             "bottom_left": Color.BLUE, "bottom_right": Color.GRAY}),
                      "bottom_left": Card(3,  {"top_left": Color.RED, "top_right": Color.PINK,
                                               "bottom_left": Color.YELLOW, "bottom_right": Color.RED}),
                      "bottom_right": Card(4,  {"top_left": Color.YELLOW, "top_right": Color.PINK,
                                                "bottom_left": Color.GREEN, "bottom_right": Color.RED})})
    assert pattern.is_pattern_valid() == False


def test_is_pattern_invalid_column():
    pattern = Square({"top_left": Card(1,  {"top_left": Color.PINK, "top_right": Color.GRAY,
                                            "bottom_left": Color.BLUE, "bottom_right": Color.GREEN}),
                      "top_right": Card(2,  {"top_left": Color.RED, "top_right": Color.YELLOW,
                                             "bottom_left": Color.PINK, "bottom_right": Color.RED}),
                      "bottom_left": Card(3,  {"top_left": Color.GRAY, "top_right": Color.GREEN,
                                               "bottom_left": Color.BLUE, "bottom_right": Color.GRAY}),
                      "bottom_right": Card(4,  {"top_left": Color.YELLOW, "top_right": Color.PINK,
                                                "bottom_left": Color.GREEN, "bottom_right": Color.RED})})
    assert pattern.is_pattern_valid() == False


def test_is_pattern_invalid_diagonal():
    pattern = Square({"top_left": Card(1,  {"top_left": Color.PINK, "top_right": Color.GRAY,
                                            "bottom_left": Color.BLUE, "bottom_right": Color.GREEN}),
                      "top_right": Card(2,  {"top_left": Color.YELLOW, "top_right": Color.RED,
                                             "bottom_left": Color.RED, "bottom_right": Color.PINK}),
                      "bottom_left": Card(3,  {"top_left": Color.YELLOW, "top_right": Color.PINK,
                                               "bottom_left": Color.GREEN, "bottom_right": Color.RED}),
                      "bottom_right": Card(4,  {"top_left": Color.GRAY, "top_right": Color.GREEN,
                                                "bottom_left": Color.BLUE, "bottom_right": Color.GRAY})})
    assert pattern.is_pattern_valid() == False
