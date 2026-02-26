from maze_valid import text_read, value_validation
from maze_gen import maze_gen, MAZE, Cord
from maze_solve import solution_dir, solve_maze
from maze_draw import draw_maze


class MazeGenerator:
    def __init__(self, WIDTH: int, HEIGHT: int, ENTRY: Cord, EXIT: Cord,
                 FILE: str, PERFECT: bool, ALGORITHM: str = "DFS") -> None:
        self.par = {
            "WIDTH": f"{WIDTH}",
            "HEIGHT": f"{HEIGHT}",
            "ENTRY": ",".join(str(x) for x in ENTRY),
            "EXIT": ",".join(str(x) for x in EXIT),
            "OUTPUT_FILE": FILE,
            "PERFECT": f"{PERFECT}",
            "ALGORITHM": ALGORITHM
        }
        msg = value_validation(self.par)
        if msg != "true":
            self.par = {}
            raise ValueError(msg)

    def generate()
        


def maze_output(par: dict, maze: MAZE, sol_dir: str) -> None:
    with open(par["OUTPUT_FILE"], "w") as file:
        for row in maze:
            for char in row:
                file.write(char)
            file.write("\n")
        file.write("\n")
        file.write(f"{par['ENTRY'][0]},{par['ENTRY'][1]}\n")
        file.write(f"{par['EXIT'][0]},{par['EXIT'][1]}\n")
        file.write(sol_dir)
        file.write("\n")


def intro_display() -> None:
    print("=== A-Maze-ing ===")
    print("1. Re-generate a new maze")
    print("2. Show/Hide path from entry to exit")
    print("3. Rotate maze colors")
    print("4. Quit")


def main() -> None:
    colors = ["37", "33", "36"]
    col_i = 0
    choice = 1
    disp_sol = False
    par = text_read()
    if not par:
        return
    maze = maze_gen(par)
    sol = solve_maze(maze, par['ENTRY'], par['EXIT'])
    sol_dir = solution_dir(sol, par['ENTRY'])
    maze_output(par, maze, sol_dir)
    draw_maze(maze, par['ENTRY'], par['EXIT'], colors[col_i], sol, False, True)
    while choice != 4:
        intro_display()
        try:
            choice = int(input("Choice? (1-4):"))
        except ValueError:
            print("Please enter only a digit between (1-4)")
            choice = 0
            continue
        if choice == 1:
            maze = maze_gen(par)
            sol = solve_maze(maze, par['ENTRY'], par['EXIT'])
            sol_dir = solution_dir(sol, par['ENTRY'])
            maze_output(par, maze, sol_dir)
            draw_maze(maze, par['ENTRY'], par['EXIT'],
                      colors[col_i], sol, False, True)
            disp_sol = False
        elif choice == 2:
            disp_sol = not disp_sol
            draw_maze(maze, par['ENTRY'], par['EXIT'],
                      colors[col_i], sol, disp_sol, False)
        elif choice == 3:
            col_i += 1
            if col_i > len(colors) - 1:
                col_i = 0
            draw_maze(maze, par['ENTRY'], par['EXIT'],
                      colors[col_i], sol, disp_sol, False)
        elif choice != 4:
            print("please enter a digit between (1-4)")


if __name__ == "__main__":
    main()
