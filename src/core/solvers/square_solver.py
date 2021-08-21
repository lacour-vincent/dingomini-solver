from itertools import permutations
from concurrent.futures import ThreadPoolExecutor
from numpy import array_split


class SquareSolver:

    CHUNKS = 4

    def __init__(self, pattern, cards):
        self.pattern = pattern
        self.cards = cards

    def solve(self):
        solutions = []
        all_permutations_chunks = array_split(self.__get_all_permutations(), self.CHUNKS)
        with ThreadPoolExecutor(max_workers=4) as executor:
            for all_permutations in all_permutations_chunks:
                permutations = executor.map(self.__is_permutation_valid, all_permutations)
                for solution in permutations:
                    if (solution is not None):
                        solutions.append(solution)
        return solutions

    def __is_permutation_valid(self, permutation):
        cards = {"top_left": permutation[0], "top_right": permutation[1],
                 "bottom_right": permutation[2], "bottom_left": permutation[3]}
        pattern = self.pattern(cards)
        if (pattern.is_pattern_valid()):
            return cards
        return None

    def __get_all_permutations(self):
        all_permutations = []
        for perm in permutations(self.cards, 4):
            all_permutations.append(list(perm))
        return all_permutations
