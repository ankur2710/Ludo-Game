from tkinter import *  # Tkinter is used as the GUI.
from tkinter import messagebox
import sys
import os
import random
import tkinter.messagebox
root = Tk()
root.resizable(width=False, height=False)  # The window size of the game.
root.geometry('1000x750')
root.configure(background='green')
root.title("Checkers")
logo = PhotoImage(file="whitebox.gif")      # Loading all the image files that are required in the game.
logo2 = PhotoImage(file="red side.gif")     # Loading all the image files that are required in the game.
logo3 = PhotoImage(file="red.gif")          # Loading all the image files that are required in the game.
logo4 = PhotoImage(file="blue side.gif")
logo5 = PhotoImage(file="green side.gif")
logo6 = PhotoImage(file="yellow side.gif")
logo7 = PhotoImage(file="center.gif")
logoxx = PhotoImage(file="test.gif")
logog = PhotoImage(file="greenbox.gif")
logogs = PhotoImage(file="greenstop.gif")
logoy = PhotoImage(file="yellowbox.gif")
logoys = PhotoImage(file="yellowstop.gif")
logob = PhotoImage(file="bluebox.gif")
logobs = PhotoImage(file="bluestop.gif")
logor = PhotoImage(file="redbox.gif")
logors = PhotoImage(file="redstop.gif")
logoh = PhotoImage(file="head.gif")
logot = PhotoImage(file="tail.gif")
logoh1 = PhotoImage(file="head1.gif")
logot1 = PhotoImage(file="tail1.gif")
logoh2 = PhotoImage(file="head2.gif")
logot2 = PhotoImage(file="tail2.gif")
logoh3 = PhotoImage(file="head3.gif")
logot3 = PhotoImage(file="tail3.gif")
logoab= PhotoImage(file="blue.gif")
logoay= PhotoImage(file="yellow.gif")
logoag= PhotoImage(file="green.gif")
Label(image=logo2, width=298, height=298).place(x=-1, y=-1)               #setting up board images
Label(image=logo4, width=300, height=300).place(x=(-2), y=(448))
Label(image=logo5, width=296, height=296).place(x=(450), y=(0))
Label(image=logo6, width=294, height=294).place(x=(450), y=(450))
Label(image=logo7, width=150, height=150).place(x=(298), y=(298))
c = 0                                #initializing variable and flags that are to be used in the game
lx = 0
bb =0
nc = 0
rollc = 0
rolls = []
RED = True
BLUE = False
GREEN = False
YELLOW = False
TURN = True
REDKILL = False
BLUEKILL = False
GREENKILL = False
YELLOWKILL = False

def board():                            #Drawing the board, piece by piece.

                                        #Splash Screen.
  tkinter.messagebox.showinfo(title=None, message="TO START GAME PRESS OKAY & TO EXIT PRESS CROSS UP IN THE WINDOW")
    v = 0
    z = 0
  while (v != 300):           #Drawing White boxes
        z = 0
        while (z != 150):
            Label(image=logo, width=46, height=46).place(x=(300 + z), y=(0 + v))
            z = z + 50
        v = v + 50

    z = 0
    v = 0
    while (v != 300):          #Drawing White boxes
        z = 0
        while (z != 150):
            Label(image=logo, width=46, height=46).place(x=(0 + v), y=(300 + z))
            z = z + 50
        v = v + 50
    #####################

    v = 0
    z = 0

    while (v != 300):            #Drawing White boxes
        z = 0
        while (z != 150):
            Label(image=logo, width=46, height=46).place(x=(300 + z), y=(450 + v))
            z = z + 50
        v = v + 50

    z = 0
    v = 0
    while (v != 300):         #Drawing White boxes
        z = 0
        while (z != 150):
            Label(image=logo, width=46, height=46).place(x=(450 + v), y=(300 + z))
            z = z + 50
        v = v + 50

    v = 0
    while (v != 250):     #Drawing Green boxes
        Label(image=logog, width=46, height=46).place(x=(350), y=(50 + v))
        v = v + 50

    Label(image=logog, width=46, height=46).place(x=(300), y=(100))
    Label(image=logogs, width=46, height=46).place(x=(400), y=(50))

    v = 0
    while (v != 250):     #Drawing Yellow boxes
        Label(image=logoy, width=46, height=46).place(x=(450 + v), y=(350))
        v = v + 50

    Label(image=logoy, width=46, height=46).place(x=(600), y=(300))
    Label(image=logoys, width=46, height=46).place(x=(650), y=(400))

    v = 0
    while (v != 250):    #Drawing Red Boxes
        Label(image=logor, width=46, height=46).place(x=(50 + v), y=(350))
        v = v + 50

    Label(image=logor, width=46, height=46).place(x=(100), y=(400))
    Label(image=logors, width=46, height=46).place(x=(50), y=(300))

    v = 0
    while (v != 250):    #Drawing Blue Boxes
        Label(image=logob, width=46, height=46).place(x=(350), y=(450 + v))
        v = v + 50

    Label(image=logobs, width=46, height=46).place(x=(300), y=(650))
    Label(image=logob, width=46, height=46).place(x=(400), y=(600))

    Label(image=logoh, width=46, height=46).place(x=250, y=400)        #Drawing arrows
    Label(image=logot, width=46, height=46).place(x=300, y=450)
    Label(image=logoh1, width=46, height=46).place(x=400, y=450)
    Label(image=logot1, width=46, height=46).place(x=450, y=400)
    Label(image=logoh2, width=46, height=46).place(x=450, y=300)
    Label(image=logot2, width=46, height=46).place(x=400, y=250)
    Label(image=logoh3, width=46, height=46).place(x=300, y=250)
    Label(image=logot3, width=46, height=46).place(x=250, y=300)

class YBox:                               #Class of yellow box
    rap = None

    def __init__(self, num=-1, x=0, y=0, x0=0, y0=0, double=False, ):
        self.num = num                #no of gamepiece acc to box
        self.x = x                    #initial and final co-ordinates of the boxes
        self.y = y
        self.x0 = x0
        self.y0 = y0
        self.rap = Label(image=logoay, width=20, height=20)        #image of game piece.
        self.double = double                                       #if one game piece on top of another.

    def swap(self):                     #Swaps the position of gamepiece according to the number on dice.
        self.rap.place(x=self.x0 + 13, y=self.y0 + 14)

class GBox:                             #Class of green box
    rap = None

    def __init__(self, num=-1, x=0, y=0, x0=0, y0=0, double=False, ):
        self.num = num
        self.x = x
        self.y = y
        self.x0 = x0
        self.y0 = y0
        self.rap = Label(image=logoag, width=20, height=20)
        self.double = double

    def swap(self):
        self.rap.place(x=self.x0 + 13, y=self.y0 + 14)

class BBox:                           #Class of Blue box
    rap = None

    def __init__(self, num=-1, x=0, y=0, x0=0, y0=0, double=False, ):
        self.num = num
        self.x = x
        self.y = y
        self.x0 = x0
        self.y0 = y0
        self.rap = Label(image=logoab, width=20, height=20)
        self.double = double

    def swap(self):
        self.rap.place(x=self.x0 + 13, y=self.y0 + 14)

class Box:                           #class of red box
    rap = None

    def __init__(self, num=-1, x=0, y=0, x0=0, y0=0, double=False, ):
        self.num = num
        self.x = x
        self.y = y
        self.x0 = x0
        self.y0 = y0
        self.rap = Label(image=logo3, width=20, height=20)
        self.double = double

    def swap(self):
        self.rap.place(x=self.x0 + 13, y=self.y0 + 14)


