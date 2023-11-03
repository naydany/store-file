
import tkinter as tk
from tkinter import *
import winsound
from random import randrange

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 740
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
root.title('Group 13 - Game Pro')
canvas = tk.Canvas(root)
 
# current_image = None
# path_img_1 = "image/background.png"  # images path
# path_img_2 = "image/background2.jpg"
path_img_1 = tk.PhotoImage(file="image/background.png")
path_img_2 = tk.PhotoImage(file="image/background2.jpg")

btn_start_game = tk.PhotoImage(file="image/game_start.png")
btn_exit_game = tk.PhotoImage(file="image/game_exit.png")
btn_help_game = tk.PhotoImage(file="image/game_help.png")

def gameShow(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=path_img_1)
    canvas.create_image(680,280, image=btn_start_game, tags="startgame")
    canvas.create_image(680,410,image=btn_exit_game, tags="exit")
    canvas.create_image(680,540,image=btn_help_game, tags="help")

def gameStart(event):
    global player, displayKillVirus, displayNumeberBullet, displayTotalCash
    canvas.delete("all")
    canvas.create_image(680, 372,  image=path_img_2 )


    # for i in range(6):
    #     lives = canvas.create_image(65 + i * 37, 45, image=heard)
    #     listOfLives.append(lives)

    # createVirusAndSize()
    # createCanLive()
    # checkBulletMeetVirus()
    winsound.PlaySound("sound/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

def move_oval(oval, canvas, master, increase=2):  # move the ball
    x1, y1, x2, y2 = canvas.coords(oval)
    if x1 <= 0:
        increase = 2
    elif x2 >= canvas_width:
        increase = -2
    x1 += increase
    x2 += increase
    canvas.coords(oval, x1, y1, x2, y2)
    master.after(10, lambda: move_oval(oval, canvas, master, increase=increase))
 
 
def resize_image(width, height, path_image):  # create image from the paths and resize them
    image = Image.open(path_image)
    img_copy = image.copy()
    image = img_copy.resize((width, height))
    return image
 
 
# def change_image(to_configure, img_to_change, new_image,master, canvas, alpha=0.0, image=None):  # chenge gradually two     images
#     global current_image
 
#     if alpha > 1:  # if alpha is > 1 the the cycle stops
#         current_image = image
#         return
#     else:
#         new_img = Image.blend(img_to_change, new_image, alpha)  # it modify a bit the image ( depends to the alpha value )
#         modifying_image = ImageTk.PhotoImage(new_img)  # create a Photoimage from the modified image
#         image = modifying_image
#         canvas.itemconfigure(to_configure, image=modifying_image)  # modify the canvas object with the new Photoimage
#         canvas.update()  # update the canvas
#         master.after(50, lambda: change_image(to_configure, img_to_change, new_image, master, canvas,alpha=alpha + 0.2, image=image))  # call again the cycle with alpha increased by 0.2
 
# master = Tk()
# monitor_width = master.winfo_screenwidth()
# monitor_height = master.winfo_screenheight()
# canvas_width = monitor_width
# canvas_height = monitor_height
# x = (monitor_width / 2) - (canvas_width // 2)
# y = (monitor_height / 2) - (canvas_height // 2)
# master.geometry('%dx%d+%d+%d' % (canvas_width + 4, canvas_height + 4, x, y))
# master.title("My game")
# canvas = Canvas(master, width=canvas_width, height=canvas_height, bg="black")
# canvas.place(x=0)
 
 
# img_1 = resize_image(canvas_width, canvas_height, path_img_1)  # resize the    images
# img_2 = resize_image(canvas_width, canvas_height, path_img_2)
 
# img = ImageTk.PhotoImage(img_1)
# image_keeper = img
 
# canvas_image = canvas.create_image(0, 0, image=img, anchor=NW)
 
# oval = canvas.create_oval(350, 340, 370, 360, fill="red")
# move_oval(oval, canvas, master)

# button = Button(canvas, text="change images", command=lambda: change_image(to_configure=canvas_image, img_to_change=img_1, new_image=img_2, master=master, canvas=canvas, alpha=0.0, image=None))
# button.place(x=0)

canvas.tag_bind("gamestart","<Button-1>", gameStart)
canvas.tag_bind("back","<Button-1>", gameShow)

canvas.pack(expand=True, fill='both')

root.mainloop()