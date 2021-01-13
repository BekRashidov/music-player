#imported modules
import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

#creating application window
musicplayer = tkr.Tk()

#setting up title
musicplayer.title("Music Player(Personal)")

#Giving the dimension
musicplayer.geometry("450x350")

directory = askdirectory()
os.chdir(directory)
songList = os.listdir()

playlist = tkr.Listbox(musicplayer, font = "Cambria 14 bold", bg = "cyan2", selectmode=tkr.SINGLE)

for item in songList:
    pos=0
    playlist.insert(pos, item)
    pos = pos+1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def ExitMusicPlayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

#Creating Buttons
Button_play = tkr.Button(musicplayer, height=3, width=5, text="Play Music", font="Cambria 14 bold", command=play, bg="lime green", fg="black")
Button_stop = tkr.Button(musicplayer, height=3, width=5, text="Stop Music", font="Cambria 14 bold", command=ExitMusicPlayer, bg="red", fg="black")
Button_pause = tkr.Button(musicplayer, height=3, width=5, text="Pause Music", font="Cambria 14 bold", command=pause, bg="yellow", fg="black")
Button_resume = tkr.Button(musicplayer, height=3, width=5, text="Resume Music", font="Cambria 14 bold", command=resume, bg="yellow", fg="black")

Button_play.pack(fill="x")
Button_stop.pack(fill="x")
Button_pause.pack(fill="x")
Button_resume.pack(fill="x")

playlist.pack(fill="both", expand="yes")

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font="Cambria 12 bold", textvariable=var)
songtitle.pack()
musicplayer.mainloop()