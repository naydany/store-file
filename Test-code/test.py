import tkinter as tk
from PIL import Image, ImageTk

WIN_WIDTH = 1920
WIN_HEIGHT = 700
SCROLLING_SPEED = 5
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 5

root = tk.Tk()
root.geometry(str(WIN_WIDTH) + "x" + str(WIN_HEIGHT))

frame = tk.Frame()
canvas = tk.Canvas(frame)

original_image = Image.open("bg_image.jpg")
image_resize = original_image.resize((WIN_WIDTH, WIN_HEIGHT))
background_image = ImageTk.PhotoImage(image_resize)

background_image_label_1 = canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
background_image_label_2 = canvas.create_image(WIN_WIDTH, 0, anchor=tk.NW, image=background_image)

player_rect = canvas.create_rectangle(
    WIN_WIDTH // 2 - PLAYER_WIDTH // 2,
    WIN_HEIGHT // 2 - PLAYER_HEIGHT // 2,
    WIN_WIDTH // 2 + PLAYER_WIDTH // 2,
    WIN_HEIGHT // 2 + PLAYER_HEIGHT // 2,
    fill="red"
)

has_player_moved = False

def scroll_bg_image(x_direction):
    canvas.move(background_image_label_1, x_direction, 0)
    canvas.move(background_image_label_2, x_direction, 0)

    if canvas.coords(background_image_label_1)[0] < -WIN_WIDTH:
        canvas.coords(background_image_label_1, WIN_WIDTH, 0)
    elif canvas.coords(background_image_label_2)[0] < -WIN_WIDTH:
        canvas.coords(background_image_label_2, WIN_WIDTH, 0)

def move_player(event):
    global has_player_moved

    if not has_player_moved:
        has_player_moved = True
        return

    if event.keysym == "Right":
        scroll_bg_image(-SCROLLING_SPEED)
    elif event.keysym == "Left":
        scroll_bg_image(SCROLLING_SPEED)

canvas.bind_all("<KeyPress>", move_player)
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

root.mainloop()