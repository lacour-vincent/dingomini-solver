from core.solver import Solver
from core.patterns.square import Square
from core.patterns.rectangle import Rectangle
from core.game import ALL_CARDS
from draw.drawer import Drawer


def main():
    solver = Solver(Rectangle, ALL_CARDS)
    drawer = Drawer(Square)
    solutions = solver.solve()
    # drawer.draw_and_save_solutions(solutions)


if __name__ == "__main__":
    main()
