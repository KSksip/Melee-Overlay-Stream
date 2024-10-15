import customtkinter
import os
import subprocess

customtkinter.set_appearance_mode("dark")


## JSON file reset

f = open("./data/info.json", "w")
f.write("{" + f"""
"p1points": 0,
"p2points": 0,
"p1name": "",
"p2name": "",    
"p1char": "Fox",
"p2char": "Fox",
"p1color": "Default",
"p2color": "Default",
"p1port": "Port 1",
"p2port": "Port 1",
"bo": "Best of 3",
"round": "Round"
""" + "}")
f.close()
##

colors = [
    "Blue",
    "Default",
    "Green",
    "Red"

]

BoX = [
    "Best of 3",
    "Best of 5"
]

charList = [
"Bowser",
"Captain Falcon",
"Donkey Kong",
"Dr. Mario",
"Falco",
"Fox",
"Ganondorf",
"Ice Climbers",
"Jigglypuff",
"Kirby",
"Luigi",
"Link",
"Mario",
"Marth",
"Mewtwo",
"Mr. Game & Watch",
"Ness",
"Peach",
"Pichu",
"Pikachu",
"Roy",
"Samus",
"Sheik",
"Yoshi",
"Young Link",
"Zelda"
]

portList = [
    "Port 1",
    "Port 2",
    "Port 3",
    "Port 4"
]


#funcs
    #update func
def updateOverlay():
    writeToJSON()

    #Tally funcs
player1Points = 0
player2Points = 0

def addPoints1():
    global player1Points
    player1Points += 1

    scoreboard.set(f"""{player1Points} - {player2Points}""")

def addPoints2():
    global player2Points
    player2Points += 1

    scoreboard.set(f"""{player1Points} - {player2Points}""")

def removePoints1():
    global player1Points
    player1Points -=1
    if player1Points < 0:
        player1Points = 0

    scoreboard.set(f"""{player1Points} - {player2Points}""")

def removePoints2():
    global player2Points
    player2Points -=1
    if player2Points < 0:
        player2Points = 0

    scoreboard.set(f"""{player1Points} - {player2Points}""")

def resetPoints():
    global player1Points
    global player2Points
    player1Points = 0
    player2Points = 0
    scoreboard.set(f"""{player1Points} - {player2Points}""")


    #reset overlay
def resetOverlay():

    resetPoints()
    p1n.set("")
    p1n.set("")
    p1Char.set("Fox")
    p2Char.set("Fox")
    p1Color.set("Default")
    p2Color.set("Default")
    portSelectDisplayP1.set(portList[0])
    portSelectDisplayP2.set(portList[0])
    nameOfRound.set("Round")
    bestOfX.set(BoX[0])


def writeToJSON():

    jsonInfo = "{" + f"""
    "p1points": {player1Points},
    "p2points": {player2Points},
    "p1name": "{p1n.get()}",
    "p2name": "{p2n.get()}",    
    "p1char": "{p1Char.get()}",
    "p2char": "{p2Char.get()}",
    "p1color": "{p1Color.get()}",
    "p2color": "{p2Color.get()}",
    "p1port": "{portSelectDisplayP1.get()}",
    "p2port": "{portSelectDisplayP2.get()}",
    "bo": "{bestOfX.get()}",
    "round": "{nameOfRound.get()}"
""" + "}"


    f = open("./data/info.json", "w")
    f.write(jsonInfo)
    f.close()

def findColors1(event):
    tmp = os.listdir(f"""./overlay/img/stock icons/{p1Char.get()}/""")
    colors1 = []
    for i in tmp:
        colors1.append(i.replace(".png", ""))

    ddMenuColorP1.configure(values=colors1)
    p1Color.set("Default")
    print(colors1)


def findColors2(event):
    tmp = os.listdir(f"""./overlay/img/stock icons/{p2Char.get()}/""")
    colors2 = []
    for i in tmp:
        colors2.append(i.replace(".png", ""))

    ddMenuColorP2.configure(values=colors2)
    p2Color.set("Default")
    print(colors2)



server = subprocess.Popen("./server", shell=True)

## window
root = customtkinter.CTk()

# root.iconbitmap('appIcon.ico')

root.title("SSBM stream interface")
root.resizable(False,False)

scoreboard = customtkinter.StringVar(root)
scoreboard.set(f"""{player1Points} - {player2Points}""")


pn1Display = customtkinter.StringVar(root)
pn2Display = customtkinter.StringVar(root)

customtkinter.CTkLabel(root, text="Player 1").grid(row=0, column=0, padx=20)
customtkinter.CTkLabel(root, text="Player 2").grid(row=0, column=6, padx=20)
customtkinter.CTkLabel(root, text="Score").grid(row=0, column=3)


p1n = customtkinter.StringVar(root)
p2n = customtkinter.StringVar(root)

player1NameEntry = customtkinter.CTkEntry(root, textvariable=p1n, placeholder_text="player 1 name").grid(row=1, column=0, pady=10)
player2NameEntry = customtkinter.CTkEntry(root, textvariable=p2n, placeholder_text="player 2 name").grid(row=1, column=6, pady=10)

customtkinter.CTkLabel(root, textvariable=scoreboard).grid(row=1, column=3)


p1Char = customtkinter.StringVar(root)
p2Char = customtkinter.StringVar(root)

p1Char.set("Fox")
p2Char.set("Fox")





ddMenuCharP1 = customtkinter.CTkOptionMenu(root, values=charList, variable=p1Char, command=findColors1).grid(column=0, row=3)
ddMenuCharP2 = customtkinter.CTkOptionMenu(root, values=charList, variable=p2Char, command=findColors2).grid(column=6, row=3)

p1Color = customtkinter.StringVar(root)
p2Color = customtkinter.StringVar(root)

p1Color.set("Default")
p2Color.set("Default")

ddMenuColorP1 = customtkinter.CTkOptionMenu(root, values=colors,  variable=p1Color)
ddMenuColorP2 = customtkinter.CTkOptionMenu(root, values=colors, variable=p2Color)

ddMenuColorP1.grid(column=0, row=4, pady=5, padx=5)
ddMenuColorP2.grid(column=6, row=4, pady=5, padx=5)

portSelectDisplayP1 = customtkinter.StringVar(root)
portSelectDisplayP2 = customtkinter.StringVar(root)

portSelectDisplayP1.set(portList[0])
portSelectDisplayP2.set(portList[0])

ddMenuPortP1 = customtkinter.CTkOptionMenu(root, variable=portSelectDisplayP1, values=portList).grid(column=0, row=5)
ddMenuPortP2 = customtkinter.CTkOptionMenu(root, variable=portSelectDisplayP2, values=portList).grid(column=6, row=5)

player1PointsAdd = customtkinter.CTkButton(root, text="+1", width=5, command=addPoints1).grid(column=2, row=1)
player2PointsAdd = customtkinter.CTkButton(root, text="+1", width=5, command=addPoints2).grid(column=4, row=1)

player1PointsRemove = customtkinter.CTkButton(root, text="-1", width=5, fg_color="red", command=removePoints1).grid(column=1, row=1, padx=5)
player2PointsRemove = customtkinter.CTkButton(root, text="-1", width=5, fg_color="red", command=removePoints2).grid(column=5, row=1, padx=5)

playerPointsReset = customtkinter.CTkButton(root, text="Reset Points", command=resetPoints).grid(column=3, row=3)

nameOfRound = customtkinter.StringVar(root)
nameOfRound.set("Round")

roundName = customtkinter.CTkEntry(root, textvariable=nameOfRound).grid(column=3, row=5)

bestOfX = customtkinter.StringVar(root)
bestOfX.set(BoX[0])

bestOf = customtkinter.CTkOptionMenu(root, variable=bestOfX, values=BoX).grid(column=3, row=4)

customtkinter.CTkButton(root, text="Reset Overlay", command=resetOverlay).grid(column=0, columnspan=3, row=12,pady=10)
customtkinter.CTkButton(root, text="Update Overlay", command=updateOverlay).grid(column=4, columnspan=3, row=12, pady=10)

root.mainloop()

server.kill()
server.terminate()