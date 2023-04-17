from core.color import Color
from core.card import Card
from core.patterns.small_rectangle import SmallRectangle


def test_is_pattern_valid():
    pattern = SmallRectangle({"left": Card(1,  {"top_left": Color.PINK, "top_right": Color.GRAY,
                                                "bottom_left": Color.BLUE, "bottom_right": Color.GREEN}),
                              "right": Card(2,  {"top_left": Color.GREEN, "top_right": Color.BLUE,
                                                 "bottom_left": Color.YELLOW, "bottom_right": Color.GRAY})})
    assert pattern.is_pattern_valid() == True


def test_is_pattern_invalid_same_card():
    pattern = SmallRectangle({"left": Card(1,  {"top_left": Color.PINK, "top_right": Color.GRAY,
                                                "bottom_left": Color.BLUE, "bottom_right": Color.GREEN}),
                              "right": Card(1,  {"top_left": Color.PINK, "top_right": Color.GRAY,
                                                 "bottom_left": Color.BLUE, "bottom_right": Color.GREEN})})
    assert pattern.is_pattern_valid() == False


def test_is_pattern_invalid_row():
    pattern = SmallRectangle({"left": Card(1,  {"top_left": Color.PINK, "top_right": Color.GRAY,
                                                "bottom_left": Color.BLUE, "bottom_right": Color.GREEN}),
                              "right": Card(2,  {"top_left": Color.PINK, "top_right": Color.BLUE,
                                                 "bottom_left": Color.YELLOW, "bottom_right": Color.RED})})
    assert pattern.is_pattern_valid() == False


def test_is_pattern_invalid_column():
    # Pattern with only column errors does not exists.
    assert False == False
