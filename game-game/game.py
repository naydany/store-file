import tkinter as tk 
import winsound
import random
windows=tk.Tk()
windows.title("Gamve VC1")
windows.geometry("700x650")
canvas=tk.Canvas(windows)
#___________________________________menu_____________________________________________
menubar = tk.Menu(windows)  
menubar.add_command(label="Welcome!") 
menubar.add_command(label="Quit!", command=quit) 
#___________________________________display menu_____________________________________________ 
windows.config(menu=menubar)
#___________________________________background window_____________________________________________
windows_bg_image = tk.PhotoImage(file = "image/bg.png") 
windows_background=canvas.create_image(350,325,image=windows_bg_image)
#___________________________________Condition:_____________________________________________
NumberOfLive=0
FoundKey=False
IsWin=False
levels=1
#___________________________________stairs_____________________________________________
stair=tk.PhotoImage(file="image/stair.png")
stair1_grass=canvas.create_image(350,570,image=stair)
stair2_grass=canvas.create_image(350,480,image=stair)
stair3_grass=canvas.create_image(350,390,image=stair)
stair4_grass=canvas.create_image(350,300,image=stair)
stair5_grass=canvas.create_image(350,210,image=stair)
#___________________________________Label_____________________________________________
canvas.create_text(70,25,text="PYTHON VC1",font=("Arial",15),fill="white")
#_________________________________heart______________________________________:
heart_image=tk.PhotoImage(file="image/heart.png")
heart1=canvas.create_image(585,25,image=heart_image)
heart2=canvas.create_image(630,25,image=heart_image)
heart3=canvas.create_image(675,25,image=heart_image)
#___________________________________Target_____________________________________________
Target=tk.PhotoImage(file="image/target.png")
door=canvas.create_image(670,615, image=Target)
#___________________________________key_____________________________________________
key_image=tk.PhotoImage(file="image/key.png")
key=canvas.create_image(350,165, image=key_image)
#___________________________________player _____________________________________________
player_image=tk.PhotoImage(file="image/me.png")
player=canvas.create_image(30, 615, image=player_image)
#________________________________________ bullet_____________________________________________
bullet_image=tk.PhotoImage(file="image/bullet.png")
bullet=canvas.create_image(-25,620,image=bullet_image)
#___________________________________monster speed& bullet_____________________________________________
monster_speed=80
bullet_speed=11
#____________________________________monster image____________________________________________________
monster1_image=tk.PhotoImage(file="image/monster1.png")
monster1=canvas.create_image(650, 525, image=monster1_image)
monster2_image=tk.PhotoImage(file="image/monster2.png")
monster2=canvas.create_image(400,435,image=monster2_image)
monster3_image=tk.PhotoImage(file="image/monster3.png")
monster3=canvas.create_image(200, 345, image=monster3_image)
monster4_image=tk.PhotoImage(file="image/monster4.png")
monster4=canvas.create_image(600, 255, image=monster4_image)
monster5_image=tk.PhotoImage(file="image/monster5.png")
monster5=canvas.create_image(450, 165, image=monster5_image)
bird_image=tk.PhotoImage(file="image/bird_monster.png")
bird_monster=canvas.create_image(550, 85, image=bird_image)
monsters=[[monster1,10,0],[monster2,10,0],[monster3,10,0],[monster4,10,0],[monster5,10,0],[bird_monster,10,0]]
#___________________________________text_image_____________________________________________
Win_banner=canvas.create_text(-50,-50,text="You win!",font=("Arial",40))
Lose_banner=canvas.create_text(-50,-50,text="Game Over",font=("",40))

#___________________________________Move monsters_____________________________________________
def move_monsters():
    global monsters,NumberOfLive,IsWin,levels,Lose_banner,monster_speed
    if NumberOfLive<3 and IsWin==False:
        for n in range(len(monsters)):
            position=canvas.coords(monsters[n][0])
            monsterX = position[0]
            if monsterX<=50 or monsterX>=650:
                monsters[n][1] = -monsters[n][1]
            canvas.move(monsters[n][0],monsters[n][1],monsters[n][2])
            if (canvas.coords(monsters[n][0])[0]-50==canvas.coords(player)[0]+30 and canvas.coords(monsters[n][0])[1]==canvas.coords(player)[1]):
                canvas.moveto(player,0,580)
                NumberOfLive+=1
                sd_touched()
                count_number_ofLife()
            if (canvas.coords(monsters[n][0])[0]+50==canvas.coords(player)[0]-30 and canvas.coords(monsters[n][0])[1]==canvas.coords(player)[1]):
                canvas.moveto(player,0,580)
                NumberOfLive+=1
                sd_touched()
                count_number_ofLife()
            if canvas.coords(monsters[n][0])[1]==canvas.coords(player)[1] and canvas.coords(player)[0]-30>=canvas.coords(monsters[n][0])[0]-50 and canvas.coords(monsters[n][0])[0]+50>=canvas.coords(player)[0]+30:
                canvas.moveto(player,0,580)
                NumberOfLive+=1
                sd_touched()
                count_number_ofLife()
        canvas.after(monster_speed,move_monsters)
    if NumberOfLive==3:
        canvas.moveto(Lose_banner,220,325)
        sd_game_over()
        canvas.after(4000,restart_game)
move_monsters()
#___________________________________Move player_____________________________________________
deltaX=0
deltaY=0
def move(event):
    global deltaX,deltaY,FoundKey,key,IsWin,NumberOfLive,Win_banner
    if NumberOfLive<3 and IsWin==False:
        if event.char == 'd'and (canvas.coords(player)[0]<670):#go right
            deltaX = 10
            deltaY = 0
        elif event.char == 'a' and canvas.coords(player)[0]>30:#go left
            deltaX = -10
            deltaY = 0
        elif event.char=="w" and canvas.coords(player)[1]>165:#go up
            deltaX = 0
            deltaY = -90
        elif event.char=="s" and canvas.coords(player)[1]<615:#go down
            deltaX = 0
            deltaY = 90
        else:
            deltaY=0
            deltaX=0
        canvas.move(player,deltaX,deltaY)
        sd_up_down_left_right()
        if FoundKey==False:
                if canvas.coords(player)[0]==canvas.coords(key)[0] and canvas.coords(player)[1]==canvas.coords(key)[1]:
                    FoundKey=True
                    canvas.moveto(key,-50,-50)
                    shoot_player()
        if canvas.coords(player)[0]==canvas.coords(door)[0] and canvas.coords(player)[1]==canvas.coords(door)[1] and FoundKey:
                IsWin=True
                canvas.moveto(Win_banner,240,325)
                canvas.after(7000,restart_game)
                sd_win()
windows.bind("<Key>",move)
#___________________________________Shoot player_____________________________________________
def shoot_player():
    global bullet,bird_monster,NumberOfLive,IsWin,bullet_speed
    Shooted_player=False
    if NumberOfLive<3 and IsWin==False:
        if (canvas.coords(player)[1]-30==canvas.coords(bullet)[1]+10) and (canvas.coords(player)[0]-30==canvas.coords(bullet)[0]+10):
            Shooted_player=True
        elif (canvas.coords(player)[1]-30==canvas.coords(bullet)[1]+10) and (canvas.coords(bullet)[0]-10==canvas.coords(player)[0]+30):
            Shooted_player=True
        elif (canvas.coords(player)[1]-30==canvas.coords(bullet)[1]+10) and (canvas.coords(bullet)[0]-10>=canvas.coords(player)[0]-30) and (canvas.coords(bullet)[0]+10<=canvas.coords(player)[0]+30):
            Shooted_player=True
        elif (canvas.coords(player)[1]-30==canvas.coords(bullet)[1]+10) and ((canvas.coords(bullet)[0]==canvas.coords(player)[0]-30) or (canvas.coords(bullet)[0]==canvas.coords(player)[0]+30)):
            Shooted_player=True
        if Shooted_player:
            NumberOfLive+=1
            count_number_ofLife()
            sd_touched()
            canvas.moveto(player,0,580)
        canvas.move(bullet,0,5)
        canvas.after(bullet_speed,shoot_player)
        if canvas.coords(bullet)[1]>660:
                bullet=canvas.create_image(canvas.coords(bird_monster)[0],canvas.coords(bird_monster)[1],image=bullet_image)
#___________________________________Lose life_____________________________________________
def count_number_ofLife():
    global NumberOfLive
    if NumberOfLive==1:
        canvas.moveto(heart1,-50,-50)
    elif NumberOfLive==2:
        canvas.moveto(heart2,-50,-50)
    elif NumberOfLive==3:
        canvas.moveto(heart3,-50,-50)
#___________________________________Sound Library_____________________________________________
#___________________________________Sound start game_____________________________________________
winsound.PlaySound("sound/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
#___________________________________Sound actions_____________________________________________
def sd_up_down_left_right():
    winsound.PlaySound("sound/up_down.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
def sd_touched():
    winsound.PlaySound("sound/touched.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
def sd_game_over():
    winsound.PlaySound("sound/gameover.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
def sd_win():
    winsound.PlaySound("sound/winsound.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
#_________________________________________Restart game_________________________________________#
listOfDoorPosition=[[320,130],[320,220],[320,310]]
listOfkeyPosition=[[0,130],[600,130],[0,220],[600,220]]
def restart_game():
    global levels,NumberOfLive,IsWin,FoundKey,monster_speed,bullet_speed,listOfkeyPosition,listOfDoorPosition
    if levels==3 and IsWin:
            end_game()
    elif IsWin:
            doorPosition=random.choice(listOfDoorPosition)
            keyPosition=random.choice(listOfkeyPosition)
            winsound.PlaySound("sound/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
            canvas.moveto(Win_banner,-50,-50)
            canvas.moveto(door,doorPosition[0],doorPosition[1])
            canvas.moveto(key,keyPosition[0],keyPosition[1])
            canvas.moveto(player,0,580)
            levels+=1
            NumberOfLive=0
            IsWin=False
            FoundKey=False
            canvas.moveto(bullet,0,660)
            monster_speed-=20
            bullet_speed-=2
            canvas.moveto(heart1,565,5)
            canvas.moveto(heart2,610,5)
            canvas.moveto(heart3,655,5)
            move_monsters()
    elif NumberOfLive==3:
            winsound.PlaySound("sound/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
            canvas.moveto(Lose_banner,-50,-50)
            levels=1
            NumberOfLive=0
            bullet_speed=11
            monster_speed=80
            canvas.moveto(heart1,565,5)
            canvas.moveto(heart2,610,5)
            canvas.moveto(heart3,655,5)
            canvas.moveto(bullet,0,660)
            canvas.moveto(door,640,580)
            canvas.moveto(key,300,130)
            move_monsters()
            IsWin=False
            FoundKey=False
def end_game():
    winsound.PlaySound("sound/endgame.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
    canvas.delete("all")
    canvas.create_text(350,325,text="Congratulation",font=("Arial",65))
#_______________________________________________________________________________________________#
#__________________________________display all________________________________________________#
canvas.pack(expand=True,fill="both")
windows.resizable(False,False)
windows.mainloop()
