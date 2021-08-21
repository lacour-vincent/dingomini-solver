from src.core.color import Color
from src.core.card import Card

DEFAULT_CARDS = [
    Card(1, {"top_left": Color.PINK, "top_right": Color.GRAY,
             "bottom_left": Color.BLUE, "bottom_right": Color.GREEN}),

    Card(2, {"top_left": Color.RED, "top_right": Color.PINK,
             "bottom_left": Color.YELLOW, "bottom_right": Color.RED}),

    Card(3, {"top_left": Color.GRAY, "top_right": Color.GREEN,
             "bottom_left": Color.BLUE, "bottom_right": Color.GRAY}),

    Card(4, {"top_left": Color.BLUE, "top_right": Color.YELLOW,
             "bottom_left": Color.RED, "bottom_right": Color.GRAY}),

    Card(5, {"top_left": Color.PINK, "top_right": Color.RED,
             "bottom_left": Color.YELLOW, "bottom_right": Color.GREEN}),

    Card(6, {"top_left": Color.PINK, "top_right": Color.YELLOW,
             "bottom_left": Color.GREEN, "bottom_right": Color.BLUE}),

    Card(7, {"top_left": Color.GREEN, "top_right": Color.PINK,
             "bottom_left": Color.GRAY, "bottom_right": Color.RED}),

    Card(8, {"top_left": Color.RED, "top_right": Color.YELLOW,
             "bottom_left": Color.BLUE, "bottom_right": Color.PINK}),

    Card(9, {"top_left": Color.GRAY, "top_right": Color.YELLOW,
             "bottom_left": Color.BLUE, "bottom_right": Color.GREEN}),
]

ALL_CONFIGURATIONS = [card.get_configurations() for card in DEFAULT_CARDS]

ALL_CARDS = [card for cards in ALL_CONFIGURATIONS for card in cards]
