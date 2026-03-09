from .maze_utils import is_open
from collections import deque
from .maze_gen import MAZE, Cord


def solve_maze(maze: MAZE, entry: Cord, exit: Cord) -> list[Cord]:
    x, y = entry
    queue: deque[tuple[int, int, list]] = deque([(x, y, [])])
    visited = [entry]
    while queue:
        x, y, path = queue.popleft()
        if (x, y) == exit:
            return path
        if (x - 1, y) not in visited and is_open(maze[x][y], "North"):
            new_path = path + [(x - 1, y)]
            visited.append((x - 1, y))
            queue.append((x - 1, y, new_path))
        if (x, y + 1) not in visited and is_open(maze[x][y], "East"):
            new_path = path + [(x, y + 1)]
            visited.append((x, y + 1))
            queue.append((x, y + 1, new_path))
        if (x + 1, y) not in visited and is_open(maze[x][y], "South"):
            new_path = path + [(x + 1, y)]
            visited.append((x + 1, y))
            queue.append((x + 1, y, new_path))
        if (x, y - 1) not in visited and is_open(maze[x][y], "West"):
            new_path = path + [(x, y - 1)]
            visited.append((x, y - 1))
            queue.append((x, y - 1, new_path))
    return []


def solution_dir(path: list[Cord], entry: Cord) -> str:
    result = ""
    (x, y) = entry
    for (xn, yn) in path:
        if xn == x - 1:
            result += 'N'
        elif xn == x + 1:
            result += 'S'
        elif yn == y + 1:
            result += 'E'
        elif yn == y - 1:
            result += 'W'
        (x, y) = (xn, yn)
    return result
