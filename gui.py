import tkinter as tk
from settings import *

global start
start = False

def game_start():
    root = tk.Tk()
    root.geometry("{}x{}".format(WIDTH,HEIGHT))
    startbutton = tk.Button(root, text="START", bg='gray', fg='black', bd='10', padx=str(100), pady=str(50))
    #p = startbutton.invoke()
    startbutton.grid(row=5, column=0,padx=230,pady=HEIGHT/2-100)
    #startbutton.pack()
    quitbutton = tk.Button(root, text="QUIT", bg='gray', fg='black', bd='10', padx=str(100), pady=str(50), command=root.destroy)
    quitbutton.grid(row=5, column=1, padx=0,pady=HEIGHT/2-100)
    #quitbutton.pack()
    root.mainloop()

def startgame(bool):
    if bool:
        return True
    else:
        return False