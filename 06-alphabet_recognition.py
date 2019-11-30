from tkinter import *
import cv2
from PIL import Image, ImageDraw
import PIL

class Paint(object):

    DEFAULT_PEN_SIZE = 15
    DEFAULT_COLOR = 'black'
    white = (255,0,0)
    black = 0,0,0
    width = 200
    height = 200

    def __init__(self):
        self.root = Tk()

        self.c = Canvas(self.root, bg='black', width=200, height=200)
        self.c.grid(row=1, columnspan=5)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.color = self.DEFAULT_COLOR
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        self.image1 = PIL.Image.new("RGB", (self.width, self.height), self.black)
        self.draw = ImageDraw.Draw(self.image1)
        self.c.pack(expand=YES, fill=BOTH)

    def paint(self, event):
        paint_color = "white"
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.DEFAULT_PEN_SIZE, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.draw.line([self.old_x, self.old_y, event.x, event.y],
                           fill="white",width=self.DEFAULT_PEN_SIZE)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def save(self):
        filename = "image.png"
        self.image1.save(filename)
        im = cv2.imread(filename)

if __name__ == '__main__':
    p = Paint()
    p.save()
    
from keras.models import load_model

# load model
model = load_model('model.h5')

import numpy as np
from keras.preprocessing import image

test_image = image.load_img('image.png', target_size = (28,28))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = model.predict(test_image)

predicted_class_indices=np.argmax(result,axis=1)

labels = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 
          'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 
          'Z': 25}

labels = dict((v,k) for k,v in labels.items())
prediction = [labels[k] for k in predicted_class_indices]
print(prediction)

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
from tkinter.font import Font

root = Tk()
root.minsize(600,450)

from PIL import Image
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