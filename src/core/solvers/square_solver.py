from itertools import permutations
from concurrent.futures import ThreadPoolExecutor
from numpy import array_split
from operator import itemgetter


class SquareSolver:
    CHUNKS = 4

    def __init__(self, pattern, cards, small_rectangle_solutions):
        self.pattern = pattern
        self.cards = cards
        self.small_rectangle_solutions = small_rectangle_solutions

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
        cards = {
            "top_left": permutation[0],
            "top_right": permutation[1],
            "bottom_right": permutation[2],
            "bottom_left": permutation[3],
        }
        pattern = self.pattern(cards)
        if pattern.is_pattern_valid():
            return cards, pattern.hash
        return None

    def __get_all_permutations(self):
        all_permutations = []
        for small_rectangle_solution in self.small_rectangle_solutions:
            permutations_from_solution = self.__get_permutations_from_solution(small_rectangle_solution)
            l, r = itemgetter("left", "right")(small_rectangle_solution)
            for permutation in permutations_from_solution:
                all_permutations.append([l, r, permutation[0], permutation[1]])

        return all_permutations

    def __get_permutations_from_solution(self, small_rectangle_solution):
        permutations_from_solutions = []
        solution_ids = [card.id for card in small_rectangle_solution.values()]
        remaining_cards = [card for card in self.cards if card.id not in solution_ids]
        for perm in permutations(remaining_cards, 2):
            permutations_from_solutions.append(list(perm))
        return permutations_from_solutions
