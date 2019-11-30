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