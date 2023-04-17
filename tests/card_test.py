from core.color import Color
from core.card import Card


def assert_card_equals(card_left, card_right):
    assert card_left.id == card_right.id
    assert card_left.top_left == card_right.top_left
    assert card_left.top_right == card_right.top_right
    assert card_left.bottom_right == card_right.bottom_right
    assert card_left.bottom_left == card_right.bottom_left


def test_card_return_all_configurations():
    configurations = Card(1,  {"top_left": Color.PINK, "top_right": Color.GRAY,
                               "bottom_left": Color.BLUE, "bottom_right": Color.GREEN}).get_configurations()
    assert_card_equals(configurations[0], Card(1, {"top_left": Color.PINK, "top_right": Color.GRAY,
                                                   "bottom_left": Color.BLUE, "bottom_right": Color.GREEN}))
    assert_card_equals(configurations[1], Card(1, {"top_left": Color.BLUE, "top_right": Color.PINK,
                                                   "bottom_left": Color.GREEN, "bottom_right": Color.GRAY}))
    assert_card_equals(configurations[2], Card(1, {"top_left": Color.GREEN, "top_right": Color.BLUE,
                                                   "bottom_left": Color.GRAY, "bottom_right": Color.PINK}))
    assert_card_equals(configurations[3], Card(1, {"top_left": Color.GRAY, "top_right": Color.GREEN,
                                                   "bottom_left": Color.PINK, "bottom_right": Color.BLUE}))
