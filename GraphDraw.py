import matplotlib.pyplot as plt
import sys
import tkinter as tk
import functionals as moj


if __name__ == '__main__':
    okno = tk.Tk()
    okno.title("GraphDraw")
    okno.geometry("800x600")
    
    input = tk.Entry(okno, width=40) 
    r1 = tk.Entry(okno, width=10) #X1 interval
    r1.insert(0, 1)
    r2 = tk.Entry(okno, width=10) #X2 interval
    r2.insert(0, 10)
    y1 = tk.Entry(okno, width=10) #Y1 interval
    y1.insert(0, -10)
    y2 = tk.Entry(okno, width=10) #Y2 interval   
    y2.insert(0, 10)    
    name1 = tk.Entry(okno, width=10) #graph title
    name1.insert(0, "Graph")
    name2 = tk.Entry(okno, width=10) #OX label
    name2.insert(0, "X Axis")
    name3 = tk.Entry(okno, width=10) #OY label
    name3.insert(0, 'Y Axis')

def wylacz():
    """Shuts down the program"""
    sys.exit(0)
    
def input_przycisk(znak):
    input.insert(0,znak)

def okienko(input, r1, r2, y1, y2, name1, name2, name3):
    """Defines position and size of window and buttons"""
    input.place(x=200, y=250)
    r1.place(x=530, y=100)
    r2.place(x=530, y=125)
    y1.place(x=530, y=150)
    y2.place(x=530, y=175)
    name1.place(x=200, y=150)
    name2.place(x=200, y=100) 
    name3.place(x=200, y=125)
    #
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
    napis7 = tk.Label(text="Available special functions: sin(x), cos(x), tan(x), exp(x), log(x)")
    napis7.place(x=20, y=50)
    napis8 = tk.Label(text="Lower limit ")
    napis8.place(x=350, y=150)
    napis9 = tk.Label(text="Upper limit ")
    napis9.place(x=350, y=175)
    #
    przycisk1 = tk.Button(okno, text="Draw graph", command = lambda: moj.ReadAndDraw(input.get(), r1.get(), r2.get(), y1.get(), y2.get(), name1.get(), name2.get(), name3.get()))
    przycisk1.place(x = 550, y = 250)
    przycisk2 = tk.Button(okno, text="Exit", command = wylacz)
    przycisk2.place(x = 550, y = 300)
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
    log = tk.Button(okno, text="log(x)", width=4,height=1, command=lambda: input_przycisk("log(x)"))
    log.place(x = 300, y = 330)
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

okienko(input, r1, r2, y1, y2, name1, name2, name3)
