import tkinter as tk
from PIL import Image, ImageTk
from random import randint
import os

WIN_WIDTH = 800
WIN_HEIGHT = 600
SCROLLING_SPEED = 10
PLAYER_SPEED = 10
JUMP_HEIGHT = 10
GRAVITY = 1
NUM_LANDS = 10
LAND_WIDTH = 200
LAND_HEIGHT = 45

# Get the absolute path of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

root = tk.Tk()
root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
root.attributes("-fullscreen", True)

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Load the background image
image_path = os.path.join(script_dir, "..", "images", "background.png")
original_image = Image.open(image_path)

# Calculate the number of background repetitions needed to fill the screen horizontally
num_repetitions = (screen_width // original_image.width) + 2

# Create a new image by concatenating the original image with itself
background_width = original_image.width * num_repetitions
background_image = Image.new("RGBA", (background_width, screen_height))
for i in range(num_repetitions):
    background_image.paste(original_image, (i * original_image.width, 0))

# Create a PhotoImage from the concatenated image
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas and display the background image
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
background_image_label = canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

# Load the player image
# player_image_path = os.path.join(script_dir, "..", "images", "")
# player_image = Image.open(player_image_path)
# player_image = player_image.resize((50, 50))  # Resize the player image
player =canvas.create_rectangle(180, 260, 220, 300, fill="blue")


# Create a player label and place it in the center of the screen
player_label = tk.Label(root, image=None)
player_label.image = ImageTk.PhotoImage(player)
player_label.configure(image=player_label.image)
player_x = screen_width // 2
player_y = screen_height // 2
player_vx = 0
player_vy = 0
player_is_jumping = False

def update_player_position():
    global player_x, player_y, player_vx, player_vy, player_is_jumping

    player_x += player_vx
    player_y += player_vy

    # Check if player is going out of the screen boundaries
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - 50:
        player_x = screen_width - 50

    if player_y < 0:
        player_y = 0
    elif player_y > screen_height - 50:
        player_y = screen_height - 50

    if player_y < screen_height - 50:
        player_vy += GRAVITY
    else:
        player_y = screen_height - 50
        player_vy = 0
        player_is_jumping = False

    player_label.place(x=player_x, y=player_y, anchor=tk.CENTER)
    root.after(10, update_player_position)

update_player_position()

canvas.pack(fill='both', expand=True)

# Function to exit the window when Escape key is pressed
def exit_window(event):
    root.quit()

root.bind('<Escape>', exit_window)

# Function to move the player
def move_player(event):
    global player_vx, player_vy

    if event.keysym == 'Right':
        player_vx = PLAYER_SPEED
        canvas.move(background_image_label, -SCROLLING_SPEED, 0)
    elif event.keysym == 'Left':
        player_vx = -PLAYER_SPEED
        canvas.move(background_image_label, SCROLLING_SPEED, 0)
    elif event.keysym == 'Up':
        player_vy = -GRAVITY * JUMP_HEIGHT
    elif event.keysym == 'Down':
        player_vy = PLAYER_SPEED
    elif event.char == 'w':
        player_vy = -GRAVITY * JUMP_HEIGHT

    # Adjust the wrapping condition for seamless scrolling
    background_coords = canvas.coords(background_image_label)
    background_x = background_coords[0]
    if background_x <= -background_width:
        canvas.move(background_image_label, background_width, 0)
    elif background_x >= 0:
        canvas.move(background_image_label, -background_width, 0)

def stop_player(event):
    global player_vx, player_vy

    if event.keysym in ['Right', 'Left']:
        player_vx = 0
    elif event.keysym in ['Up', 'Down']:
        player_vy = 0
    elif event.char == 'w':
        player_vy = 0

root.bind('<KeyPress>', move_player)
root.bind('<KeyRelease>', stop_player)

# Create the lands
lands = []
land_image_path = os.path.join(script_dir, "..", "images", "land.png")
land_image = Image.open(land_image_path)
land_image = land_image.resize((LAND_WIDTH, LAND_HEIGHT))  # Resize the land image

for _ in range(NUM_LANDS):
    x = randint(0, screen_width - LAND_WIDTH)
    y = randint(0, screen_height - LAND_HEIGHT)
    land_label = tk.Label(root, image=None)
    land_label.image = ImageTk.PhotoImage(land_image)
    land_label.configure(image=land_label.image)
    land_label.place(x=x, y=y)
    lands.append((land_label, x, y))

root.mainloop()