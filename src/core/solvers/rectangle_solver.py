from itertools import permutations
from concurrent.futures import ThreadPoolExecutor
from numpy import array_split
from operator import itemgetter


class RectangleSolver:

    CHUNKS = 4

    def __init__(self, pattern, cards, square_solutions):
        self.pattern = pattern
        self.cards = cards
        self.square_solutions = square_solutions

    def solve(self):
        solutions = []
        perms = self.__get_all_permutations()
        print(len(perms))
        all_permutations_chunks = array_split(perms, self.CHUNKS)
        with ThreadPoolExecutor(max_workers=4) as executor:
            for all_permutations in all_permutations_chunks:
                permutations = executor.map(self.__is_permutation_valid, all_permutations)
                for solution in permutations:
                    if (solution is not None):
                        solutions.append(solution)
        return solutions

    def __is_permutation_valid(self, permutation):
        cards = {"top_left": permutation[0], "top_middle": permutation[1],  "top_right": permutation[2],
                 "bottom_left": permutation[3], "bottom_middle": permutation[4], "bottom_right": permutation[5]}
        pattern = self.pattern(cards)
        if (pattern.is_pattern_valid()):
            return cards
        return None

    def __get_all_permutations(self):
        all_permutations = []
        for square_solution in self.square_solutions:
            permutations_from_solution = self.__get_permutations_from_solution(square_solution)
            tl, tr, bl, br = itemgetter('top_left', 'top_right', "bottom_left", "bottom_right")(square_solution)
            for permutation in permutations_from_solution:
                all_permutations.append([tl, tr, permutation[0], bl, br, permutation[1]])
                all_permutations.append([permutation[0], tl, tr, permutation[1], bl, br])
        return all_permutations

    def __get_permutations_from_solution(self, square_solution):
        permutations_from_solutions = []
        solution_ids = [card.id for card in square_solution.values()]
        remaining_cards = [card for card in self.cards if card.id not in solution_ids]
        for perm in permutations(remaining_cards, 2):
            permutations_from_solutions.append(list(perm))
        return permutations_from_solutions
