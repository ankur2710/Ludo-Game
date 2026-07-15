
from tkinter import *                                                                         #Tkinter is used as the GUI.
import random
root= Tk()

#root.geometry('1000x1000')

#base= PhotoImage(file= "ludo board.gif")

#Label(root, image=base).pack(side="left")

canvas = Canvas(width = 1000, height = 800, bg = 'yellow')
root.resizable(width=False, height=False)

canvas.pack(expand = YES, fill = BOTH)

gif1 = PhotoImage(file = 'ludo board.gif')
canvas.create_image(50, 10, image = gif1, anchor = NW)


g3 = canvas.create_oval(50,290,80,320, outline="green", fill="green", tags="oval")
        #40, 380, 90, 430
g4 = canvas.create_oval(50,390,80,420, outline="green", fill="green", tags="oval")

drag_data = {"x": 0, "y": 0, "item": None}
init_data = {"x": 0, "y": 0, "item": None}
final_coordinate = [0, 0]

def OnTokenButtonPress(event):
    # record the item and its location
    drag_data["item"] = canvas.find_closest(event.x, event.y)[0]
    drag_data["x"] = event.x
    drag_data["y"] = event.y

    init_data["item"] = drag_data["item"]  # defining new destination
    init_data["x"] = drag_data["x"]
    init_data["y"] = drag_data["y"]

    item_below = canvas.find_overlapping(event.x, event.y, event.x, event.y)[0]


