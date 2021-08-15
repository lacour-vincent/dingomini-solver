from src.core.color import Color
from src.core.card import Card
from src.core.patterns.square import Square


def test_is_pattern_valid():
    pattern = Square(Card(Color.GREEN, Color.BLUE, Color.PINK, Color.GRAY),
                     Card(Color.GRAY, Color.YELLOW, Color.GREEN, Color.BLUE),
                     Card(Color.YELLOW, Color.PINK, Color.BLUE, Color.RED),
                     Card(Color.RED, Color.GREEN, Color.YELLOW, Color.PINK))
    assert pattern.is_pattern_valid() == True


def test_is_pattern_invalid_row():
    pattern = Square(Card(Color.YELLOW, Color.RED, Color.PINK, Color.RED),
                     Card(Color.YELLOW, Color.PINK, Color.BLUE, Color.RED),
                     Card(Color.GRAY, Color.YELLOW, Color.GREEN, Color.BLUE),
                     Card(Color.GRAY, Color.GREEN, Color.GRAY, Color.BLUE))
    assert pattern.is_pattern_valid() == False


def test_is_pattern_invalid_column():
    pattern = Square(Card(Color.BLUE, Color.GRAY, Color.GREEN, Color.GRAY),
                     Card(Color.RED, Color.YELLOW, Color.RED, Color.PINK),
                     Card(Color.RED, Color.YELLOW, Color.PINK, Color.BLUE),
                     Card(Color.BLUE, Color.GRAY, Color.YELLOW, Color.GREEN))
    assert pattern.is_pattern_valid() == False


def test_is_pattern_invalid_diagonal():
    pattern = Square(Card(Color.YELLOW, Color.RED, Color.PINK, Color.RED),
                     Card(Color.GRAY, Color.BLUE, Color.GRAY, Color.GREEN),
                     Card(Color.BLUE, Color.RED, Color.YELLOW, Color.PINK),
                     Card(Color.PINK, Color.YELLOW, Color.BLUE, Color.GREEN))
    assert pattern.is_pattern_valid() == False
