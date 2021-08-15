import tkinter as tk
from guiprojectfunctions import whaleback
import os
import sys

#Initialize overall canvas, and add background image
WIDTH = 700
HEIGHT = 600

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='black')
canvas.pack()

#Get path for image- needed to bundle into one executable. Then, set as PhotoImage for background.
relative_path = '\\dice_image.png'
def img_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = os.path.dirname(__file__) + '\\dice_image.png'
    return base_path
bgimage = img_resource_path(relative_path)

rolldice = tk.PhotoImage(file=bgimage)
canvas.create_image(350, 300, image=rolldice)

#Create upper frame for entry of number of dice to use, with entry and label
dicenumframe = tk.Frame(canvas)
dicenumframe.place(relheight=0.1, relwidth=0.35, relx=0.1, rely=0.2)

dicenum = tk.StringVar(root, '2')
get_dicenum = tk.Entry(dicenumframe, textvariable=dicenum, font=12, justify='center')
get_dicenum.place(relheight=0.5, relwidth=1, rely=0.5)

dicenumlabel = tk.Label(dicenumframe, bg='gold', fg='black', text='Number of Dice to Roll', font=12)
dicenumlabel.place(relheight=0.5, relwidth=1, rely=0)

#Create second upper frame for entry of side to dice, with entry and label
dicesideframe = tk.Frame(canvas)
dicesideframe.place(relheight=0.1, relwidth=0.35, relx=0.55, rely=0.2)

dicesides = tk.StringVar(root, '6')
get_sidenum = tk.Entry(dicesideframe, textvariable=dicesides, font=12, justify='center')
get_sidenum.place(relheight=0.5, rely=0.5, relwidth=1)

dicesidelabel = tk.Label(dicesideframe, bg='black', fg='gold', text='Number of sides of dice', font=12)
dicesidelabel.place(relheight=0.5, rely=0, relwidth=1)

#Create button to roll the dice!
resultdict = {}
rollthedice = tk.Button(canvas, text='Roll the Dice!', font=40, command=lambda: whaleback(dicenum=get_dicenum, dicesides=get_sidenum, resultdict=resultdict, dicetotaltext=dicetotaltext, dicerollstext=dicerollstext))
rollthedice.place(relheight=0.08, relwidth=0.4, relx=0.3, rely=0.35)

#Create a frame for the dice result display, with labels for total and individual rolls
diceresultframe = tk.Frame(canvas)
diceresultframe.place(relheight=0.2, relwidth=0.5, relx=0.25, rely=0.5)

dicetotaltext = tk.Label(diceresultframe, bg='black', fg='gold', font=('Times','24','bold'), text='Total: ')
dicetotaltext.place(relheight=0.5, relwidth=1, relx=0, rely=0)

dicerollstext= tk.Label(diceresultframe, bg='gold', fg='black', font=('Times', '16'), text='Individual Rolls: ')
dicerollstext.place(relheight=0.5, relwidth=1, relx=0,rely=0.5)

root.protocol("WM_DELETE_WINDOW", root.quit)
root.mainloop()
root.destroy()