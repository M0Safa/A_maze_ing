import random
from maze_utils import open_dir, Forty_two_cord
from typing import List
MAZE = List[List[str]]
Cord = tuple[int, int]


def open_path(maze: MAZE, cord: Cord, dir: str) -> None:
    (x, y) = cord
    f_t = Forty_two_cord(len(maze[0]), len(maze))
    ops_dirs = {
        "North": ((x - 1, y), "South"),
        "South": ((x + 1, y), "North"),
        "East": ((x, y + 1), "West"),
        "West": ((x, y - 1), "East")
    }
    ((xn, yn), ops_dir) = ops_dirs[dir]
    if (xn, yn) in f_t:
        return
    val = open_dir(maze[x][y], dir)
    val_n = open_dir(maze[xn][yn], ops_dir)
    maze[x][y] = val
    maze[xn][yn] = val_n


def check_neigh(w: int, h: int, visited: list[Cord], cord: Cord):
    (x, y) = cord
    neigh = []
    if (x - 1, y) not in visited and x != 0:
        neigh.append((x - 1, y))
    if (x, y + 1) not in visited and y != w - 1:
        neigh.append((x, y + 1))
    if (x + 1, y) not in visited and x != h - 1:
        neigh.append((x + 1, y))
    if (x, y - 1) not in visited and y != 0:
        neigh.append((x, y - 1))
    return neigh


def maze_gen(p: dict) -> MAZE:
    w = p["WIDTH"]
    h = p["HEIGHT"]
    forty_two = Forty_two_cord(w, h)
    visited = []
    maze = [['F' for _ in range(w)] for _ in range(h)]
    for cell in forty_two:
        visited.append(cell)
    (x, y) = visited[0]
    while (x, y) in visited:
        x = random.randint(0, h - 1)
        y = random.randint(0, w - 1)
    visited.append((x, y))
    stack = [(x, y)]
    while len(visited) < (w * h):
        neigh = check_neigh(w, h, visited, (x, y))
        if not neigh:
            if p['ALGORITHM'] == "DFS":
                (x, y) = stack.pop()
            elif p['ALGORITHM'] == "HK":
                (x, y) = hunt_kill(w, h, visited, stack)
            continue
        stack.append((x, y))
        (xn, yn) = random.choice(neigh)
        visited.append((xn, yn))
        if xn == x - 1:
            open_path(maze, (x, y), "North")
        elif xn == x + 1:
            open_path(maze, (x, y), "South")
        elif yn == y + 1:
            open_path(maze, (x, y), "East")
        elif yn == y - 1:
            open_path(maze, (x, y), "West")
        (x, y) = (xn, yn)
    if not p['PERFECT']:
        not_perfect(maze, 20)
    return maze


def hunt_kill(w: int, h: int, visited: list[Cord], stack: list[Cord]) -> Cord:
    for (x, y) in stack:
        if check_neigh(w, h, visited, (x, y)):
            return (x, y)
    return (0, 0)


def not_perfect(maze: MAZE, percentage: int) -> None:
    w = len(maze[0])
    h = len(maze)
    f_t = Forty_two_cord(w, h)
    for row in range(h):
        for col in range(w):
            if (row, col) in f_t:
                continue
            if random.random() < float(percentage / 100):
                dir = random.choice(["East", "South"])
                if dir == "East" and col == w - 1:
                    dir = "South"
                if dir == "South" and row == h - 1:
                    if col == w - 1:
                        continue
                    dir = "East"
                open_path(maze, (row, col), dir)
