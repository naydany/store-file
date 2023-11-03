import tkinter as tk
import random



class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.canvas.create_rectangle(0, 300, 1536, 400, fill="Brown", tags="wall")
        self.canvas.pack()
        self.player = self.canvas.create_rectangle(180, 260, 220, 300, fill="blue")
        self.canvas.bind_all("<KeyPress>", self.move_player)
        self.canvas.focus_set()
        self.scroll_offset = 0
        self.obstacles = []
        self.target = self.create_target()
        self.create_obstacles()

    def create_target(self):
        x = random.randint(10, 390)
        y = random.randint(10, 390)
        return self.canvas.create_oval(x, y, x+20, y+20, fill="red")

    # Create levels of game
    def create_obstacles(self):
        walls = [self.canvas.create_rectangle(230, 160, 400, 190, fill="white",tags="wall"),
                 self.canvas.create_rectangle(480, 100, 650, 130, fill="white",tags="wall"),
                 self.canvas.create_rectangle(780, 200, 950, 230, fill="white",tags="wall"),
                 self.canvas.create_rectangle(450, 300, 650, 330, fill="Red",tags="wall"),
                 self.canvas.create_rectangle(850, 360, 900, 390, fill="Red",tags="wall"),
                 self.canvas.create_rectangle(480, 400, 950, 430, fill="white",tags="wall"),
                 self.canvas.create_rectangle(1050, 380, 1150, 410, fill="white",tags="wall"),
                 self.canvas.create_rectangle(240, 480, 330, 510, fill="white",tags="wall")]
        for obstacle in walls:  
            self.obstacles.append(obstacle)

    # move player
    def move_player(self, event):
        x, y = 0, 0
        if event.keysym == "Left":
            x = -10
        elif event.keysym == "Right":
            x = 10
        
        # elif event.keysym == "Up":
        #     y = -10
        # elif event.keysym == "Down":
        #     y = 10
        # self.check_collision()
        self.canvas.move(self.player, x, y)
        self.scroll_screen(x)
      
    def scroll_screen(self, x_direction):
        player_coords = self.canvas.coords(self.player)
        x1, _, x2, _ = player_coords

        if x_direction > 0 and x2 >= 400 - self.scroll_offset:
            self.scroll_offset += 40
            self.canvas.move(self.player, -10, 0)
            self.canvas.move(self.target, -10, 0)
            for obstacle in self.obstacles:
                self.canvas.move(obstacle, -10, 0)
        elif x_direction < 0 and x1 <= self.scroll_offset:
            self.scroll_offset -= 40
            self.canvas.move(self.player, 10, 0)
            self.canvas.move(self.target, 10, 0)
            for obstacle in self.obstacles:
                self.canvas.move(obstacle, 10, 0)

    
# Create the main Tkinter window
root = tk.Tk()
root.title("Game Example")



# Create the game instance
game = Game(root)

# Start the Tkinter event loop
root.mainloop()