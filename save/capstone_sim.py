#!/usr/bin/python
"""
Adapted from: http://hopper.unco.edu/course/CS101/S07/lab7.html
"""

#Displays a circle bouncing around the canvas window.
from Tkinter import *

class Ball:
    def __init__(self, color, tag, x0, y0, x1, y1, dx, dy):
        self.color = color
        self.tag = tag
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.dx = dx
        self.dy = cy



class Simulator(object):


    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        
        window = Tk()
        self.canvas = Canvas(window, width = self.max_x, height = self.max_y)
        self.canvas.pack()




    def main(self):

        x0 = 10		# initial left-most edge of ball
        y0 = 50		# initial top-most edge of ball
        x1 = 60		# inital right-most edge of ball
        y1 = 100	# you've probably got the idea by now.
        dx = 2
        dy = 3
        # create ball:
        which = self.canvas.create_oval(x0,y0,x1,y1,fill="blue", tag='blueBall')
        while True:
            self.canvas.move('blueBall', dx, dy)
            self.canvas.after(20)
            self.canvas.update()
            # the next 4 if statements check if the ball hits a wall: if it hits
            # a floor/ceiling its y-velocity reverses and it if hits a left/right 
            # wall its x-velocity reverses
            if x1 >= self.max_x:
                dx = -2
            if y1 >= self.max_y:
                dy = -3
            if y0 < 0:
                dy = 3
            if x0 < 0:
                dx = 2
            x0 += dx
            x1 += dx
            y0 += dy
            y1 += dy

        window.mainloop()

if __name__ == "__main__":
    sim = Simulator(800, 600)
    sim.main()
    
    

