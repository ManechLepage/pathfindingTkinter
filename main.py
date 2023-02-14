import tkinter as tk
import enum


class State(enum.Enum):
    EMPTY = 0
    WALL = 1
    START = 2
    END = 3
    PATH = 4
    VISITED = 5


class Colors(enum.Enum):
    EMPTY = "#262626"
    WALL = "#b0b0b0"
    START = "#00ff00"
    END = "#ff0000"
    PATH = "#00ffff"
    VISITED = "#ff00ff"


class Grid:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.grid = []
        for x in range(rows):
            col = []
            for y in range(cols):
                col.append(State.EMPTY)
            self.grid.append(col)

        self.start = None
        self.end = None


class PathfindingGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pathfinding")
        self.root.geometry("500x500")

        self.grid_canvas = tk.Canvas(self.root, bg="#262626", bd=0, highlightthickness=0)
        self.grid_canvas.pack(expand=True, fill="both")

        self.grid = Grid(50, 50)
        square_size = 50
        for x in range(self.grid.rows):
            for y in range(self.grid.cols):
                color = Colors.EMPTY.value
                if self.grid.grid[x][y] == State.START:
                    color = Colors.START.value
                elif self.grid.grid[x][y] == State.END:
                    color = Colors.END.value
                self.grid_canvas.create_rectangle(x * square_size, y * square_size, (x + 1) * square_size,
                                                  (y + 1) * square_size, fill=color, outline=color)

        self.grid_canvas.bind("<Button-1>", lambda event: self.update_grid(event, Colors.WALL.value))
        self.grid_canvas.bind("<B1-Motion>", lambda event: self.update_grid(event, Colors.WALL.value))
        self.grid_canvas.bind("<Button-3>", lambda event: self.update_grid(event, Colors.EMPTY.value))
        self.grid_canvas.bind("<B3-Motion>", lambda event: self.update_grid(event, Colors.EMPTY.value))

        #TODO: grid not working
        self.buttons = tk.Frame(self.root)
        self.buttons.place(relx=0.5, rely=0, anchor="n")

        self.generate_button = tk.Button(self.buttons, text="Generate")
        self.generate_button.grid(row=0, column=0, sticky="ew", columnspan=2)

        self.dijkstra_button = tk.Checkbutton(self.buttons, text="Dijkstra")
        self.dijkstra_button.grid(row=1, column=0, sticky="ew")

        self.a_star_button = tk.Checkbutton(self.buttons, text="A*")
        self.a_star_button.grid(row=1, column=1, sticky="ew")

        self.reset_button = tk.Button(self.buttons, text="Reset")
        self.reset_button.grid(row=2, column=0, sticky="ew", columnspan=2)

        self.root.mainloop()

    def update_grid(self, event, color):
        closest_square = self.grid_canvas.find_closest(event.x, event.y)[0]
        self.grid_canvas.itemconfig(closest_square, fill=color)


PathfindingGUI()
