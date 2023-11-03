import tkinter as tk


# from PIL import Image, ImageTk

# Variable

GRAVITY_FORCE = 9
distance = 0

collected_coins = 0

scroll_offset = 0

keyPressed = []
obstacles = []
thorns = []
coin_cash = []

WIN_WIDTH = 1920
width = 1920
height = 1080

is_jumping = False 


window = tk.Tk()
window.title("Mr.Incredible")


# Create a frame
frame = tk.Frame(window)
frame.pack()
canvas = tk.Canvas(frame, width=1920, height=1080)
canvas.pack()