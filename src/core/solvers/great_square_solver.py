from itertools import permutations
from concurrent.futures import ThreadPoolExecutor
from numpy import array_split


class GreatSquareSolver:

    CHUNKS = 4

    def __init__(self, pattern, cards, rectangle_solutions):
        self.pattern = pattern
        self.cards = cards
        self.rectangle_solutions = rectangle_solutions

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
        all_three_permutations = [list(p) for p in permutations(self.cards, 3)]
        for rectangle_solution in self.rectangle_solutions:
            for permutation in all_three_permutations:
                all_permutations.append([rectangle_solution[0], rectangle_solution[1], rectangle_solution[2],
                                         rectangle_solution[3], rectangle_solution[4], rectangle_solution[5],
                                         permutation[0], permutation[1], permutation[2]])
                all_permutations.append([permutation[0], permutation[1], permutation[2],
                                         rectangle_solution[2], rectangle_solution[1], rectangle_solution[0],
                                         rectangle_solution[5], rectangle_solution[4], rectangle_solution[3]])
        return all_permutations
