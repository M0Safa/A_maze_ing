import sys
import re
from maze_utils import Forty_two_cord


def value_validation(params: dict) -> str:
    # Width validation
    params["WIDTH"] = int(params["WIDTH"])
    if params["WIDTH"] < 9:
        return "WIDTH must be bigger than 9"

    # height validation
    params["HEIGHT"] = int(params["HEIGHT"])
    if params["HEIGHT"] < 7:
        return "Height must be bigger than 7"
    f_t = Forty_two_cord(params["WIDTH"], params["HEIGHT"])

    # Entry and Exit validation
    for cord in ["ENTRY", "EXIT"]:
        if params[cord].count(",") != 1:
            return f"{cord} must be two value seperated by ','"
        x, y = params[cord].split(',')
        params[cord] = int(y), int(x)
        if int(y) > params["HEIGHT"] or int(y) < 0:
            return ("y of entry is out of range")
        if int(x) > params["WIDTH"] or int(x) < 0:
            return ("x of entry is out of range")
        if params[cord] in f_t:
            return (f"{cord} must not be in 42 logo")
    if params["EXIT"] == params["ENTRY"]:
        return "Entry must be different than exit"

    # Output file name validation
    if len(params["OUTPUT_FILE"]) > 255:
        return "the name of output file must be less than 255 char"
    if re.search(r'[\/:*?"<>|]', params["OUTPUT_FILE"]):
        return "File name must not contain illegal char"
    if not params["OUTPUT_FILE"].endswith(".txt"):
        return "Output file must end with .txt"

    # perfect key validation
    if params["PERFECT"] in ("True", "1"):
        params["PERFECT"] = True
    elif params["PERFECT"] in ("False", "0"):
        params["PERFECT"] = False
    else:
        return ("Perfect key must be a bool")

    # algo validation
    if params["ALGORITHM"] not in ["DFS", "HK"]:
        return "Undefined algo choose DFS or HK"

    # seed validation
    if params["SEED"] is not None:
        params["SEED"] = int(params["SEED"])
    return "true"


def text_read() -> dict:
    try:
        if len(sys.argv) != 2:
            raise ValueError("Error: plz enter only the file name")
        keys = ["WIDTH", "HEIGHT", "ENTRY", "EXIT",
                "OUTPUT_FILE", "PERFECT"]
        params = {
            'ALGORITHM': "DFS",
            'SEED': None
        }
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
                if key in ["ALGORITHM", "SEED"]:
                    params[key] = value
                    continue
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
