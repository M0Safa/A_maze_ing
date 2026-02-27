# A_Maze_Ing

This project has been created as part of the 42 curriculum by [mosafa]https://profile-v3.intra.42.fr/users/mosafa [melhajj]https://profile-
v3.intra.42.fr/users/melhajj

## Description

This project is a terminal-based maze utility that leverages graph theory algorithms to generate and solve complex. Using either Depth-First Search 
(DFS) or the Hunt-and-Kill (HK) algorithm, the program procedurally carves out a random grid based on user-defined dimensions, entry and exit points To complement 
the generation, the tool implements a Breadth-First Search (BFS) algorithm to calculate and display the shortest possible path between the start and finish. The 
entire experience is brought to life through a dynamic ASCII rendering engine in the terminal, featuring real-time animations, customizable color schemes, and the 
ability to toggle the solution path's visibility on the fly.


## Instructions

For using the script of Maze generator run `a_maze_ing.py` by puting your desired paramters in the `config.txt`:

```Bash
make run
```
And for run the main script in debug mode:

```Bash
make debug
```
To clean temporary files:

```Bash
make clean
```
Lastly to run flake8 and mypy:

```Bash
make lint
```
The program doesnt required any package to install so no need to run `make install`.
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

## Resource

DFS algorithm: https://youtu.be/PMMc4VsIacU?si=pcedlGLbZPUAi9nH

BFS algorithm: https://youtu.be/xlVX7dXLS64?si=I0ZYINY7la3RAYzp

HK algorithm:  same as DFS but with different backtracking methode

**We used AI to help figure out the ASCII rendering (getting those characters to look like a real maze!) and to help polish the logic for the generation 
algorithms.**

### 1) Complete config structure and format:

[config.txt:]

```bash
WIDTH=20 #(mandatory) can't be float or negative
HEIGHT=20 #(mandatory) can't be float or negative
ENTRY=0,0 #(mandatory) can't be float or negative
EXIT=19,19 #(mandatory) can't be float or negative
OUTPUT_FILE=maze.txt #(mandatory) where the output should be written
PERFECT=0 #(mandatory) defines if the maze will have two or one solution
seed=333   #(optional) negatives and 0 are included
algorithm=DFS #(optional) can use HK instead
```

### 2) Maze generation algorithm chosen:

Primary chosen algorithm (for default runs): DFS:
**We chose DFS because:**
- Very simple and intuitive to implement.
- Produces long, deep corridors that are visually clean and easy to debug.
- Perfect for educational purposes since it clearly demonstrates stack-based backtracking.
- <u>And because it was the first one we started with, so obviously it's the default one.</u>

Secondary is: HK (Hunt and kill)

- For learning purposes.

### 3) What part of your code is reusable, and how:

The class MazeGenerator in mazegen package. you can used as demonstarated in the instructions part

### 4) Team & project management

- **Team members & roles**
    
    - `mosafa`: .
        
    - `melhajj`: .
        
- **Planning & evolution**
    
    - Initial plan: parameter reader and validator → implement generator + simple visualizer → add solvers → tests.
        
    - Evolved: we add another maze generator algorithm `HK` and we add animation to maze drawing 
        
    - It took us some time but in the end we delivered :)
        
- **What worked well**
    
    The most part that worked well is using terminal (ASCII rendering) to display the maze. we used block with different collors that give
    a beautiful representation to maze and also using clear and sleep function we were able to add animation 
        
- **What could be improved**
    
  - we could add more colors (there is only 3)
  - we could provide more algorithms (there is only 2 and they are similar)
  - we could use another display methode like Mlx
        

### 5) Tools used

- Git + GitHub
    
- Python 3.10 (project code)
    
- Make (convenience commands)

- Poetry (to build the package)
