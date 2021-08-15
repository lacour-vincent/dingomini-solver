from src.core.color import Color
from src.core.card import Card

DEFAULT_CARDS = [
    Card(Color.GRAY, Color.YELLOW, Color.GREEN, Color.BLUE),
    Card(Color.YELLOW, Color.PINK, Color.BLUE, Color.RED),
    Card(Color.PINK, Color.RED, Color.YELLOW, Color.RED),
    Card(Color.GRAY, Color.BLUE, Color.GRAY, Color.GREEN),
    Card(Color.YELLOW, Color.GRAY, Color.RED, Color.BLUE),
    Card(Color.GREEN, Color.PINK, Color.RED, Color.GRAY),
    Card(Color.BLUE, Color.GREEN, Color.PINK, Color.YELLOW),
    Card(Color.PINK, Color.RED, Color.GREEN, Color.YELLOW),
    Card(Color.GRAY, Color.GREEN, Color.BLUE, Color.PINK),
]

ALL_CONFIGURATIONS = [card.get_configurations() for card in DEFAULT_CARDS]

ALL_CARDS = [card for cards in ALL_CONFIGURATIONS for card in cards]
