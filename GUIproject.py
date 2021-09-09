import tkinter as tk
from guiprojectfunctions import whaleback
import os
import sys

#Initialize overall canvas, and add background image
WIDTH = 1200
HEIGHT = 750

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
dicenumframe.place(relheight=0.1, relwidth=0.20, relx=0.05, rely=0.05)

dicenum = tk.StringVar(root, '2')
get_dicenum = tk.Entry(dicenumframe, textvariable=dicenum, font=12, justify='center', bg='black', fg='gold')
get_dicenum.place(relheight=0.5, relwidth=1, rely=0.5)

dicenumlabel = tk.Label(dicenumframe, bg='gold', fg='black', text='Number of Dice to Roll', font=12)
dicenumlabel.place(relheight=0.5, relwidth=1, rely=0)

#Create second upper frame for entry of side to dice, with entry and label
dicesideframe = tk.Frame(canvas)
dicesideframe.place(relheight=0.1, relwidth=0.2, relx=0.75, rely=0.05)

dicesides = tk.StringVar(root, '6')
get_sidenum = tk.Entry(dicesideframe, textvariable=dicesides, font=12, justify='center', bg='black', fg='gold')
get_sidenum.place(relheight=0.5, rely=0.5, relwidth=1)

dicesidelabel = tk.Label(dicesideframe, bg='gold', fg='black', text='Number of sides of dice', font=12)
dicesidelabel.place(relheight=0.5, rely=0, relwidth=1)

#Create button to roll the dice!
resultdict = {}
rollthedice = tk.Button(canvas, 
                        text='Roll the Dice!', 
                        font=40, 
                        command=lambda: [whaleback(dicenum=get_dicenum, 
                                                dicesides=get_sidenum, 
                                                resultdict=resultdict, 
                                                dicetotaltext=dicetotaltext, 
                                                dicerollstext=dicerollstext), 
                                        addpic(graphcanvas=graphcanvas),
                                        ],
                        bg='gold', 
                        fg='black')
rollthedice.place(relheight=0.1, relwidth=0.4, relx=0.3, rely=0.05)

#Create a frame for the dice result display, with labels for total and individual rolls
diceresultframe = tk.Frame(canvas)
diceresultframe.place(relheight=0.15, relwidth=0.5, relx=0.25, rely=0.2)

dicetotaltext = tk.Label(diceresultframe, bg='black', fg='gold', font=('Times','24','bold'), text='Total: ')
dicetotaltext.place(relheight=0.5, relwidth=1, relx=0, rely=0)

dicerollstext= tk.Label(diceresultframe, bg='gold', fg='black', font=('Times', '16'), text='Individual Rolls: ')
dicerollstext.place(relheight=0.5, relwidth=1, relx=0,rely=0.5)

#Create a frame for a graph of roll history, and canvas used to display the chart
graphframe = tk.Frame(canvas, bg='black')
graphframe.place(relheight=0.55, relwidth=0.5, relx=0.25, rely=0.4)

graphcanvas = tk.Canvas(graphframe, bg='gold')
graphcanvas.place(relheight=1, relwidth=1)

#Set up storage of chart picture and function to asssign to the canvas
chartofrolls = None

def addpic(graphcanvas):
    global chartofrolls
    roll_path = '\\rollhistory.png'
    def graph_resource_path(roll_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        graph_path = os.path.dirname(__file__) + '\\rollhistory.png'
        return graph_path
    rollchart = graph_resource_path(roll_path)
    chartofrolls = tk.PhotoImage(file=rollchart)
    graphcanvas.create_image(300, 200, image=chartofrolls)

#Closing procedure
root.protocol("WM_DELETE_WINDOW", root.quit)
root.mainloop()
root.destroy()