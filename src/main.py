from core.solver import Solver
from core.patterns.square import Square
from core.game import ALL_CARDS
from draw.drawer import Drawer

import time


def main():
    t0 = time.time()
    solver = Solver(Square, ALL_CARDS)
    drawer = Drawer(Square)
    solutions = solver.solve()
    t1 = time.time()
    print(F"Execution time : {t1 - t0 }")
    # drawer.draw_and_save_solutions(solutions)


if __name__ == "__main__":
    main()
