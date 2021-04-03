import tkinter as tk
from settings import *

class menuSystem:
    
    def __init__(self):
        self.start = False
        self.root = 0

    def game_start(self):
        self.root = tk.Tk()
        self.root.geometry("{}x{}".format(WIDTH,HEIGHT))
        startbutton = tk.Button(self.root, text="START", bg='gray', fg='black', bd='10', padx=str(100), pady=str(50), command=self.startgame)
        startbutton.pack()
        startbutton.grid(row=0, column=0,padx=230,pady=HEIGHT/2-100)
        #startbutton.pack()
        quitbutton = tk.Button(self.root, text="QUIT", bg='gray', fg='black', bd='10', padx=str(100), pady=str(50), command=self.root.destroy)
        quitbutton.grid(row=0, column=1, padx=0,pady=HEIGHT/2-100)
        #quitbutton.pack()
        self.root.mainloop()

    def startgame(self):
        self.start = True
        self.root.destroy()
        if self.start == True:
            self.root.destroy()
            print('e')