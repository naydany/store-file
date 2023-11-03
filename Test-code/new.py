import tkinter as tk
from PIL import ImageTk, Image
import random

# Create the main window
window_width = 800
window_height = 600
window = tk.Tk()
window.title("Platformer Game")

# Load player image
player_image_path = "power_man.png"
player_image = ImageTk.PhotoImage(Image.open(player_image_path))
player_size = player_image.width()
player_x = window_width // 2
player_y = window_height // 2

# Define colors
WHITE = "#ffffff"

# Define cash item properties
cash_size = 20
cash_items = []
num_cash_items = 10

# Generate random positions for cash items
def generate_cash_positions():
    for _ in range(num_cash_items):
        x = random.randint(0, window_width - cash_size)
        y = random.randint(0, window_height - cash_size)
        cash_items.append((x, y))

# Check collision between the player and cash items
def check_collision():
    for cash_pos in cash_items:
        cash_x, cash_y = cash_pos
        if (player_x + player_size > cash_x and player_x < cash_x + cash_size) and \
           (player_y + player_size > cash_y and player_y < cash_y + cash_size):
            cash_items.remove(cash_pos)

# Create the game canvas
canvas = tk.Canvas(window, width=window_width, height=window_height)
canvas.pack()

generate_cash_positions()

def move_left(event):
    global player_x
    player_x -= 5

def move_right(event):
    global player_x
    player_x += 5

def move_up(event):
    global player_y
    player_y -= 5

def move_down(event):
    global player_y
    player_y += 5

# Bind arrow key events to movement functions
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)

def update_game():
    check_collision()

    canvas.delete("all")
    canvas.create_image(player_x, player_y, anchor="nw", image=player_image)

    for cash_pos in cash_items:
        cash_x, cash_y = cash_pos
        canvas.create_rectangle(cash_x, cash_y, cash_x + cash_size, cash_y + cash_size, fill="red")

    window.after(16, update_game)

update_game()

# Start the main loop
window.mainloop()