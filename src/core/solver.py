from itertools import permutations
from concurrent.futures import ThreadPoolExecutor
from numpy import array_split


class Solver:

    def __init__(self, pattern, cards):
        self.pattern = pattern
        self.cards = cards

    def is_permutation_valid(self, permutation):
        pattern = self.pattern(*permutation)
        if (pattern.is_pattern_valid()):
            return permutation
        return None

    def solve(self):
        solutions = []
        chunks = 4
        all_permutations_chunks = array_split(self.get_all_permutations(), chunks)
        with ThreadPoolExecutor(max_workers=4) as executor:
            for all_permutations in all_permutations_chunks:
                permutations = executor.map(self.is_permutation_valid, all_permutations)
                for solution in permutations:
                    if (solution is not None):
                        solutions.append(solution)
        return solutions

    def get_all_permutations(self):
        all_permutations = []
        N = self.pattern.TOTAL_CARDS
        print("get all permutations")
        for permutation in permutations(self.cards, N):
            all_permutations.append(list(permutation))
        print(len(all_permutations))
        return all_permutations
