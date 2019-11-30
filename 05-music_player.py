prediction = 'a'

import pandas as pd
import random
from pygame import mixer
import os

song_list = pd.read_csv('songs.csv', encoding='latin-1')

def songList(prediction):
    songs = []
    for i in range(len(song_list['name'])):
        if prediction[0].lower() == song_list['name'][i][0].lower():
            songs.append(song_list['name'][i])
            song = np.random.choice(songs)
    song_name = song + ".mp3"
#    print(song_name)
    for root,dirs,files in os.walk("music"):
        for filename in files:
            if filename == song_name.lower():
                mixer.init()
                mixer.music.load('music/'+filename)
                mixer.music.play()
                return song           
            
song_name = songList(prediction)

details = []
for i in range(len(song_list['name'])):
    if song_list['name'][i] == song_name:
        details.append(song_list['name'][i])
        details.append(song_list['artists'][i])
        details.append(song_list['duration'][i])
        
SongName = "Song : "+details[0]
Artists = "Artists : "+details[1]
Duration = "Time : "+str(details[2])+" mins"

import pygame
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.minsize(600,450)

from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("logo.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 25)
draw.text((150, 50),SongName,(255,255,255),font=font)
draw.text((180, 300),Artists,(255,255,255),font=font)
draw.text((200, 335),Duration,(255,255,255),font=font)
img.save('music.jpg')

def stopsong(event):
    pygame.mixer.music.stop()
    
def pausesong(event):
    pygame.mixer.music.pause()

label = Label(root,text='SONG DETAILS')
label.pack()

canvas = Canvas(root, width = 550, height = 400)  
canvas.pack() 
img = ImageTk.PhotoImage(Image.open("music.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)


stopbutton = Button(root,text='■',height = 2, width = 10)
stopbutton.pack(side=BOTTOM)
stopbutton.bind("<Button-1>",stopsong)

root.mainloop()