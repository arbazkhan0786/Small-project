import pygame
import tkinter
from tkinter.filedialog import askdirectory
import os

player = tkinter.Tk()
player.title("Music playe")
player.geometry("310x325")

vars = tkinter.StringVar()
vars.set ("Select the song to play")

os.chdir(askdirectory())
songlist = os.listdir()

player = tkinter.Listbox(player,font="Helvetical 12 bold" ,width=28,bg="black",fg="white",selectmode=tkinter.SINGLE)

for item in songlist:
    player.insert(0,item)

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playing.get(tkinter.ACTIVE))
    name = playing.get(tkinter.ACTIVE)
    vars.set(f"{name[:16]}..." if len(name)>18 else name)
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause

def resume():
    pygame.mixer.music.unpause()

text = tkinter.Label(player,font="Helvetica",textvariable=vars).grid(row=0,columnspan=3)
playing.grid(columnspan=3)

playB = tkinter.Button(player,width=7,height=8)
pauseB = tkinter.Button(player,width=7,height=8)
resumeB = tkinter.Button(player,width=9,height=10)

player.mainloop()