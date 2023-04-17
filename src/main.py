from core.patterns.small_rectangle import SmallRectangle

# from core.patterns.square import Square
# from core.patterns.rectangle import Rectangle
# from core.patterns.great_square import GreatSquare

from core.solvers.small_rectangle_solver import SmallRectangleSolver

# from core.solvers.great_square_solver import GreatSquareSolver
# from core.solvers.square_solver import SquareSolver
# from core.solvers.rectangle_solver import RectangleSolver


from core.game import ALL_CARDS
from draw.drawer import Drawer


def main():
    drawer = Drawer()

    small_rectangle_solver = SmallRectangleSolver(SmallRectangle, ALL_CARDS)
    print("solver small rectangle ...")
    small_rectangle_solutions = small_rectangle_solver.solve()
    print(f"small rectangle solutions : {len(small_rectangle_solutions)}")
    drawer.save_small_rectangle_solutions(SmallRectangle, small_rectangle_solutions)

    # square_solver = SquareSolver(Square, ALL_CARDS, small_rectangle_solutions)
    # print("solve square ...")
    # square_solutions = square_solver.solve()
    # print(f"square solutions : {len(square_solutions)}")
    # drawer.save_square_solutions(Square, square_solutions)

    # rectangle_solver = RectangleSolver(Rectangle, ALL_CARDS, square_solutions)
    # print("solve rectangle ...")
    # rectangle_solutions = rectangle_solver.solve()
    # print(f"rectangle solutions : {len(rectangle_solutions)}")
    # drawer.save_rectangle_solutions(Rectangle, rectangle_solutions)

    # great_square_solver = GreatSquareSolver(
    #     GreatSquare, ALL_CARDS, rectangle_solutions
    # )
    # print("solve great square ...")
    # great_square_solutions = great_square_solver.solve()
    # print(f"great square solutions : {len(great_square_solutions)}")
    # drawer.save_great_square_solutions(GreatSquare, great_square_solutions)


if __name__ == "__main__":
    main()
