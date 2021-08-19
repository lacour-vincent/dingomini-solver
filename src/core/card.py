class Card:
    def __init__(self, id, top_left, top_right, bottom_right, bottom_left):
        self.id = id
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_right = bottom_right
        self.bottom_left = bottom_left

    def get_configurations(self) -> list:
        return [self,
                Card(self.id, self.bottom_left, self.top_left, self.top_right, self.bottom_right),
                Card(self.id, self.bottom_right, self.bottom_left, self.top_left, self.top_right),
                Card(self.id, self.top_right, self.bottom_right, self.bottom_left, self.top_left),
                ]
