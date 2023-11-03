import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Platform Game")
root.attributes('-fullscreen', True)

game_play = tk.PhotoImage(file="bg_show1.png")


canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="white")
canvas = tk.Canvas(root,bg="black")
canvas.pack(fill=tk.BOTH, expand=True)


# canvas.delete("all")
canvas.create_image(680, 420, image=game_play)

platform = canvas.create_rectangle(50, root.winfo_screenheight() - 50, root.winfo_screenwidth() - 50, root.winfo_screenheight() - 40, fill="black")

player = canvas.create_oval(root.winfo_screenwidth() // 2 - 10, root.winfo_screenheight() - 60, root.winfo_screenwidth() // 2 + 10, root.winfo_screenheight() - 40, fill="blue")

lives = 3

lives_label = tk.Label(root, text="Lives: " + str(lives), font=("Arial", 16))
lives_label.place(x=20, y=20)  # Position the label at the top-left corner

left_key_label = tk.Label(root, text="L", font=("Arial", 24), fg="red")
left_key_label.place(x=20, y=root.winfo_screenheight() - 60)

def lose_life():
    global lives
    lives -= 1
    lives_label.config(text="Lives: " + str(lives))
    
    if lives == 0:
        messagebox.showinfo("Game Over", "You ran out of lives!")
        root.quit()

def move_left(event):
    canvas.move(player, -10, 0)
    check_collision()

def move_right(event):
    canvas.move(player, 10, 0)
    check_collision()

def check_collision():
    player_coords = canvas.coords(player)
    platform_coords = canvas.coords(platform)
    
    if player_coords[2] >= platform_coords[0] and player_coords[0] <= platform_coords[2] and player_coords[3] >= platform_coords[1]:
        lose_life()

root.bind('<Left>', move_left)
root.bind('<Right>', move_right)

root.mainloop()