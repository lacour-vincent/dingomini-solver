from itertools import permutations
from concurrent.futures import ThreadPoolExecutor
from numpy import array_split
from operator import itemgetter


class GreatSquareSolver:
    CHUNKS = 4

    def __init__(self, pattern, cards, rectangle_solutions):
        self.pattern = pattern
        self.cards = cards
        self.rectangle_solutions = rectangle_solutions

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
            "top_middle": permutation[1],
            "top_right": permutation[2],
            "center_left": permutation[3],
            "center_middle": permutation[4],
            "center_right": permutation[5],
            "bottom_left": permutation[6],
            "bottom_middle": permutation[7],
            "bottom_right": permutation[8],
        }
        pattern = self.pattern(cards)
        if pattern.is_pattern_valid():
            return cards, pattern.hash
        return None

    def __get_all_permutations(self):
        all_permutations = []
        for rectangle_solution in self.rectangle_solutions:
            permutations_from_solution = self.__get_permutations_from_solution(rectangle_solution)
            tl, tm, tr, bl, bm, br = itemgetter(
                "top_left",
                "top_middle",
                "top_right",
                "bottom_left",
                "bottom_middle",
                "bottom_right",
            )(rectangle_solution)
            for permutation in permutations_from_solution:
                all_permutations.append(
                    [
                        tl,
                        tm,
                        tr,
                        bl,
                        bm,
                        br,
                        permutation[0],
                        permutation[1],
                        permutation[2],
                    ]
                )
        return all_permutations

    def __get_permutations_from_solution(self, rectangle_solution):
        permutations_from_solutions = []
        solution_ids = [card.id for card in rectangle_solution.values()]
        remaining_cards = [card for card in self.cards if card.id not in solution_ids]
        for perm in permutations(remaining_cards, 3):
            permutations_from_solutions.append(list(perm))
        return permutations_from_solutions
