from itertools import permutations
from concurrent.futures import ThreadPoolExecutor
from numpy import array_split


class GreatSquareSolver:

    CHUNKS = 4

    def __init__(self, pattern, cards, square_solutions):
        self.pattern = pattern
        self.cards = cards
        self.square_solutions = square_solutions

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
        pattern = self.pattern(*permutation)
        if (pattern.is_pattern_valid()):
            return permutation
        return None

    def __get_all_permutations(self):
        all_permutations = []
        for square_solution in self.square_solutions:
            permutations_from_solution = self.__get_permutations_from_solution(square_solution)
            for permutation in permutations_from_solution:
                all_permutations.append([square_solution[0], square_solution[1], permutation[0],
                                         permutation[1], square_solution[2], square_solution[3],
                                         permutation[2], permutation[3], permutation[4]])

                all_permutations.append([permutation[0], square_solution[0], square_solution[1],
                                         square_solution[2], square_solution[3], permutation[1],
                                         permutation[2], permutation[3], permutation[4]])

                all_permutations.append([permutation[0], permutation[1], permutation[2],
                                         permutation[3], square_solution[1], square_solution[0],
                                         square_solution[3], square_solution[2], permutation[4]])

                all_permutations.append([permutation[0], permutation[1], permutation[2],
                                         square_solution[1], square_solution[0], permutation[3],
                                         permutation[4], square_solution[3], square_solution[2]])

        return all_permutations

    def __get_permutations_from_solution(self, square_solution):
        permutations_from_solutions = []
        solution_ids = [card.id for card in square_solution]
        remaining_cards = [card for card in self.cards if card.id not in solution_ids]
        for perm in permutations(remaining_cards, 5):
            permutations_from_solutions.append(list(perm))
        return permutations_from_solutions
