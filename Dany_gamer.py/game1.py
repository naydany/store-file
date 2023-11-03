import random
import tkinter
from tkinter import messagebox
import sys

def some_randomness():
    """ ~ returns random value from -0.5 to 0.5 """
    return random.random() - 0.5

class PaddleBall:
    def __init__(self):
        # window
        root = tkinter.Tk()
        root.geometry("400x200+100+100")
        root.title("Paddle Ball!")

        # used in move_paddle() method
        self.paddle_dy = 10

        # canvas
        self.width = 400
        self.height = 200
        self.my_canvas = tkinter.Canvas(root, bg="white", \
                                    width=self.width, height=self.height)
        self.my_canvas.pack()

        # frame
        self.frm_control = tkinter.Frame(root)
        self.frm_control.pack()

        # oval
        self.radius = 10
        self.x = 375
        self.y = int(self.height / 2) # NEED HELP
        self.my_canvas.create_oval(self.x - self.radius, \
                               self.height / 2 + self.radius, \
                               self.x + self.radius, \
                               self.height / 2 - self.radius,
                               fill="red", tags="disk")

        # paddle
        self.paddle_top = 75
        self.paddle_bot = 125
        self.paddle_x = 15
        # line
        self.my_canvas.create_line(self.paddle_x, self.paddle_top, \
                               self.paddle_x, self.paddle_bot, \
                               width=3, fill="blue", tags="paddle")

        # slot
        self.slot_width = 15
        self.slot_height = 20
        self.slot_top = int(self.height / 2 - self.slot_height)
        self.slot_bot = int(self.height / 2 + self.slot_height)

        # top line - slot
        self.my_canvas.create_line(self.width - self.slot_width / 2, 0, \
                               self.width - self.slot_width / 2, \
                               self.slot_top, width=self.slot_width, \
                               fill="blue", tags="slot")

        # bottom line - slot
        self.my_canvas.create_line(self.width - self.slot_width / 2, \
                               self.slot_bot, \
                               self.width - self.slot_width / 2, \
                               self.height, width=self.slot_width, \
                               fill="blue", tags="slot")

        # bind
        self.my_canvas.bind("<KeyPress-Up>", self.move_paddle_up)
        self.my_canvas.bind("<KeyPress-Down>", self.move_paddle_down)

        self.sleep_time = 30
        self.my_canvas.focus_set()
        self.animate()

    # paddle method(s)
    def move_paddle_up(self, _):
        self.paddle_dy = -abs(self.paddle_dy)
        self.move_paddle()

    def move_paddle_down(self, _):
        self.paddle_dy = abs(self.paddle_dy)
        """ ~ checks if the oval's in the slot:
         1. if the right part of the oval (x + radius) has crossed slot
        entrance (width - slot_width)
         2. if the top oval point (y - radius) is bigger than slot_top position
            and if bottom oval point (y + radius) is smaller than slot_bottom
            position. also, it allows small clipping (2 pixels) to avoid 
            strange bounces on the boundaries of the slot """
        return self.x + self.radius >= self.width - self.slot_width and \
            self.slot_top + self.radius - 2 <= self.y <= \
            self.slot_bot - self.radius + 2

    def is_paddle_on_screen(self):
        """ ~ checks if the paddle is in the screen's boundaries """
        return (self.paddle_dy > 0 or self.paddle_top >= \
                abs(self.paddle_dy)) and self.paddle_bot < \
                self.height - self.paddle_dy

PaddleBall() # anonymous instance