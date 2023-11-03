import tkinter as tk
from tkinter import *
import winsound
from random import randrange
import random
from tkinter.ttk import *
 
# creates a Tk() object
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


SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
root.title('Group 13 - Game Pro')
canvas = tk.Canvas(root,bg="black")

# ----------image------------
game_level= tk.PhotoImage(file="image/bg_show_lavel.png")
game_start = tk.PhotoImage(file="image/bg_show1.png")
game_play = tk.PhotoImage(file="image/start_game.png")

btn_start_game = tk.PhotoImage(file="image/btn_start3.png")
btn_exit_game = tk.PhotoImage(file="image/btn_exit1.png")
btn_help_game = tk.PhotoImage(file="image/btn_help1.png")
btn_back = tk.PhotoImage(file="image/btn_back1.png")

help_image = tk.PhotoImage(file="image/help_game5.png")
title_game = tk.PhotoImage(file="image/text_main.png")


def gameShow(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_start)
    canvas.create_image(270,530, image=btn_start_game, tags="startgame")
    canvas.create_image(670,530,image=btn_exit_game, tags="exit")
    canvas.create_image(1070,530,image=btn_help_game, tags="help")
    canvas.create_image(680,200,image=title_game, tags="text")

# -----level1-----


# -------level2------
def levelMedium(event):
    canvas.delete("all")
#     canvas.create_image(680, 352,  image=game_play)
    openNewWindow()

# # --------level3--------
def levelHard(event):
    canvas.delete("all")
#     canvas.create_image(680, 352,  image=game_play)
    openNewWindow()

# -------Show_level--------
def showLevel(event):
    canvas.delete("all")
    canvas.create_image(685, 372,  image=game_level)

    canvas.create_text(320, 225, text="Level1",tags="level1", fill='red', font=('Halloween Slime (PERSONAL USE)', 50 ,'bold'))

    canvas.create_text(670, 345, text="Level2",tags="level2", fill='red', font=('Halloween Slime (PERSONAL USE)', 50 ,'bold'))

    canvas.create_text(1020, 445, text="Level3",tags="level3", fill='red', font=('Halloween Slime (PERSONAL USE)', 50 ,'bold'))

    winsound.PlaySound("sound/for_level.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    


# ----------------Exit-------------------
def gameExit(event):
    root.destroy()

# ------------------help-------------------
def gameHelp(event):
    canvas.delete("all")
    canvas.create_image(685, 352, image=help_image)
    canvas.create_image(200, 220, image=btn_back, tags="back")


canvas.create_image(685, 352, image=game_start)

canvas.create_image(680,200,image=title_game, tags="text")
canvas.create_image(270,530, image=btn_start_game, tags="startgame")
canvas.create_image(670,530,image=btn_exit_game, tags="exit")
canvas.create_image(1070,530,image=btn_help_game, tags="help")

winsound.PlaySound("sound/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)


# function to open a new window 
# on a button click
def openNewWindow():
        # Toplevel object which will 
        # be treated as a new window
        root.withdraw()
        newWindow = tk.Toplevel(root)
        # sets the title of the
        # Toplevel widget
        newWindow.title("New Window")
    
        # sets the geometry of toplevel
        newWindow.geometry("1920x1080")
      

        # Define cash item properties
        # cash_size = 20
        # cash_items = []
        # num_cash_items = 10

        # Create the window

        # Create a frame
        frame = tk.Frame(newWindow)
        frame.pack()
        canvas = tk.Canvas(frame, width=1920, height=1080)
        canvas.pack()

        # Load image
        # image1 = tk.PhotoImage(file="power_man.png")
        # player = canvas.create_image(300, 400, image=image1)

        image6 = tk.PhotoImage(file="image/bg_show1.png")
        # background_image_label_1 = canvas.create_image(0, 0, anchor=tk.NW, image=image6)
        # background_image_label_2 = canvas.create_image(WIN_WIDTH, 0, anchor=tk.NW, image=image6)
        canvas.create_image(640, 300, image=image6)
        imgae_player = tk.PhotoImage(file="image/power_man.png")
        player = canvas.create_image(400, 300, image=imgae_player)
        # land = canvas.create_rectangle(0, 500, 1536, 800, fill="Blue", tags="wall")
        image7 = tk.PhotoImage(file="image/land.png")
        canvas.create_image(768, 650, image=image7, tags="wall")

        def game():
            canvas.pack()
            canvas.bind_all("<KeyPress>", handle_key_press)
            canvas.bind_all("<KeyRelease>", handle_key_release)
            canvas.focus_set()
            create_obstacles()
            # create_obstacles()

        ground = tk.PhotoImage(file="image/ground.png")
        ground1 = tk.PhotoImage(file="image/barrier.png")

        def create_obstacles():
        
            walls = [
                canvas.create_image( 880  ,  272 , image=ground  , tags="wall")   ,
                canvas.create_image( 680  ,  372 , image=ground  , tags="wall")   ,
                canvas.create_image( 380  ,  472 , image=ground  , tags="wall")   ,
                canvas.create_image( 980  ,  572 , image=ground  , tags="wall")   ,
                canvas.create_image( 1600 ,  570 , image=ground  , tags="wall")   ,
                canvas.create_image( 1480 ,  470 , image=ground  , tags="wall")   ,
                canvas.create_image( 1980 ,  400 , image=ground  , tags="wall")   ,
                canvas.create_image( 3200 ,  380 , image=ground  , tags="wall")   ,
                canvas.create_image( 2480 ,  570 , image=ground  , tags="wall")   ,
                canvas.create_image( 2480 ,  540 , image=ground1 , tags="wall")
            ] 
            for obstacle in walls:
                obstacles.append(obstacle)
        
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

            root.after(20, move_player)



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


        game()
        move_player()
        newWindow.mainloop()
        # newWindow.mainloop()
        # canvas.create_image(100, 100,  image=game_play)

        # A Label widget to show in toplevel
      

canvas.tag_bind("startgame","<Button-1>", showLevel)
canvas.tag_bind("back","<Button-1>", gameShow)
canvas.tag_bind("exit","<Button-1>", gameExit)
canvas.tag_bind("help","<Button-1>", gameHelp)

canvas.tag_bind("level1","<Button-1>", openNewWindow)
canvas.tag_bind("level1","<Button-1>", levelMedium)
canvas.tag_bind("level1","<Button-1>", levelHard)


canvas.pack(expand=True, fill='both')


#________________level one ___________________

    
root.mainloop()