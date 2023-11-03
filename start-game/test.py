import tkinter as tk

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 740
roof = tk.Tk()

roof.title('Platformer game - teamA7')
roof.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
canvas = tk.Canvas(roof)

class CharacterSprite(object):
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y

        self.sprite = tk.PhotoImage(file="image/background.png")
        self.canvas.create_image(x, y, image=self.sprite)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

        self.canvas.move(self.sprite, dx, dy)

# class Game(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.canvas = tk.Canvas(self, width=500, height=500)
#         self.canvas.pack()

#         self.character = CharacterSprite(self.canvas, 100, 100)

#         self.bind("<KeyPress>", self.on_key_press)

#     def on_key_press(self, event):
#         key = event.keysym

#         if key == "Left":
#             self.character.move(-5, 0)
#         elif key == "Right":
#             self.character.move(5, 0)
#         elif key == "Up":
#             self.character.move(0, -5)
#         elif key == "Down":
#             self.character.move(0, 5)

if __name__ == "__main__":
    # game = Game()
    roof.mainloop()