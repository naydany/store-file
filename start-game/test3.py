import tkinter as tk
import random

window = tk.Tk()
window.geometry('500x500')
frame = tk.Frame(window, width=500, height=500)
frame.pack()

canvas = tk.Canvas(frame, width=500, height=500)
canvas.pack()

colors = ["red","pink","orange","teal","lightblue","purple"]

def create_oval():
    positionx = random.randint(0,400)
    positiony = random.randint(0,400)
    size = random.randint(20,200)
    color = random.choice(colors)
    canvas.create_oval(positionx,positiony,positionx+size,positiony+size,fill = color)
    canvas.after(500,create_oval)
create_oval()

window.bind("<Button-1>",create_oval)
window.mainloop()