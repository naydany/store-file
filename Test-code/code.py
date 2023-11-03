import tkinter as tk
import random
import time
# from PIL import Image, ImageTk

# Variable
keyPressed = []
SPEED = 15
TIME = 10
GRAVITY_FORCE = 9
distance = 0
collected_coins = 0
scroll_offset = 0
obstacles = []
WIN_WIDTH = 1920
canvas_width = 1920
game_over = False
score = 0
is_jumping = False 
width=1920
height=1080
x = 20
y = 20
player_x = width // 2
player_y = height // 2


# Define cash item properties
cash_size = 20
cash_items = []
num_cash_items = 10

# Create the window
window = tk.Tk()
window.title("Mr.Incredible")


# Create a frame
frame = tk.Frame(window)
frame.pack()
canvas = tk.Canvas(frame, width=1920, height=1080)
canvas.pack()

# Load images
# image1 = tk.PhotoImage(file="power_man.png")
# player = canvas.create_image(300, 400, image=image1)

image6 = tk.PhotoImage(file="bg_show1.png")
background_image_label_1 = canvas.create_image(0, 0, anchor=tk.NW, image=image6)
background_image_label_2 = canvas.create_image(WIN_WIDTH, 0, anchor=tk.NW, image=image6)


image1 = tk.PhotoImage(file="power_man.png")
player = canvas.create_image(400, 300, image=image1)

# land = canvas.create_rectangle(0, 500, 1536, 800, fill="Blue", tags="wall")
image7 = tk.PhotoImage(file="land.png")
land = canvas.create_image(768, 650, image=image7, tags="wall")

def game():
    canvas.pack()
    canvas.bind_all("<KeyPress>", handle_key_press)
    canvas.bind_all("<KeyRelease>", handle_key_release)
    canvas.focus_set()
    create_obstacles()
    # create_obstacles()

title_game = tk.PhotoImage(file="ground.png")
title_game1 = tk.PhotoImage(file="barrier.png")

def create_obstacles():
  
    walls = [
        canvas.create_image( 880  ,  272 , image=title_game  , tags="wall")   ,
        canvas.create_image( 680  ,  372 , image=title_game  , tags="wall")   ,
        canvas.create_image( 380  ,  472 , image=title_game  , tags="wall")   ,
        canvas.create_image( 980  ,  572 , image=title_game  , tags="wall")   ,
        canvas.create_image( 1600 ,  570 , image=title_game  , tags="wall")   ,
        canvas.create_image( 1480 ,  470 , image=title_game  , tags="wall")   ,
        canvas.create_image( 1980 ,  400 , image=title_game  , tags="wall")   ,
        canvas.create_image( 3200 ,  380 , image=title_game  , tags="wall")   ,
        canvas.create_image( 2480 ,  570 , image=title_game  , tags="wall")   ,
        canvas.create_image( 2480 ,  540 , image=title_game1 , tags="wall")
    ] 
    for obstacle in walls:
        obstacles.append(obstacle)






# Generate random positions for cash items
def generate_cash_positions():
    for _ in range(num_cash_items):
        x = random.randint(0, width - cash_size)
        y = random.randint(0, height - cash_size)
        cash_items.append((x, y))

# Check collision between the player and cash items
def check_collision():
    for cash_pos in cash_items:
        cash_x, cash_y = cash_pos
        if (player_x + x > cash_x and player_x < cash_x + cash_size) and \
           (player_y + y > cash_y and player_y < cash_y + cash_size):
            cash_items.remove(cash_pos)






def handle_key_press(event):
    global is_jumping, jump_count
    if event.keysym == "Left" and "Left" not in keyPressed:
        keyPressed.append("Left")
    elif event.keysym == "Right" and "Right" not in keyPressed:
        keyPressed.append("Right")
    elif event.keysym == "Up" and not is_jumping:
        is_jumping = True
        jump_count = 20

def handle_key_release(event):
    if event.keysym == "Left" and "Left" in keyPressed:
        keyPressed.remove("Left")
    elif event.keysym == "Right" and "Right" in keyPressed:
        keyPressed.remove("Right")

def move_player():
    global is_jumping, jump_count
    x, y = 0, 0
    if "Left" in keyPressed:
        x = -10
    elif "Right" in keyPressed:
        x = 10

    if is_jumping:
        y = -GRAVITY_FORCE
        jump_count -= 1
        if jump_count == 0:
            is_jumping = False

    if check_movement(player, x, y):
        canvas.move(player, x, y)
    scroll_screen(x)

    if not is_jumping:
        apply_gravity()

    window.after(20, move_player)



    # if random.random() < 0.05:
    #     obstacle =create_obstacles()
    #     obstacles.append(obstacle)

def check_movement(item, dx=0, dy=0):
    item_coords = canvas.coords(item)
    new_x1 = item_coords[0] + dx + 50
    new_y1 = item_coords[1] + dy + 50
    new_x2 = item_coords[0] + dx - 50
    new_y2 = item_coords[1] + dy - 50

    overlapping_objects = canvas.find_overlapping(new_x1, new_y1, new_x2, new_y2)

    for wall_id in canvas.find_withtag("wall"):
        if wall_id in overlapping_objects:
            return False

    return True

def apply_gravity():
    if not check_movement(player, 0, GRAVITY_FORCE):
        return

    canvas.move(player, 0, GRAVITY_FORCE)
    scroll_screen(0)
def scroll_screen(x_direction):
    global scroll_offset
    player_coords = canvas.coords(player)
    x1, _ = player_coords

    if x_direction > 0 and x1 >= 300 - scroll_offset:
        scroll_offset += 40
        canvas.move(player, -10, 0)
        for obstacle in obstacles:
            canvas.move(obstacle, -10, 0)

    elif x_direction < 0 and x1 <= scroll_offset:
        scroll_offset -= 40
        canvas.move(player, 10, 0)
        for obstacle in obstacles:
            canvas.move(obstacle, 10, 0)

def check_game_over():
    global game_over
    player_coords = canvas.coords(player)
    
    if player_coords[1] + 50 >= 539 and 2480 <= player_coords[0] <= 2530:
        game_over = True
        canvas.create_text(canvas.winfo_width() // 2, canvas.winfo_height() // 2, text="Game Over",
                           font=("Helvetica", 36), fill="red")
        canvas.unbind("<KeyPress>")  # Disable key bindings when the game is over


game()
move_player()
window.mainloop()