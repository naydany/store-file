
import tkinter as tk
from tkinter import *
import random


# Variable
keyPressed = []
SPEED = 7
TIME = 10
GRAVITY_FORCE = 9
bullet_color = "red"
# Set up a list to store player bullets
player_bullets = []
# Set up a list to store enemy bullets
enemy_bullets = []
scroll_offset = 0
obstacles = []
pol_pots = []
target = None
is_jumping = False
jump_count = 0
SHOOTING_DISTANCE = 300
enemy_ation = 10
direction = 1
WIN_WIDTH=1920
WIN_HIGHT=700
# Create the bullet
bullet = None
root = tk.Tk()
root.title("Game Example")
canvas = tk.Canvas(root, width=1400, height=700)
canvas.pack()

image6 = tk.PhotoImage(file="bg_show1.png")
image_obstacle1 = tk.PhotoImage(file="ground.png")
image_obstacle2= tk.PhotoImage(file="image_obstacle2.png")
image_obstacle3 = tk.PhotoImage(file="image_obstacle3.png")

canvas.create_image(630, 352, image=image6)
background_image_label_1 = canvas.create_image(0, 0, anchor=tk.NW, image=image6)
background_image_label_2 = canvas.create_image(WIN_WIDTH, 0, anchor=tk.NW, image=image6)

player = canvas.create_oval(180, 260, 220, 300, fill="blue")

# player_image = Image.open("./image/soldier.png")
# player_image = player.resize((100, 100))

def game():
    canvas.create_rectangle(0, 600, 1536, 800, fill="Black", tags="wall")
    canvas.pack()
    canvas.bind_all("<KeyPress>",handle_key_press)
    canvas.bind_all("<KeyRelease>",handle_key_release)
    canvas.bind_all("<space>",shoot)
    canvas.focus_set()
    create_obstacles()
    # create_enemies()
    # enemy()
    
  
 
# def create_target():
#     x = random.randint(10, 390)
#     y = random.randint(10, 390)
#     return canvas.create_oval(x, y, x + 20, y + 20, fill="red")

    # Create wall of game
# def create_obstacles():
#     walls = [
#         canvas.create_rectangle(230, 240, 400, 280, fill="white", tags="wall"),
#         canvas.create_rectangle(480, 100, 650, 130, fill="white", tags="wall"),
#         canvas.create_rectangle(780, 200, 950, 230, fill="white", tags="wall"),
#         canvas.create_rectangle(450, 300, 650, 330, fill="Red", tags="wall"),
#         canvas.create_rectangle(850, 360, 900, 390, fill="Red", tags="wall"),
#         canvas.create_rectangle(480, 400, 950, 430, fill="white", tags="wall"),
#         canvas.create_rectangle(1050, 380, 1150, 410, fill="white", tags="wall"),
#         canvas.create_rectangle(240, 480, 330, 510, fill="white", tags="wall")
#         ]
#     for obstacle in walls:
#         obstacles.append(obstacle)


def create_obstacles():
    x1 =scroll_offset + 900  # Start the obstacle just outside the right edge of the screen
    x2 = x1 + random.randint(50, 400)  # Random width of the obstacle
    y1 = random.randint(250, 600)  # Random vertical position of the obstacle
    y2 = y1 + random.randint(20, 60)  # Random height of the obstacle
    return canvas.create_rectangle(x1, y1, x2, y2, fill="black", tags="wall")


# def create_obstacles():
#     x1 = scroll_offset + 900  # Start the obstacle just outside the right edge of the screen
#     y1 = random.randint(250, 600)  # Random vertical position of the obstacle

#     # Randomly select an image from the obstacle_images list
#     obstacle_image = random.choice([image_obstacle1, image_obstacle2, image_obstacle3])  # Add more images if needed

#     # Get the original width and height of the obstacle image
#     original_width = obstacle_image.width()
#     original_height = obstacle_image.height()

#     # Generate random width and height within a certain range
#     width = random.randint(50, 150)  # Adjust the range as needed
#     height = random.randint(20, 60)  # Adjust the range as needed

#     # Scale the obstacle image to the random width and height
#     obstacle_image = obstacle_image.subsample(int(original_width / width), int(original_height / height))

#     # Display the obstacle image on the canvas
#     canvas.create_image(x1, y1, image=obstacle_image, anchor="nw")

#     # Update the screen
#     canvas.update()

#     # Call the function again after a certain delay to create a continuous stream of obstacles
#     canvas.after(2000, create_obstacles)


# image_1 = Image.open("img/0.png")
# imageTk_1 = ImageTk.PhotoImage(image_1)

# def create_ennemy(posX,posY) :
#    canvas.create_image(500, 500, image= imageTk_1, anchor="center"),

#     return  canvas.create_rectangle(
#         posX, posY, posX+50, posX+50, fill="black", tags="solider")


# def create_enemies():
#     enemys = [
#         #create_ennemy(230,40),
#         #create_ennemy(780,200),
#         #create_ennemy(450,300),
#         #create_ennemy(230,40),
#         #create_ennemy(230,40),
#         #create_ennemy(230,40),
#         canvas.create_image(500,200, image= imageTk_1, anchor="center",tags= "change"),
#         canvas.create_image(500,240, image= imageTk_1, anchor="center"),
#         canvas.create_image(500,280, image= imageTk_1, anchor="center"),
#         canvas.create_image(500,340, image= imageTk_1, anchor="center"),
#         canvas.create_image(500,380, image= imageTk_1, anchor="center"),
#         canvas.create_image(500,420, image= imageTk_1, anchor="center")
#         ]
#     for enemy in enemys:
#         pol_pots.append(enemy)
        
# def enemy():
#     for pol_pot in pol_pots:
#         create_bullet(pol_pot)
#         move_enemy(pol_pot)

def create_bullet(pol_pot):
    global bullet, update_id
    hx1, hy1 = canvas.coords(pol_pot)
    px1, py1, px2, py2 = canvas.coords(player)
    if hx1 - px2 <= SHOOTING_DISTANCE and bullet is None:
        
        # Enemy is within shooting distance and bullet is not present, shoot
        bullet = canvas.create_rectangle(hx1, (hy1) + 5 , hx1 - 10, (hy1) + 10, fill="orange")
        

    # Move the bullet
    if bullet is not None:
        canvas.move(bullet, -2, 0)
        bx1, by1, bx2, by2 = canvas.coords(bullet)

        # Check for bullet-player collision
        if bx2 < 0:
            # Bullet reached the end, remove it
            canvas.delete(bullet)
            bullet = None
        elif bx2 > px1 and by1 < py2 and by2 > py1:
            # Bullet collided with the player, end the game
            canvas.create_text(900 // 2, 900 // 2, text="Game Over", font=("Arial", 24))
        
    # window.after_cancel(update_id)
    update_id = root.after(20,create_bullet, pol_pot)



# def move_enemy(pol_pot):
#     global enemy_ation, direction
#     canvas.move(pol_pot, direction, 0)
#     enemy_ation += direction
#     if enemy_ation >= 120:
#         direction = -1
#     elif enemy_ation <= 10:
#         direction = 1
    
#     canvas.after(100, move_enemy,pol_pot)


# study of key that has enter by player
def handle_key_press(event):
    global is_jumping, jump_count
    if event.keysym == "Left" and "Left" not in keyPressed:
        keyPressed.append("Left")
    elif event.keysym == "Right" and "Right" not in keyPressed:
        keyPressed.append("Right")
    elif event.keysym == "Up" and not is_jumping:
        is_jumping = True
        jump_count = 20
    
    # function for release key of player
def handle_key_release(event):
    if event.keysym == "Left" and "Left" in keyPressed:
        keyPressed.remove("Left")
    elif event.keysym == "Right" and "Right" in keyPressed:
        keyPressed.remove("Right")
    
    # function for shooing of charcter
def shoot(event):
    x1, y1, x2, y2 = canvas.coords(player)
    bullet = canvas.create_rectangle(x1 + 20, y1 + 10, x1 + 30, y1 + 20, fill=bullet_color)
    player_bullets.append(bullet)

    # function for move character
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
    # add functions
    move_bullets()
    check_bullet_collision()
    root.after(10,move_player)

    if random.random() < 0.05:
        obstacle =create_obstacles()
        obstacles.append(obstacle)


# Load your action images
# image1 = tk.PhotoImage(file="jump/0.png")
# image2 = tk.PhotoImage(file="jump/1.png")
# image3 = tk.PhotoImage(file="jump/2.png")
# image4 = tk.PhotoImage(file="jump/3.png")
# image5 = tk.PhotoImage(file="jump/4.png")

# Display the initial image

# Define the sequence of images
# image_sequence = [image1, image2, image3,image4,image5]
# def jump_animation():
#     for image in image_sequence:
#         canvas.itemconfig(object_id, image=image)
#         canvas.update()  # Refresh the canvas
#         canvas.after(100)  # Delay between each image
        
        
        
# # Load your action images
# image_walk1 = tk.PhotoImage(file="Run/0.png")
# image_walk2 = tk.PhotoImage(file="Run/1.png")
# image_walk3 = tk.PhotoImage(file="Run/2.png")
# image_walk4 = tk.PhotoImage(file="Run/3.png")
# image_walk5 = tk.PhotoImage(file="Run/4.png")
# image_walk6 = tk.PhotoImage(file="Run/5.png")

# Display the initial image
# object_id = canvas.create_image(100, 100, image=image_walk1)
# walk_action = [image_walk1, image_walk2, image_walk3,image_walk4,image_walk5,image_walk6]

# def walk_animation():
#     for image in walk_action:
#         canvas.itemconfig(object_id, image=image)
#         canvas.update()  # Refresh the canvas
#         canvas.after(100)  # Delay between each image
    

# Check condition of wall```python
def check_movement(item, dx=0, dy=0):
    item_coords = canvas.coords(item)
    new_x1 = item_coords[0] + dx + 5
    new_y1 = item_coords[1] + dy + 5
    new_x2 = item_coords[2] + dx - 5
    new_y2 = item_coords[3] + dy - 5

    overlapping_objects = canvas.find_overlapping(new_x1, new_y1, new_x2, new_y2)

    for wall_id in canvas.find_withtag("wall"):
        if wall_id in overlapping_objects:
            return False

    return True

# Gravity for character
def apply_gravity():
    if not check_movement(player, 0, GRAVITY_FORCE):
        return

    canvas.move(player, 0, GRAVITY_FORCE)
    scroll_screen(0)

def scroll_bg_image(x_direction):
    canvas.move(background_image_label_1, x_direction, 0)
    canvas.move(background_image_label_2, x_direction, 0)

    if canvas.coords(background_image_label_1)[0] < -WIN_WIDTH:
        canvas.coords(background_image_label_1, WIN_WIDTH, 0)
    elif canvas.coords(background_image_label_2)[0] < -WIN_WIDTH:
        canvas.coords(background_image_label_2, WIN_WIDTH, 0)


# Scroll screen
def scroll_screen(x_direction):
    global scroll_offset
    player_coords = canvas.coords(player)
    x1, _, x2, _ = player_coords
    
    if x_direction > 0 and x2 >= 400 -scroll_offset:
        scroll_offset += 40
        canvas.move(player, -10, 0)
        for obstacle in obstacles:
                canvas.move(obstacle, -10, 0)
        for enemy in pol_pots:
                canvas.move(enemy, -10, 0)
    elif x_direction < 0 and x1 <=scroll_offset:
        scroll_offset -= 40
        canvas.move(player, 10, 0)
        for obstacle in obstacles:
            canvas.move(obstacle, 10, 0)
        for enemy in pol_pots:
            canvas.move(enemy, 10, 0)

    

# Move bullets
def move_bullets():
    for bullet in player_bullets:
        canvas.move(bullet, 10, 0)

# Check bullet collision
def check_bullet_collision():
    for bullet in player_bullets:
        bullet_coords = canvas.coords(bullet)
        overlapping_objects =canvas.find_overlapping(*bullet_coords)

        # delect bulet when it thouch someting
        for obstacle in obstacles:
            if obstacle in overlapping_objects:
                canvas.delete(bullet)
                player_bullets.remove(bullet)
                
            
game()
move_player()
root.mainloop()