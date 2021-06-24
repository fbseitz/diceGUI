import tkinter as tk
import random

#Create function to print dice roll result
def rollresults(dicelist, dicetotal, dicetotaltext, dicerollstext):
    """Function to format text display of the results of the dice roll"""
    
    dicetotaltext['text'] = f"Total: {dicetotal}"

    dicerollstring = "Individual Rolls: "

    for x in range(len(dicelist)):
        addstring = f"{dicelist[x]} "
        dicerollstring += addstring
    
    dicerollstext['text'] = dicerollstring.rstrip('\t')

def graphresults():
    """Function to graph current results of dicerolls"""    
    

#Create function to roll the dice!
def whaleback(dicenum, dicesides, resultdict, dicetotaltext, dicerollstext):
    """Function to calculate dice roll and log results"""
    dicetotal = 0
    dicelist = []

    #Test input of dice number and sides to ensure integers
    try:
        minresult = int(dicenum.get())
    except:
        dicetotaltext['text'] = "Error"
        dicerollstext['text'] = "Dice Number is not a number."
        return

    try:
        maxresult = minresult * int(dicesides.get())
    except:
        dicetotaltext['text'] = "Error"
        dicerollstext['text'] = "Dice Sides is not a number."

    #Roll each dice, calculating total and making a list of results
    for x in range(minresult):
        result = random.randint(1, int(dicesides.get()))
        dicetotal += result
        dicelist.append(result)
    
    #Log total in a dictionary to track history
    if dicetotal in resultdict.keys():
        resultdict[dicetotal] += 1
    else:
        resultdict[dicetotal] = 1
    
    #Format text representation of result to be displayed in the GUI
    rollresults(dicetotal=dicetotal, dicelist=dicelist, dicetotaltext=dicetotaltext, dicerollstext=dicerollstext)


#rolllist = []
#for x in range(minresult, maxresult+1):
#rolllist.append({x: resultdict.get(x)})
    