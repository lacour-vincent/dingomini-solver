from src.core.color import Color
from src.core.card import Card


def assert_card_equals(card_left, card_right):
    assert card_left.id == card_right.id
    assert card_left.top_left == card_right.top_left
    assert card_left.top_right == card_right.top_right
    assert card_left.bottom_right == card_right.bottom_right
    assert card_left.bottom_left == card_right.bottom_left


def test_card_return_all_configurations():
    configurations = Card(1, Color.PINK, Color.GRAY, Color.GREEN, Color.BLUE).get_configurations()
    assert_card_equals(configurations[0], Card(1, Color.PINK, Color.GRAY, Color.GREEN, Color.BLUE))
    assert_card_equals(configurations[1], Card(1, Color.BLUE, Color.PINK, Color.GRAY, Color.GREEN))
    assert_card_equals(configurations[2], Card(1, Color.GREEN, Color.BLUE, Color.PINK, Color.GRAY))
    assert_card_equals(configurations[3], Card(1, Color.GRAY, Color.GREEN, Color.BLUE, Color.PINK))
