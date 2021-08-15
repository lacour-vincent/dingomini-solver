from itertools import combinations


class Solver:
    def __init__(self, pattern, cards):
        self.pattern = pattern
        self.cards = cards

    def solve(self):
        all_combinations = list([c for c in combinations(self.cards, self.pattern.TOTAL_CARDS)])
        solutions = []
        for combination in all_combinations:
            pattern = self.pattern(*combination)
            if (pattern.is_pattern_valid()):
                solutions.append([*combination])
        return solutions
