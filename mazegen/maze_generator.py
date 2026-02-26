from maze_valid import value_validation
from maze_utils import maze_output
from maze_gen import maze_gen, Cord, MAZE
from maze_solve import solution_dir, solve_maze
from maze_draw import draw_maze


class MazeGenerator:
    def __init__(self, WIDTH: int, HEIGHT: int, ENTRY: Cord, EXIT: Cord,
                 FILE: str, PERFECT: bool, ALGORITHM: str = "DFS",
                 SEED: int = None) -> None:
        self.__par = {
            "WIDTH": f"{WIDTH}",
            "HEIGHT": f"{HEIGHT}",
            "ENTRY": ",".join(str(x) for x in ENTRY),
            "EXIT": ",".join(str(x) for x in EXIT),
            "OUTPUT_FILE": FILE,
            "PERFECT": f"{PERFECT}",
            "ALGORITHM": ALGORITHM,
            "SEED": SEED
        }
        msg = value_validation(self.__par)
        if msg != "true":
            self.__par = {}
            raise ValueError(msg)
        self.__maze = []
        self.__sol = []

    def generate(self) -> None:
        self.__maze = maze_gen(self.__par)
        self.__sol = solve_maze(self.__maze, self.__par['ENTRY'],
                                self.__par['EXIT'])
        sol_dir = solution_dir(self.__sol, self.__par['ENTRY'])
        maze_output(self.__par, self.__maze, sol_dir)

    def display(self, color: str, show_sol: bool, show_anim: bool) -> None:
        draw_maze(self.__maze, self.__par['ENTRY'], self.__par['EXIT'], color,
                  self.__sol, show_sol, show_anim)
        
    def get_maze(self) -> MAZE:
        return self.__maze

    def get_solution(self) -> list[Cord]:
        return self.__sol
