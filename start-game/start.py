import tkinter as tk
from tkinter import *
from random import randrange

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 740
roof = tk.Tk()

roof.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
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


player_X = 150
player_Y = 450
enamyX = 1400
listOfDiedVirus = []
listOfBullet = []
listOfLives = []
listOfVirus = []
listOfCash = []
numberOfBullet = 45
numberOfVirus = 30
canLive = 6
createVirusSize = 0
countCreateVirus = 0
killVirus = 0
toConfig = 0
totalCash = 0
isStart = True

def processGame():
    if numberOfVirus == 0 and canLive != 0:
        gameWin()
    if numberOfBullet == 0:
        gameOver()
    canvas.after(100, processGame)


# def gameShow(event):
#     canvas.delete("all")
#     canvas.create_image(680, 372, image=game_start)
#     # canvas.create_image(680,280, image=btn_start_game, tags="startgame")
#     # canvas.create_image(680,410,image=btn_exit_game, tags="exit")
#     # canvas.create_image(680,540,image=btn_help_game, tags="help")

def gameStart(event):
    global player, displayKillVirus, displayNumeberBullet, displayTotalCash
    canvas.delete("all")
    canvas.create_image(680, 372,  image=game_play)
    player = canvas.create_image(player_X, player_Y, image=hero)
    displayKillVirus = canvas.create_text(1087, 47, text=numberOfVirus, font=("serif", 18 ,'bold'), fill="black")
    displayTotalCash = canvas.create_text(1200, 47, text=totalCash, font=("serif", 18 ,'bold'), fill="black")
    displayNumeberBullet = canvas.create_text(1310, 47, text=numberOfBullet, font=("serif", 18 ,'bold'), fill="black")

    for i in range(6):
        lives = canvas.create_image(65 + i * 37, 45, image=heard)
        listOfLives.append(lives)

    createVirusAndSize()
    createCanLive()
    checkBulletMeetVirus()
    winsound.PlaySound("sound/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

    
processGame()

canvas.pack(expand=True, fill='both')
roof.mainloop()