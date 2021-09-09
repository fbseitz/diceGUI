import tkinter as tk
import random
import matplotlib.pyplot as plt
import os

def rollresults(dicelist, dicetotal, dicetotaltext, dicerollstext):
    """Function to format text display of the results of the dice roll"""
    
    dicetotaltext['text'] = f"Total: {dicetotal}"

    dicerollstring = "Individual Rolls: "

    for x in range(len(dicelist)):
        addstring = f"{dicelist[x]} "
        dicerollstring += addstring
    
    dicerollstext['text'] = dicerollstring.rstrip('\t')

def graphresults(minresult, maxresult, resultdict):
    """Function to graph current results of dicerolls"""
    
    #Create list of current range of possible dice outcomes, 
    # and a list of actual number of rolls of each dice possible outcome that has occurred.
    possiblerange = []
    actualoutcomes = []
    maxrolled = 0

    for x in range(minresult, maxresult + 1):
        possiblerange.append(x)
        if x in resultdict.keys():
            actualoutcomes.append(resultdict[x])
            if resultdict[x] > maxrolled:
                maxrolled = resultdict[x]
        else:
            actualoutcomes.append(0)
    
    #Create a list up to highest number of any result rolled for use with Y ticks in graph.
    outcomerange = []
    for x in range(0, maxrolled + 1):
        outcomerange.append(x)
    
    #Create, format, and save figure.
    fig, ax = plt.subplots()
    bargraph = plt.bar(x=possiblerange, height=actualoutcomes, tick_label=possiblerange, color='gold')
    
    plt.yticks(outcomerange)
    ax.tick_params(axis='x', colors='gold')    
    ax.tick_params(axis='y', colors='gold')
    ax.spines['left'].set_color('gold')       
    ax.spines['bottom'].set_color('gold')    
    ax.set_facecolor('black')
    
    filename = os.path.dirname(__file__) + '//rollhistory'

    plt.savefig(fname=filename, facecolor='black')
    plt.close('all')

#Create function to roll the dice (this doubles as the "main" function, and incorporates the others)
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

    #Graph Results
    graphresults(minresult=minresult, maxresult=maxresult, resultdict=resultdict)

    #Reset Canvas
    