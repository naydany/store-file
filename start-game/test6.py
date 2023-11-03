# import tkinter as tk
# from random import randint, choice

# def scroll_right():
#     canvas.xview('scroll', 1, 'units')

# def auto_scroll():
#     scroll_right()
#     window.after(700, auto_scroll)

# window = tk.Tk()
# window.geometry("1000x400")
# window.title("Game")
# frame = tk.Frame(window)
# frame.pack()
# canvas = tk.Canvas(frame, width=3000, height=400, bg="white")
# canvas.pack()

# # randome shape
# for i in range(100):
#     left = randint(0,3000)
#     top = randint(0,3000)
#     right = left + randint(10, 400)
#     bottom = top + randint(10, 400)
#     color = choice(['red', 'green', 'blue', 'yellow', 'orange', 'purple'])
#     canvas.create_rectangle(left, top, right, bottom, fill=color)

# auto_scroll()


# window.mainloop()


# from tkinter import Tk, Button
# from PIL import Image, ImageTk

# root = Tk()

# # Load the image
# image = Image.open("image/btn_start_game.png")
# # Resize the image to the desired dimensions
# resized_image = image.resize((100, 50))
# # Convert the image to Tkinter format
# tk_image = ImageTk.PhotoImage(resized_image)

# # Create the button with the image
# button = Button(root, image=tk_image, height=50, width=100, compound="center")
# button.pack()

# root.mainloop()

import tkinter as tk
from tkinter import *
import winsound

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
root.title('Group 13 - Game Pro')
canvas = tk.Canvas(root)

game_play = tk.PhotoImage(file="image/bg_show.png")
game_start = tk.PhotoImage(file="image/bg_start.png")

btn_start_game = tk.PhotoImage(file="image/btn_start_game.png")
btn_exit_game = tk.PhotoImage(file="image/btn_exit_game.png")
btn_help_game = tk.PhotoImage(file="image/btn_help_game.png")

def gameShow(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_start)
    canvas.create_image(680, 280, image=btn_start_game, tags="startgame")
    canvas.create_image(680, 410, image=btn_exit_game, tags="exit")
    canvas.create_image(680, 540, image=btn_help_game, tags="help")

def gameStart(event):
    global player, displayKillVirus, displayNumeberBullet, displayTotalCash
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_play)
    # player = canvas.create_image(player_X, player_Y, image=hero)
    # displayKillVirus = canvas.create_text(1087, 47, text=numberOfVirus, font=("serif", 18 ,'bold'), fill="black")
    # displayTotalCash = canvas.create_text(1200, 47, text=totalCash, font=("serif", 18 ,'bold'), fill="black")
    # displayNumeberBullet = canvas.create_text(1310, 47, text=numberOfBullet, font=("serif", 18 ,'bold'), fill="black")

    # for i in range(6):
    #     lives = canvas.create_image(65 + i * 37, 45, image=heard)
    #     listOfLives.append(lives)

    # createVirusAndSize()
    # createCanLive()
    # checkBulletMeetVirus()
    winsound.PlaySound("sound/play.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

canvas.create_image(680, 372, image=game_start)

button_start = tk.Button(image=btn_start_game, command=gameStart)
button_start.place(x=700, y=380)

button_exit = tk.Button(image=btn_exit_game, command=exit)
button_exit.place(x=500, y=510)

button_help = tk.Button(image=btn_help_game, command=help)
button_help.place(x=500, y=640)

winsound.PlaySound("sound/start.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

canvas.pack(expand=True, fill='both')
root.mainloop()