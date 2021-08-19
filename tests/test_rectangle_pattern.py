from src.core.color import Color
from src.core.card import Card
from src.core.patterns.rectangle import Rectangle


# def test_is_pattern_valid():
#     pattern = Rectangle(Card(1, Color.GREEN, Color.BLUE, Color.PINK, Color.GRAY),
#                         Card(2, Color.GRAY, Color.YELLOW, Color.GREEN, Color.BLUE),
#                         Card(3, Color.YELLOW, Color.PINK, Color.BLUE, Color.RED),
#                         Card(4, Color.RED, Color.GREEN, Color.YELLOW, Color.PINK))
#     assert pattern.is_pattern_valid() == True


def test_is_pattern_invalid_same_card():
    pattern = Rectangle(Card(1, Color.YELLOW, Color.RED, Color.PINK, Color.RED),
                        Card(1, Color.YELLOW, Color.PINK, Color.BLUE, Color.RED),
                        Card(3, Color.GRAY, Color.YELLOW, Color.GREEN, Color.BLUE),
                        Card(4, Color.GRAY, Color.GREEN, Color.GRAY, Color.BLUE),
                        Card(5, Color.GRAY, Color.GREEN, Color.GRAY, Color.BLUE),
                        Card(6, Color.GRAY, Color.GREEN, Color.GRAY, Color.BLUE))
    assert pattern.is_pattern_valid() == False


def test_is_pattern_invalid_row():
    pattern = Rectangle(Card(1, Color.YELLOW, Color.RED, Color.PINK, Color.RED),
                        Card(2, Color.YELLOW, Color.PINK, Color.BLUE, Color.RED),
                        Card(3, Color.GRAY, Color.YELLOW, Color.GREEN, Color.BLUE),
                        Card(4, Color.GRAY, Color.GREEN, Color.GRAY, Color.BLUE),
                        Card(5, Color.GRAY, Color.GREEN, Color.GRAY, Color.BLUE),
                        Card(6, Color.GRAY, Color.GREEN, Color.GRAY, Color.BLUE))
    assert pattern.is_pattern_valid() == False


def test_is_pattern_invalid_column():
    pattern = Rectangle(Card(1, Color.BLUE, Color.GRAY, Color.GREEN, Color.GRAY),
                        Card(2, Color.RED, Color.YELLOW, Color.RED, Color.PINK),
                        Card(3, Color.RED, Color.YELLOW, Color.PINK, Color.BLUE),
                        Card(4, Color.BLUE, Color.GRAY, Color.YELLOW, Color.GREEN),
                        Card(5, Color.GRAY, Color.GREEN, Color.GRAY, Color.BLUE),
                        Card(6, Color.GRAY, Color.GREEN, Color.GRAY, Color.BLUE))
    assert pattern.is_pattern_valid() == False


def test_is_pattern_invalid_diagonal():
    pattern = Rectangle(Card(1, Color.YELLOW, Color.RED, Color.PINK, Color.RED),
                        Card(2, Color.GRAY, Color.BLUE, Color.GRAY, Color.GREEN),
                        Card(3, Color.BLUE, Color.RED, Color.YELLOW, Color.PINK),
                        Card(4, Color.PINK, Color.YELLOW, Color.BLUE, Color.GREEN),
                        Card(5, Color.GRAY, Color.GREEN, Color.GRAY, Color.BLUE),
                        Card(6, Color.GRAY, Color.GREEN, Color.GRAY, Color.BLUE))
    assert pattern.is_pattern_valid() == False