from itertools import permutations
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


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
        all_permutations = self.get_all_permutations()
        print(len(all_permutations))
        results = []
        with ThreadPoolExecutor(max_workers=None) as executor:
            futures = {executor.submit(self.is_permutation_valid, perm): perm for perm in all_permutations}
            for future in as_completed(futures):
                results.append(future.result())
        return [r for r in results if r is not None]

    def get_all_permutations(self):
        all_permutations = []
        N = self.pattern.TOTAL_CARDS
        for i, card in enumerate(self.cards):
            if (i < len(self.cards) - N):
                k = i // N
                j = (k + 1) * N
                omega = [card, *self.cards[j:]]
                all_permutations.append([list(p) for p in permutations(omega, N)])
        return [card for cards in all_permutations for card in cards]
