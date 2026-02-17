import sys
from maze_utils import Forty_two_cord


def value_validation(params: dict) -> str:
    params["WIDTH"] = int(params["WIDTH"])
    if params["WIDTH"] < 9:
        return "WIDTH must be bigger than 9"
    params["HEIGHT"] = int(params["HEIGHT"])
    if params["HEIGHT"] < 7:
        return "Height must be bigger than 7"
    f_t = Forty_two_cord(params["WIDTH"], params["HEIGHT"])
    if params["ENTRY"].count(",") != 1:
        return "Entry must be two value seperated by ','"
    if params["EXIT"].count(",") != 1:
        return "Exit must be two value seperated by ','"
    if params["EXIT"] == params["ENTRY"]:
        return "Entry must be different than exit"
    x, y = params["ENTRY"].split(',')
    params["ENTRY"] = int(y), int(x)
    if int(y) > params["HEIGHT"] or int(y) < 0:
        return ("y of entry is out of range")
    if int(x) > params["WIDTH"] or int(x) < 0:
        return ("x of entry is out of range")
    x, y = params["EXIT"].split(',')
    params["EXIT"] = int(y), int(x)
    if int(y) > params["HEIGHT"] or int(y) < 0:
        return ("y of exit is out of range")
    if int(x) > params["WIDTH"] or int(x) < 0:
        return ("y of exit is out of range")
    if params["ENTRY"] in f_t:
        return ("Entry must not be in 42 logo")
    if params["EXIT"] in f_t:
        return ("Exit must not be in 42 logo")
    if not params["OUTPUT_FILE"].endswith(".txt"):
        return "Output file already exist"
    if params["PERFECT"] in ("True", "1"):
        params["PERFECT"] = True
    elif params["PERFECT"] in ("False", "0"):
        params["PERFECT"] = False
    else:
        return ("Perfect key must be a bool")
    return "true"


def text_read() -> dict:
    try:
        if len(sys.argv) != 2:
            raise ValueError("Error: plz enter only the file name")
        keys = ["WIDTH", "HEIGHT", "ENTRY", "EXIT",
                "OUTPUT_FILE", "PERFECT"]
        params = {}
        file_name = sys.argv[1]
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                if line[0] == '#':
                    continue
                if line.count("=") != 1:
                    raise ValueError("enter only key and value " +
                                     "seperated with'='")
                key, value = line.split('=')
                if key not in keys:
                    raise ValueError("enter only right key and once")
                keys.remove(key)
                params[key] = value
            if keys:
                raise ValueError(f"you miss those key:{keys}")
            msg = value_validation(params)
            if msg != "true":
                raise ValueError(msg)
    except FileNotFoundError:
        print("Error:wrong file name")
        return {}
    except ValueError as e:
        print(e)
        return {}
    return params
