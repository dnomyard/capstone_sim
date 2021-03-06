#!/usr/bin/python
import Tkinter as tk
import numpy
from random import randint

class Application(tk.Frame):
    """
    Station class is used to define end stations in maaru simulation
    """
    class Station():
    
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        
        def rssi(self, copter):
            point_a = numpy.array((self.x, self.y))
            point_b = numpy.array((copter.x, copter.y))
            
            distance = numpy.sqrt(numpy.sum((point_a - point_b)**2))
            
            rssi = int(1/distance * 100000)
            return rssi
        
    class Copter():
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def flyToWaypoint(self):
            
            pass


    def __init__(self, max_x, max_y, master=None):
        tk.Frame.__init__(self, master)
        self.max_x = max_x
        self.max_y = max_y
        self.grid()
        self.createWidgets()
        self.flag = True

    def createWidgets(self):
        self.canvas = tk.Canvas(self, width = self.max_x, height = self.max_y, background='white')
        self.canvas.pack()
        self.canvas.grid()
        # quit button not working - TODO
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

    def quit(self):
        self.flag = False
        tk.Frame.quit(self)

    def addStations(self):
        # size of stations
        edge = 20
        # station 1: top of canvas
        s1 = self.Station(self.max_x/2, 10)
        station1 = self.canvas.create_rectangle(s1.x, s1.y, (s1.x + edge), (s1.y + edge), fill="red", tag='station1')
        self.text1 = self.canvas.create_text(s1.x + 60, s1.y + 10, text="RSSI", tag = "rssi1_label")
        
        # station 2: bottom of canvas
        s2 = self.Station(self.max_x/2, self.max_y - 10)
        station2 = self.canvas.create_rectangle(s2.x, (s2.y - edge), (s2.x + edge), s2.y, fill="green", tag='station2')
        self.text2 = self.canvas.create_text(s2.x + 60, s2.y - 10, text="RSSI", tag = "rssi2_label")
        
        self.s1 = s1
        self.s2 = s2


    def maaru(self):
    
        # random starting location
        start_x = randint(100, self.max_x - 100)/4
        start_y = randint(100, self.max_y - 100)/4
        # create quadcopter object
        maaru = self.Copter(start_x, start_y)

        testcopter = self.canvas.create_bitmap(maaru.x, maaru.y, bitmap="@./copter.xbm", tag='maaru')

        # initialize change in x, y
        dx = 2
        dy = 3
        # initialize boundaries of maaru for wall bouncing
        x0 = maaru.x - 40
        x1 = maaru.x + 40
        y0 = maaru.y - 40
        y1 = maaru.y + 40

        while self.flag:
            # update maaru location
            self.canvas.move('maaru', dx, dy)
            self.canvas.after(20)
            self.canvas.update()
            maaru.x += dx
            maaru.y += dy
            rssi1 = self.s1.rssi(maaru)
            rssi2 = self.s2.rssi(maaru)
            
            # update rssi text boxes
            self.canvas.itemconfigure(self.text1, text="RSSI: " + str(rssi1))
            self.canvas.itemconfigure(self.text2, text="RSSI: " + str(rssi2))
            
            # copter should bounce off of walls           
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
             

            if rssi1 > 335 and rssi2 > 335:
                self.flag = False


app = Application(800, 600)
app.master.title('Maaru Simulator')
app.addStations()
app.maaru()
app.mainloop()

