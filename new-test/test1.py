# import tkinter as tk
# from random import randint, choice
# from PIL import Image, ImageTk

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

# # Create a list to store the PhotoImage objects for all of the images that you want to put behind the canvas.
# image_list = []
# for i in range(1,6):
#     image = Image.open(str(i) + ".jpg")
#     bg_img = ImageTk.PhotoImage(image)
#     image_list.append(bg_img)

# # Iterate over the list of PhotoImage objects and create a create_image() item for each image.
# for image in image_list:
#     canvas.create_image(0, 0, image=image, tag="background")

# # Place the create_image() items behind the canvas by setting the tag option to "background".
# canvas.tag_lower("background")


# auto_scroll()


# window.mainloop()