from itertools import permutations
from concurrent.futures import ThreadPoolExecutor
from numpy import array_split


class SmallRectangleSolver:
    CHUNKS = 4

    def __init__(self, pattern, cards):
        self.pattern = pattern
        self.cards = cards

    def solve(self):
        solutions = []
        solution_hashes = []
        all_permutations_chunks = array_split(self.__get_all_permutations(), self.CHUNKS)
        with ThreadPoolExecutor(max_workers=4) as executor:
            for all_permutations in all_permutations_chunks:
                permutations = executor.map(self.__is_permutation_valid, all_permutations)
                for solution in permutations:
                    if solution is not None:
                        pattern, hash = solution
                        if hash not in solution_hashes:
                            solutions.append(pattern)
                            solution_hashes.append(hash)
        return solutions

    def __is_permutation_valid(self, permutation):
        cards = {"left": permutation[0], "right": permutation[1]}
        pattern = self.pattern(cards)
        if pattern.is_pattern_valid():
            return cards, pattern.hash
        return None

    def __get_all_permutations(self):
        all_permutations = []
        for perm in permutations(self.cards, 2):
            all_permutations.append(list(perm))
        return all_permutations
