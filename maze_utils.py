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
