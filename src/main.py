from core.solvers.great_square_solver import GreatSquareSolver
from core.solvers.square_solver import SquareSolver
from core.solvers.rectangle_solver import RectangleSolver

from core.patterns.square import Square
from core.patterns.rectangle import Rectangle
from core.patterns.great_square import GreatSquare

from core.game import ALL_CARDS
from draw.drawer import Drawer


def main():
    drawer = Drawer()
    square_solver = SquareSolver(Square, ALL_CARDS)
    square_solutions = square_solver.solve()
    rectangle_solver = RectangleSolver(Rectangle, ALL_CARDS, square_solutions)
    rectangle_solutions = rectangle_solver.solve()
    great_square_solver = GreatSquareSolver(GreatSquare, ALL_CARDS, rectangle_solutions)
    great_square_solutions = great_square_solver.solve()

    drawer.save_square_solutions(Square, square_solutions)
    drawer.save_rectangle_solutions(Rectangle, rectangle_solutions)
    drawer.save_great_square_solutions(GreatSquare, great_square_solutions)


if __name__ == "__main__":
    main()
