from src.core.color import Color
from src.core.card import Card

DEFAULT_CARDS = [
    Card(1, Color.GRAY, Color.YELLOW, Color.GREEN, Color.BLUE),
    Card(2, Color.YELLOW, Color.PINK, Color.BLUE, Color.RED),
    Card(3, Color.PINK, Color.RED, Color.YELLOW, Color.RED),
    Card(4, Color.GRAY, Color.BLUE, Color.GRAY, Color.GREEN),
    Card(5, Color.YELLOW, Color.GRAY, Color.RED, Color.BLUE),
    Card(6, Color.GREEN, Color.PINK, Color.RED, Color.GRAY),
    Card(7, Color.BLUE, Color.GREEN, Color.PINK, Color.YELLOW),
    Card(8, Color.PINK, Color.RED, Color.GREEN, Color.YELLOW),
    Card(9, Color.GRAY, Color.GREEN, Color.BLUE, Color.PINK),
]

ALL_CONFIGURATIONS = [card.get_configurations() for card in DEFAULT_CARDS]

ALL_CARDS = [card for cards in ALL_CONFIGURATIONS for card in cards]
