from maze_valid import text_read
from mazegen import MazeGenerator
from maze_utils import intro_display


def main() -> None:
    colors = ["37", "33", "36"]
    col_i = 0
    choice = 1
    show_sol = False
    show_anim = True
    par = text_read()
    if not par:
        return
    maze = MazeGenerator(par["WIDTH"], par["HEIGHT"], par["ENTRY"],
                         par["EXIT"], par["OUTPUT_FILE"], par["PERFECT"],
                         par["ALGORITHM"], par["SEED"])
    maze.generate()
    maze.display(colors[col_i], show_sol, show_anim)
    while choice != 4:
        intro_display()
        try:
            choice = int(input("Choice? (1-4):"))
        except ValueError:
            print("Please enter only a digit between (1-4)")
            choice = 0
            continue
        if choice == 1:
            show_sol = False
            maze.generate()
            maze.display(colors[col_i], show_sol, show_anim)
        elif choice == 2:
            show_sol = not show_sol
            maze.display(colors[col_i], show_sol, not show_anim)
        elif choice == 3:
            col_i += 1
            if col_i > len(colors) - 1:
                col_i = 0
            maze.display(colors[col_i], show_sol, not show_anim)
        elif choice != 4:
            print("please enter a digit between (1-4)")


if __name__ == "__main__":
    main()
