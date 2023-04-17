class Card:
    def __init__(self, id, colors):
        self.id = id
        self.top_left = colors["top_left"]
        self.top_right = colors["top_right"]
        self.bottom_left = colors["bottom_left"]
        self.bottom_right = colors["bottom_right"]

    def get_configurations(self):
        return [
            self,
            Card(
                self.id,
                {
                    "top_left": self.bottom_left,
                    "top_right": self.top_left,
                    "bottom_left": self.bottom_right,
                    "bottom_right": self.top_right,
                },
            ),
            Card(
                self.id,
                {
                    "top_left": self.bottom_right,
                    "top_right": self.bottom_left,
                    "bottom_left": self.top_right,
                    "bottom_right": self.top_left,
                },
            ),
            Card(
                self.id,
                {
                    "top_left": self.top_right,
                    "top_right": self.bottom_right,
                    "bottom_left": self.top_left,
                    "bottom_right": self.bottom_left,
                },
            ),
        ]
