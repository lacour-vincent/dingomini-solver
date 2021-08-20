from itertools import permutations
from concurrent.futures import ThreadPoolExecutor
from numpy import array_split


class RectangleSolver:

    CHUNKS = 4

    def __init__(self, pattern, cards, square_solutions):
        self.pattern = pattern
        self.cards = cards
        self.square_solutions = square_solutions

    def is_permutation_valid(self, permutation):
        pattern = self.pattern(*permutation)
        if (pattern.is_pattern_valid()):
            return permutation
        return None

    def solve(self):
        solutions = []
        all_permutations_chunks = array_split(self.get_all_permutations(), self.CHUNKS)
        with ThreadPoolExecutor(max_workers=4) as executor:
            for all_permutations in all_permutations_chunks:
                permutations = executor.map(self.is_permutation_valid, all_permutations)
                for solution in permutations:
                    if (solution is not None):
                        solutions.append(solution)
        return solutions

    def get_all_permutations(self):
        all_permutations = []
        all_two_permutations = [list(p) for p in permutations(self.cards, 2)]
        for square_solution in self.square_solutions:
            for permutation in all_two_permutations:
                all_permutations.append([square_solution[0], square_solution[1], permutation[0],
                                         permutation[1], square_solution[2], square_solution[3]])
                all_permutations.append([permutation[0], square_solution[0], square_solution[1],
                                         square_solution[2], square_solution[3], permutation[1]])
        return all_permutations
