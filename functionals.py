import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import math as m


def isIntervalNumber(r1, r2, y1, y2):
    """Checks if given intervals are numbers"""
    czek = [r1, r2, y1, y2]
    for i in range(0,4):
        if czek[i].lstrip('-').isdigit() == False:
            return False

    return True

def AddPrefix(wejscie):
    """Adds prefixes m. (math.) and looks for math functions"""
    for k in range(0,len(wejscie)):
            wzor = wejscie[k]
            wzor = wzor.replace('^', '**')
            wzor = list(wzor)
            j = 0
            isLogarytmPodany = False
            
            for i in range(0,len(wzor)):  
                if wzor[i][0] == 'l':
                    wzor[i] = 'm.' + wzor[i]
                    isLogarytmPodany = True
                if j <= i and (wzor[i] == 's' or wzor[i][0] == 'c' or wzor[i][0] == 't' or wzor[i][0] == 'e' or wzor[i][0] == 'p'):
                    wzor[i] = 'm.' + wzor[i]
                    j = i+3
            wzor = ''.join(wzor)
            
    return isLogarytmPodany, wzor

def isDomainCorrect(r1, r2, isLogGiven, wzor):
    """Checks if given interval is a correct function domain"""  
    rangeX1 = float(r1)
    rangeX2 = float(r2)
    if ((rangeX1 >= rangeX2) or (isLogGiven == True and rangeX1 <= 0)):
        return False
    else:
        return True

def CalculateInput(r1, r2, y1, y2, wzor):
    rangeX1 = float(r1)
    rangeX2 = float(r2)
    rangeY1 = float(y1)
    rangeY2 = float(y2)
    args = [*np.arange(rangeX1, rangeX2, 0.01)]           
    try: 
        [eval(wzor) for x in args]                       
    except:
        raise ValueError("Not a math function!\n")
    
    func = [eval(wzor) for x in args]

    return rangeY1, rangeY2, args, func

def ReadAndDraw(input, r1, r2, y1, y2, name1, name2, name3):
    """Reads formulas and draws graphs"""
    if isIntervalNumber(r1, r2, y1, y2):
        plt.clf()
        wejscie = input.split(";")
        isLogGiven, wzor = AddPrefix(wejscie)
        if isDomainCorrect(r1, r2, isLogGiven, wzor):
            rangeY1, rangeY2, args, func = CalculateInput(r1, r2, y1, y2, wzor)
        else:
            print("Bad range!\n")
            import GraphDraw
            GraphDraw.okienko(input, r1, r2, y1, y2, name1, name2, name3)
    else:
        print("Not a number!\n")
            
        plt.plot(args, func)
        #plt.legend(loc="upper left")
        plt.ylim(rangeY1,rangeY2)
        plt.title(name2)
        plt.xlabel(name1)
        plt.ylabel(name3)
        plt.show()
        

