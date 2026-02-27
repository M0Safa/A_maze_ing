def is_open(c: str, dir: str) -> bool:
    dirs = ["North", "East", "South", "West"]
    i = dirs.index(dir)
    nb = int(c, 16)
    if (nb >> i) & 1 == 0:
        return True
    return False


def close_dir(c: str, dir: str) -> str:
    dirs = ["North", "East", "South", "West"]
    i = dirs.index(dir)
    nb = int(c, 16)
    if (nb >> i) & 1 == 1:
        return c
    return hex(nb + (2 ** i))[2:].upper()


def open_dir(c: str, dir: str) -> str:
    dirs = ["North", "East", "South", "West"]
    i = dirs.index(dir)
    nb = int(c, 16)
    if (nb >> i) & 1 == 0:
        return c
    return hex(nb - (2 ** i))[2:].upper()


def Forty_two_cord(width: int, height: int) -> list[tuple[int, int]]:
    a = int(height / 2)
    b = int(width / 2)
    forty_two = [(a - 2, b - 3), (a - 1, b - 3), (a, b - 3), (a, b - 2),
                 (a, b - 1), (a + 1, b - 1), (a + 2, b - 1), (a - 2, b + 1),
                 (a, b + 1), (a + 1, b + 1), (a + 2, b + 1), (a - 2, b + 2),
                 (a, b + 2), (a + 2, b + 2), (a - 2, b + 3), (a - 1, b + 3),
                 (a, b + 3), (a + 2, b + 3)]
    return forty_two


def intro_display() -> None:
    print("=== A-Maze-ing ===")
    print("1. Re-generate a new maze")
    print("2. Show/Hide path from entry to exit")
    print("3. Rotate maze colors")
    print("4. Quit")


def maze_output(par: dict, maze: list[list[str]], sol_dir: str) -> None:
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
