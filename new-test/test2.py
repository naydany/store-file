import tkinter as tk
from random import randint, choice
from PIL import Image, ImageTk

# def scroll_right():
#   """Scrolls the canvas to the right."""
#   canvas.xview('scroll', 1, 'units')

# def auto_scroll():
#   """Automatically scrolls the canvas to the right."""
#   scroll_right()
#   window.after(700, auto_scroll)

window = tk.Tk()
window.geometry("1000x400")
window.title("Game")
frame = tk.Frame(window)
frame.pack()
canvas = tk.Canvas(frame, width=3000, height=400, bg="white")
canvas.pack()

# Create a list to store the PhotoImage objects for all of the images that you want to put behind the canvas.
image_list = []
# for i in range(1, 6):
#   image = Image.open(str(i) + ".jpg")
#   bg_img = ImageTk.PhotoImage(image)
#   image_list.append(bg_img)

WIN_WIDTH = 1920
WIN_HEIGHT = 700
# SCROLLING_SPEED = 5

original_image = Image.open("4.jpg")
image_resize = original_image.resize((WIN_WIDTH, WIN_HEIGHT))
background_image = ImageTk.PhotoImage(image_resize)

background_image_label_1= canvas.create_image(0, 0,anchor=tk.NW, image=background_image)
background_image_label_2= canvas.create_image(WIN_WIDTH, 0,anchor=tk.NW, image=background_image)


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


# Iterate over the list of PhotoImage objects and create a create_image() item for each image.
# Set the anchor option to "nw" to place the image at the top-left corner of the canvas.
# Set the tag option to "background" to place the image behind the canvas.
for image in image_list:
  canvas.create_image(0, 0, image=image, anchor="nw", tag="background")

# Place the create_image() items behind the canvas by calling the tag_lower() method.
canvas.tag_lower("background")

# # Define axis ranges
# x_min = 0
# x_max = 3000
# y_min = 0
# y_max = 400

# # Create random shapes on the canvas.
# for i in range(100):
#   left = randint(x_min, x_max)
#   top = randint(y_min, y_max)
#   right = left + randint(10, 50)
#   bottom = top + randint(10, 100)
#   color = choice(['red', 'green', 'blue', 'yellow', 'orange', 'purple'])
#   canvas.create_rectangle(left, top, right, bottom, fill=color)

# Start the automatic scrolling.
# auto_scroll()

window.mainloop()