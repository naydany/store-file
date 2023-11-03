# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the window
win.geometry("700x350")

# Make the window size fixed
win.resizable(False,False)

# Create a canvas widget
canvas=Canvas(win, width=700, height=350)
canvas.pack()

# Create an oval or ball in the canvas widget
ball=canvas.create_oval(10,10,50,50, fill="green3")

# Move the ball
xspeed=yspeed=3

def move_ball():
   global xspeed, yspeed

   canvas.move(ball, xspeed, yspeed)
   (leftpos, toppos, rightpos, bottompos)=canvas.coords(ball)
   if leftpos <=0 or rightpos>=700:
      xspeed=-xspeed

   if toppos <=0 or bottompos >=350:
      yspeed=-yspeed

   canvas.after(30,move_ball)

canvas.after(30, move_ball)

win.mainloop()