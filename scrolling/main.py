import tkinter as tk
from PIL import Image, ImageTk
from random import randint, choice


def scroll_right():
  """Scrolls the canvas to the right."""
  canvas.xview('scroll', 1, 'units')

def auto_scroll():
  """Automatically scrolls the canvas to the right."""
  scroll_right()
  root.after(700, auto_scroll)

WIN_WIDTH = 1920
WIN_HEIGHT = 700
SCROLLING_SPEED = 4
root = tk.Tk()
root.geometry(str(WIN_WIDTH) + "x" + str(WIN_HEIGHT))

frame = tk.Frame()
canvas = tk.Canvas(frame)
original_image = Image.open("bg_image.jpg")
image_resize = original_image.resize((WIN_WIDTH, WIN_HEIGHT))
background_image = ImageTk.PhotoImage(image_resize)

background_image_label_1= canvas.create_image(0, 0,anchor=tk.NW, image=background_image)
background_image_label_2= canvas.create_image(WIN_WIDTH, 0,anchor=tk.NW, image=background_image)

class Game:
    def __init__(self, root):
      self.canvas.create_rectangle(0, 600, 1336, 700, fill="black", tags="wall")
      self.canvas.pack()

def handle_key_press(self, event):
    if event.keysym == "Left" and "Left" not in keyPressed:
        keyPressed.append("Left")
    elif event.keysym == "Right" and "Right" not in keyPressed:
        keyPressed.append("Right")
    elif event.keysym == "Up" and not self.is_jumping:
        self.is_jumping = True
        self.jump_count = 20

def scroll_bg_image():
    
    canvas.move(background_image_label_1, -1, 0)
    canvas.move(background_image_label_2, -1, 0)

    if canvas.coords(background_image_label_1)[0]< -1920:
        canvas.coords(background_image_label_1, 1920, 0)
    elif canvas.coords(background_image_label_2)[0]< -1920:
        canvas.coords(background_image_label_2, 1920, 0)
    canvas.after(5, scroll_bg_image)


scroll_bg_image()

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Define axis ranges
x_min = 0
x_max = 3000
y_min = 0
y_max = 400

# Create random shapes on the canvas.
for i in range(100):
  left = randint(x_min, x_max)
  top = randint(y_min, y_max)
  right = left + randint(10, 50)
  bottom = top + randint(10, 100)
  color = choice(['red', 'green', 'blue', 'yellow', 'orange', 'purple'])
  canvas.create_rectangle(left, top, right, bottom, fill=color)

auto_scroll()


root.mainloop()