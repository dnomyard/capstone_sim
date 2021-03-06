#!/usr/bin/python
import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, max_x, max_y, master=None):
        tk.Frame.__init__(self, master)
        self.max_x = max_x
        self.max_y = max_y
        self.grid()
        self.createWidgets()
        

    def createWidgets(self):
        self.canvas = tk.Canvas(self, width = self.max_x, height = self.max_y)
        self.canvas.pack()
        self.canvas.grid()
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()


    def addBall(self):
        self.x0 = 10		# initial left-most edge of ball
        self.y0 = 50		# initial top-most edge of ball
        self.x1 = 60		# inital right-most edge of ball
        self.y1 = 100	# you've probably got the idea by now.
        self.dx = 2
        self.dy = 3
        # create ball:
        which = self.canvas.create_oval(self.x0,self.y0,self.x1,self.y1,fill="blue", tag='blueBall')        

    def moveBall(self):
        while True:
            self.canvas.move('blueBall', self.dx, self.dy)
            self.canvas.after(20)
            self.canvas.update()
            # the next 4 if statements check if the ball hits a wall: if it hits
            # a floor/ceiling its y-velocity reverses and it if hits a left/right 
            # wall its x-velocity reverses
            if self.x1 >= self.max_x:
                self.dx = -2
            if self.y1 >= self.max_y:
                self.dy = -3
            if self.y0 < 0:
                self.dy = 3
            if self.x0 < 0:
                self.dx = 2
            self.x0 += self.dx
            self.x1 += self.dx
            self.y0 += self.dy
            self.y1 += self.dy 

app = Application(400, 300)
app.addBall()
app.moveBall()
app.master.title('Sample application')
app.mainloop()

