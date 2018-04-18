import os
import pygame
import tkinter
from mutagen.id3 import ID3
from tkinter.filedialog import askdirectory
from tkinter import Tk, RIGHT, LEFT, BOTH, RAISED

root = tkinter.Tk()
root.minsize(300, 300)

songList = []
realnames = []
v = tkinter.StringVar()
songlabel = tkinter.Label(root, textvariable=v, width=35)

index = 0

def play1(event):
        global index
        pygame.mixer.music.load(songList[index])
        pygame.mixer.music.play()
        updateLabel()
          
def ns1(event):
        global index
        index +=1
        pygame.mixer.music.load(songList[index])
        pygame.mixer.music.play()
        updateLabel()

def ps1(event):
        global index
        index -=1
        pygame.mixer.music.load(songList[index])
        pygame.mixer.music.play()
        updateLabel()

def stop1(event):
        pygame.mixer.music.stop()

def updateLabel():
        global index
        global realnames
        v.set(realnames[index])
        return realnames
        
def directorychooser():

        directory = askdirectory()
        os.chdir(directory)
        for files in os.listdir(directory):
                if files.endswith('mp3'):
                        realdir = os.path.realpath(files)
                        audio = ID3(realdir)
                        realnames.append(audio['TIT2'].text[0])
                        
                        songList.append(files)

directorychooser()
updateLabel()

label = tkinter.Label(root,text='Music Player', width=75)
label.pack()


listbox = tkinter.Listbox(root, width=55)
listbox.pack()

realnames.reverse()

for items in realnames:
        listbox.insert(0, items)

realnames.reverse()

playbtn = tkinter.Button(root, text = 'Play')
playbtn.pack(fill=BOTH)

nextbtn = tkinter.Button(root, text = 'Next')
nextbtn.pack(side=RIGHT, padx=5, pady=10)

prevbtn = tkinter.Button(root, text = 'Previous')
prevbtn.pack(side=LEFT, padx=5)

stopbtn = tkinter.Button(root, text = 'Stop')
stopbtn.pack(fill=BOTH)


pygame.mixer.init()
pygame.mixer.music.load(songList[0])
pygame.mixer.music.play()

nextbtn.bind('<Button-1>', ns1)
prevbtn.bind('<Button-1>', ps1)
stopbtn.bind('<Button-1>', stop1)
playbtn.bind('<Button-1>', play1)

songlabel.pack()

root.mainloop()
