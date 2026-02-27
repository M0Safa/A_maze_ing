# mazegen

A reusable Python package for maze generation and solving, built as part of the A-Maze-ing 42 project.

---

## Installation

To install the package locally, first It is recommended to use a virtual environment:

```Bash
python -m venv venv
source venv/bin/activate
```

Then install required build tool and build the packages:

```Bash
pip install build
python3 -m build
```

Now you will be able to install the package:

```Bash
pip install dist/mazegen-1.0.0-py3-none-any.whl
```
After installing the package you can import the class of  `MazeGenerator` and build a maze by entering required parameter
and use provided methodes:
```Python
  from mazegen import MazeGenerator
  maze = MazeGenerator(par["WIDTH"], par["HEIGHT"], par["ENTRY"],
                         par["EXIT"], par["OUTPUT_FILE"], par["PERFECT"],
                         par["ALGORITHM"], par["SEED"])
    maze.generate()
    maze.display(color, show_sol, show_animation)
    maze.get_maze()
    maze.get_solution()
```
