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

