import os
import time
from .maze_utils import is_open, Forty_two_cord
from .maze_gen import MAZE, Cord


def grid_disp(grid: MAZE):
    os.system('clear')
    for row in grid:
        print("".join(row))
    print("")


def sol_paint(grid: MAZE, sol_nodes: list[Cord],
              entry: Cord, exit: Cord, SOL: str) -> None:
    x, y = entry
    for (xn, yn) in sol_nodes:
        vr, vc = 2 * xn + 1, 2 * yn + 1
        if (xn, yn) != exit:
            grid[vr][vc] = SOL
        if xn == x - 1:
            grid[vr + 1][vc] = SOL
        elif xn == x + 1:
            grid[vr - 1][vc] = SOL
        elif yn == y + 1:
            grid[vr][vc - 1] = SOL
        elif yn == y - 1:
            grid[vr][vc + 1] = SOL
        grid_disp(grid)
        time.sleep(0.01)
        (x, y) = (xn, yn)


def path_paint(maze: MAZE, grid: MAZE, rows: int, cols: int,
               anim: bool, PATH: str) -> None:
    for r in range(rows):
        for c in range(cols):
            val = maze[r][c]
            vr, vc = 2 * r + 1, 2 * c + 1
            if is_open(val, "North"):
                grid[vr-1][vc] = PATH
            if is_open(val, "East"):
                grid[vr][vc+1] = PATH
            if is_open(val, "South"):
                grid[vr+1][vc] = PATH
            if is_open(val, "West"):
                grid[vr][vc-1] = PATH
            if anim:
                grid_disp(grid)
                time.sleep(0.005)


def draw_maze(maze: MAZE, entry: Cord, exit: Cord, color: str,
              sol_nodes: list[Cord], draw_sol: bool, anim: bool) -> None:
    WALL = f"\033[{color}m\u2588\u2588\033[0m"
    PATH = "  "
    START = "\033[35m\u2588\u2588\033[0m"
    EXIT = "\033[31m\u2588\u2588\033[0m"
    BLUE = "\033[34m\u2588\u2588\033[0m"
    SOL = "\033[32m\u2588\u2588\033[0m"
    rows = len(maze)
    cols = len(maze[0])
    f_t = Forty_two_cord(cols, rows)
    v_rows = 2 * rows + 1
    v_cols = 2 * cols + 1
    grid = [[WALL for _ in range(v_cols)] for _ in range(v_rows)]
    for r in range(rows):
        for c in range(cols):
            vr, vc = 2 * r + 1, 2 * c + 1
            grid[vr][vc] = PATH
    for x, y in f_t:
        grid[2 * x + 1][2 * y + 1] = BLUE
    er, ec = entry
    grid[2 * er + 1][2 * ec + 1] = START
    xr, xc = exit
    grid[2 * xr + 1][2 * xc + 1] = EXIT
    path_paint(maze, grid, rows, cols, anim, PATH)
    grid_disp(grid)
    if draw_sol:
        sol_paint(grid, sol_nodes, entry, exit, SOL)
    grid_disp(grid)
