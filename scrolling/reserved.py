import tkinter as tk
import random
from PIL import Image, ImageTk
from random import choice

# from random import randint, choice
root = tk.Tk()
root.title("Game Example")
WIN_WIDTH = 1400
WIN_HEIGHT = 700
SCROLLING_SPEED = 4


keyPressed = []
SPEED = 7
TIME = 10
GRAVITY_FORCE = 9

class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=1400, height=700)
        self.canvas.pack()
        self.canvas.create_rectangle(0, 600, 1336, 700, fill="black", tags="wall")
        self.canvas.pack()
        self.player = self.canvas.create_rectangle(180, 260, 220, 300, fill="blue")
        # self.player_image = ImageTk.PhotoImage(file="player.jpg")
        # self.player = self.canvas.create_image(200, 280, anchor=tk.NW, image=self.player_image)
        self.canvas.bind_all("<KeyPress>", self.handle_key_press)
        self.canvas.bind_all("<KeyRelease>", self.handle_key_release)
        self.canvas.focus_set()
        self.scroll_offset = 0
        self.obstacles = []
        self.target = self.create_target()
        self.is_jumping = False
        self.jump_count = 0
        original_image = Image.open("bg_image.jpg")
        image_resize = original_image.resize((WIN_WIDTH, WIN_HEIGHT))
        self.background_image = ImageTk.PhotoImage(image_resize)

        self.background_image_label = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

    # -------------image_scroll creen------------
    def scroll_screen(self, x_direction):
        player_coords = self.canvas.coords(self.player)
        x1, _, x2, _ = player_coords

        if x_direction > 0 and x2 >= 400 - self.scroll_offset:
            self.scroll_offset += 40
            self.canvas.move(self.player, -10, 0)
            self.canvas.move(self.target, -10, 0)
            for obstacle in self.obstacles:
                self.canvas.move(obstacle, -10, 0)
            self.canvas.move(self.background_image_label, -10, 0)  # Move the background image
        elif x_direction < 0 and x1 <= self.scroll_offset:
            self.scroll_offset -= 40
            self.canvas.move(self.player, 10, 0)
            self.canvas.move(self.target, 10, 0)
            for obstacle in self.obstacles:
                self.canvas.move(obstacle, 10, 0)
            self.canvas.move(self.background_image_label, 10, 0)  # Move the background image

    def create_target(self):
        x = random.randint(10, 390)
        y = random.randint(10, 390)
        return self.canvas.create_oval(x, y, x + 20, y + 20, fill="red")

    

    def create_obstacle(self):
        x1 = self.scroll_offset + 900  # Start the obstacle just outside the right edge of the screen
        x2 = x1 + random.randint(50, 150)  # Random width of the obstacle
        y1 = random.randint(150, 400)  # Random vertical position of the obstacle
        y2 = y1 + random.randint(20, 60)  # Random height of the obstacle
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", tags="wall")
        # original_land_image = Image.open("ground.jpg")
        # land_image_resize = original_land_image.resize((WIN_WIDTH, 100))
        # self.land_image = ImageTk.PhotoImage(land_image_resize)
        # self.land_image_label = self.canvas.create_image(0, WIN_HEIGHT - 100, anchor=tk.NW, image=self.land_image)


    def handle_key_press(self, event):
        if event.keysym == "Left" and "Left" not in keyPressed:
            keyPressed.append("Left")
        elif event.keysym == "Right" and "Right" not in keyPressed:
            keyPressed.append("Right")
        elif event.keysym == "Up" and not self.is_jumping:
            self.is_jumping = True
            self.jump_count = 20

    def handle_key_release(self, event):
        if event.keysym == "Left" and "Left" in keyPressed:
            keyPressed.remove("Left")
        elif event.keysym == "Right" and "Right" in keyPressed:
            keyPressed.remove("Right")

    def move_player(self):
        x, y = 0, 0

        if "Left" in keyPressed:
            x = -10
        elif "Right" in keyPressed:
            x = 10

        if self.is_jumping:
            y = -GRAVITY_FORCE
            self.jump_count -= 1
            if self.jump_count == 0:
                self.is_jumping = False

        if self.check_movement(self.player, x, y):
            self.canvas.move(self.player, x, y)

        # Call scroll_screen method to update scrolling position
        self.scroll_screen(x)

        if not self.is_jumping:
            self.apply_gravity()

        self.root.after(20, self.move_player)

        # Create obstacles while moving
        if random.random() < 0.05:
            obstacle = self.create_obstacle()
            self.obstacles.append(obstacle)
    def check_movement(self, item, dx=0, dy=0):
        item_coords = self.canvas.coords(item)
        new_x1 = item_coords[0] + dx + 9
        new_y1 = item_coords[1] + dy + 9
        new_x2 = item_coords[2] + dx - 7
        new_y2 = item_coords[3] + dy - 7   

        overlapping_objects = self.canvas.find_overlapping(new_x1, new_y1, new_x2, new_y2)

        for wall_id in self.canvas.find_withtag("wall"):
            if wall_id in overlapping_objects:
                return False

        return True

    def apply_gravity(self):
        if not self.check_movement(self.player, 0, GRAVITY_FORCE):
            return

        self.canvas.move(self.player, 0, GRAVITY_FORCE)
        self.scroll_screen(0)
    def scroll_screen(self, x_direction):
        player_coords = self.canvas.coords(self.player)
        x1, _, x2, _ = player_coords

        # if x_direction > 0 and x2 >= 400 - self.scrollThe code got cut off. Here's the continuation:

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



game = Game(root)
game.move_player()

root.mainloop()