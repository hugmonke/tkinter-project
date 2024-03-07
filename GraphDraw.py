import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import math as m
import sys

okno = tk.Tk()
okno.title("GraphDraw")
okno.geometry("800x600")
def sprawdz(): 
    """Checks if given intervals are numbers"""
    czek = [r1.get(), r2.get(), y1.get(), y2.get()]
    for i in range(0,4):
        if czek[i].lstrip('-').isdigit() == False:
            print("Intervals must be numbers!\n")
            break
        else:
            rysuj()
            break
def rysuj():
    """Reads formulas and draws graphs"""
    plt.clf()
    wejscie = input.get()
    wejscie = wejscie.split(";") #Dzielimy wejście na listę list z odpowiednio podzielonymi wzorami
    for k in range(0,len(wejscie)):
        wzor = wejscie[k]
        wzor = wzor.replace('^', '**')
        wzor = list(wzor)
        j = 0
        log = 0
 
        for i in range(0,len(wzor)): #Dodaje przedroski m. (math.) by eval() automatycznie wykrywal funkcje
            if wzor[i][0] == 'l':
                wzor[i] = 'm.' + wzor[i]
                log = True
            if j <= i and (wzor[i] == 's' or wzor[i][0] == 'c' or wzor[i][0] == 't' or wzor[i][0] == 'e' or wzor[i][0] == 'p'): #poszukuje funkcyj matematycznych
                wzor[i] = 'm.' + wzor[i]
                j = i+3
         
        wzor = ''.join(wzor)
        dziala = False
        while (dziala == False):                                       #Sprawdzamy, czy podany zakres zgadza się z dziedziną funkcji
            rangeX1 = float(r1.get())
            rangeX2 = float(r2.get())
            rangeY1 = float(y1.get())
            rangeY2 = float(y2.get())
            if ((rangeX1 >= rangeX2) or (log == True and rangeX1 <= 0)):   #Jeśli nie, podaj poprawny zakres
                print("Bad range!\n")
                okienko()
            else:
                args = [*np.arange(rangeX1, rangeX2, 0.01)]               #Jeśli tak, to rysuj wykres
                try: 
                    [eval(wzor) for x in args]                              #Sprawdza, czy wpisany przez nas tekst jest funkcją matematyczną
                except:
                    raise ValueError("Not a math function!\n")
                func = [eval(wzor) for x in args]
                dziala = True
                plt.plot(args, func, label = str(wejscie[k]))
                plt.legend(loc="upper left")
                plt.ylim(rangeY1,rangeY2)
                plt.title(name2.get())
                plt.xlabel(name1.get())
                plt.ylabel(name3.get())
    plt.show()

        
            
def wylacz():
    """Shuts down the program"""
    sys.exit(0)
def czysc():
    """Clears the graph"""
    plt.clf()
    plt.show()
def input_przycisk(znak):
    input.insert(0,znak)
def okienko():
    """Defines position and size of window and buttons"""
    input.place(x=200, y=250)
    r1.place(x=530, y=100)
    r2.place(x=530, y=125)
    y1.place(x=530, y=150)
    y2.place(x=530, y=175)
    name1.place(x=200, y=150)
    name2.place(x=200, y=100) 
    name3.place(x=200, y=125)
    #############################################
    napis1 = tk.Label(text="Left limit: ")
    napis1.place(x=350, y=100)
    napis2 = tk.Label(text="Right limit: ")
    napis2.place(x=350, y=125)
    napis3 = tk.Label(text="Function formula: ")
    napis3.place(x=20, y=250)
    napis4 = tk.Label(text="X-label ")
    napis4.place(x=20, y=150)
    napis5 = tk.Label(text="Title ")
    napis5.place(x=20, y=100)
    napis6 = tk.Label(text="Y-label ")
    napis6.place(x=20, y=125)
    napis7 = tk.Label(text="Available special functions: sin(x), cos(x), tan(x), cot(x), exp(x), log(x,b), sqrt(x) ")
    napis7.place(x=20, y=50)
    napis8 = tk.Label(text="Lower limit ")
    napis8.place(x=350, y=150)
    napis9 = tk.Label(text="Upper limit ")
    napis9.place(x=350, y=175)
    #############################################
    przycisk1 = tk.Button(okno, text="Draw graph", command = lambda: sprawdz())
    przycisk1.place(x = 550, y = 250)
    przycisk2 = tk.Button(okno, text="Exit", command = wylacz)
    przycisk2.place(x = 550, y = 300)
    przycisk3 = tk.Button(okno, text="Clear", command = czysc)
    przycisk3.place(x = 550, y = 350)
    cyfra1 = tk.Button(okno, text="1", command=lambda: input_przycisk(1))
    cyfra1.place(x = 200, y = 300)
    cyfra2 = tk.Button(okno, text="2", command=lambda: input_przycisk(2))
    cyfra2.place(x = 220, y = 300)
    cyfra3 = tk.Button(okno, text="3", command=lambda: input_przycisk(3))
    cyfra3.place(x = 240, y = 300)
    cyfra4 = tk.Button(okno, text="4", command=lambda: input_przycisk(4))
    cyfra4.place(x = 200, y = 330)
    cyfra5 = tk.Button(okno, text="5", command=lambda: input_przycisk(5))
    cyfra5.place(x = 220, y = 330)
    cyfra6 = tk.Button(okno, text="6", command=lambda: input_przycisk(6))
    cyfra6.place(x = 240, y = 330)
    cyfra7 = tk.Button(okno, text="7", command=lambda: input_przycisk(7))
    cyfra7.place(x = 200, y = 360)
    cyfra8 = tk.Button(okno, text="8", command=lambda: input_przycisk(8))
    cyfra8.place(x = 220, y = 360)
    cyfra9 = tk.Button(okno, text="9", command=lambda: input_przycisk(9))
    cyfra9.place(x = 240, y = 360)
    cyfra0 = tk.Button(okno, text="0", command=lambda: input_przycisk(0))
    cyfra0.place(x = 220, y = 390)
    sinus = tk.Button(okno, text="sin(x)", width=4,height=1, command=lambda: input_przycisk("sin(x)"))
    sinus.place(x = 260, y = 300)
    cosinus = tk.Button(okno, text="cos(x)", width=4,height=1, command=lambda: input_przycisk("cos(x)"))
    cosinus.place(x = 260, y = 330)
    tg = tk.Button(okno, text="tan(x)", width=4,height=1, command=lambda: input_przycisk("tan(x)"))
    tg.place(x = 300, y = 300)
    ctg = tk.Button(okno, text="cot(x)", width=4,height=1, command=lambda: input_przycisk("cot(x)"))
    ctg.place(x = 300, y = 330)
    liczb_pi = tk.Button(okno, text="\u03C0", width=1,height=1, command=lambda: input_przycisk("pi"))
    liczb_pi.place(x = 200, y = 390)
    liczb_e = tk.Button(okno, text="e", width=1,height=1, command=lambda: input_przycisk("e"))
    liczb_e.place(x = 240, y = 390)
    plus = tk.Button(okno, text="+", width=1,height=1, command=lambda: input_przycisk("+"))
    plus.place(x = 260, y = 360)
    minus = tk.Button(okno, text="-", width=1,height=1, command=lambda: input_przycisk("-"))
    minus.place(x = 280, y = 360)
    razy = tk.Button(okno, text="*", width=1,height=1, command=lambda: input_przycisk("*"))
    razy.place(x = 300, y = 360)
    dziel = tk.Button(okno, text="/", width=1,height=1, command=lambda: input_przycisk("/"))
    dziel.place(x = 320, y = 360)
    okno.mainloop()


input = tk.Entry(okno, width=40) #wejscie funkcyj
r1 = tk.Entry(okno, width=10) #zakresX1
r2 = tk.Entry(okno, width=10) #zakresX2
y1 = tk.Entry(okno, width=10) #zakresY1
y2 = tk.Entry(okno, width=10) #zakresY2        
name1 = tk.Entry(okno, width=10) #nazwa wykresu
name2 = tk.Entry(okno, width=10) #nazwa osi OX
name3 = tk.Entry(okno, width=10) #nazwa osi OY
okienko()
