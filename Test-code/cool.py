import tkinter as tk


from PIL import Image, ImageTk

# Variable

GRAVITY_FORCE = 9


collected_coins = 0

scroll_offset = 0

keyPressed = []
obstacles = []
thorns = []
coin_cash = []

WIN_WIDTH = 1920
width = 1920
height = 1080

is_jumping = False 


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


time_remaining = 60
timer_label = tk.Label(frame, text=f"Time: {time_remaining}s", font=("arial", 20))
timer_label.place(x=900, y=30)
# Score variables
score_count = 0
score_label = tk.Label(frame, text=f"Scores: {score_count}/20", font=("arial", 20))
score_label.place(x=1060, y=30)


image1 = ImageTk.PhotoImage(Image.open("power_man.png"))
player = canvas.create_image(400, 300, image=image1)
player_size = image1.width()

player_x = width // 2
player_y = height // 2

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

def update_game():
    check_collision()

    canvas.delete("all")
    canvas.create_image(player_x, player_y, anchor=tk.CENTER, image=image1)

    for cash_pos in cash_items:
        cash_x, cash_y = cash_pos
        canvas.create_rectangle(cash_x, cash_y, cash_x + cash_size, cash_y + cash_size, fill="red")

    window.after(16, update_game)

# Start the game
update_game()



# land = canvas.create_rectangle(0, 500, 1536, 800, fill="Blue", tags="wall")
image7 = tk.PhotoImage(file="land.png")
land = canvas.create_image(768, 650, image=image7, tags="wall")

def game():
    canvas.pack()
    canvas.bind_all("<KeyPress>", handle_key_press)
    canvas.bind_all("<KeyRelease>", handle_key_release)
    canvas.focus_set()
    create_obstacles()
    create_coins()
    create_thorns()


ground = tk.PhotoImage(file="ground.png")
hazard_thorns= tk.PhotoImage(file="barrier.png")
coin_image = tk.PhotoImage(file="coin.png")

def create_obstacles():
  
    ground_walls = [
        canvas.create_image( 880  ,  272 , image=ground  , tags="wall")   ,
        canvas.create_image( 680  ,  372 , image=ground  , tags="wall")   ,
        canvas.create_image( 380  ,  472 , image=ground  , tags="wall")   ,
        canvas.create_image( 980  ,  572 , image=ground  , tags="wall")   ,
        canvas.create_image( 1600 ,  570 , image=ground  , tags="wall")   ,
        canvas.create_image( 1480 ,  470 , image=ground  , tags="wall")   ,
        canvas.create_image( 1980 ,  400 , image=ground  , tags="wall")   ,
        canvas.create_image( 3200 ,  380 , image=ground  , tags="wall")   ,
        canvas.create_image( 2480 ,  570 , image=ground  , tags="wall")   , 
    ] 
    for obstacle in ground_walls:
        obstacles.append(obstacle)

def create_thorns():
  
    thorn_barriers = [
        canvas.create_image( 880  ,  272 , image=hazard_thorns , tags="thorn")   ,
        canvas.create_image( 680  ,  372 , image=hazard_thorns , tags="thorn")   ,
        canvas.create_image( 380  ,  472 , image=hazard_thorns , tags="thorn")   ,
        canvas.create_image( 980  ,  572 , image=hazard_thorns , tags="thorn")   ,
        canvas.create_image( 1600 ,  570 , image=hazard_thorns , tags="thorn")   ,
        canvas.create_image( 1480 ,  470 , image=hazard_thorns , tags="thorn")   ,
        canvas.create_image( 1980 ,  400 , image=hazard_thorns , tags="thorn")   ,
        canvas.create_image( 3200 ,  380 , image=hazard_thorns , tags="thorn")   ,
        canvas.create_image( 2480 ,  570 , image=hazard_thorns , tags="thorn")   ,
        canvas.create_image( 2480 ,  540 , image=hazard_thorns , tags="thorn")
    ] 
    for hazard_thorn in thorn_barriers:
        
        thorns.append(hazard_thorn)



def create_coins():
    coins = [
        canvas.create_image(800, 200, image=coin_image, tags="coin"),
        canvas.create_image(600, 300, image=coin_image, tags="coin"),
        canvas.create_image(300, 400, image=coin_image, tags="coin"),
        canvas.create_image(900, 500, image=coin_image, tags="coin"),
        canvas.create_image(1500, 498, image=coin_image, tags="coin"),
        canvas.create_image(1380, 398, image=coin_image, tags="coin"),
        canvas.create_image(1880, 328, image=coin_image, tags="coin"),
        canvas.create_image(3100, 308, image=coin_image, tags="coin"),
        canvas.create_image(2380, 498, image=coin_image, tags="coin"),
        canvas.create_image(2380, 468, image=coin_image, tags="coin")
    ]
    for coin in coins:
        coin_cash.append(coin)




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
        x = -20  # Increase the value to speed up movement to the left
    elif "Right" in keyPressed:
        x = 20  # Increase the value to speed up movement to the right

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


def check_movement(item, dx=0, dy=0):
    item_coords = canvas.coords(item)
    new_x1 = item_coords[0] + dx + 50
    new_y1 = item_coords[1] + dy + 50
    new_x2 = item_coords[0] + dx - 50
    new_y2 = item_coords[1] + dy - 50

    overlapping_objects = canvas.find_overlapping(new_x1, new_y1, new_x2, new_y2)
    overlapping_objects = canvas.find_overlapping(new_x1, new_y1, new_x2, new_y2)
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

game()


move_player()
window.mainloop()