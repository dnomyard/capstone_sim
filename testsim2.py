#!/usr/bin/python
import MaaruSim


def main():
    testsim = MaaruSim.MaaruSim(1000, 650)
    
    # In your actual code, you will need to set a local variable for the
    # RSSI threshhold and then check the threshhold values in your 'main loop'
    # This method was just easier for this simulation . . .
    threshold = 225
    testsim.setRssiThresholds(threshold)
    
    x, y = testsim.getLocation()
    print "Starting location: " + str(x) + ", " + str(y)
    
    # In your actual code, you will need to compare the individual RSSI values
    # to whatever threshhold value you set above.  That will decide whether you 
    # have found a suitable location or whether you need to keep looking.
    while not testsim.checkThresholdMet():
        # This is where the 'meat' of your algorithm will be encoded.
        # As long as you have not found a suitable retrans location (i.e., one
        # in which the RSSI threshholds are met for both end stations), you 
        # need to keep executing your algorithm looking for a "better" spot.

        # This very simple algorith simply moves to what I know is the 
        # center of the map!
        
        # Here's how you get the current RSSI values from the two endpoints.
        s1_rssi = testsim.s1.getRssi(testsim.maaru)
        s2_rssi = testsim.s2.getRssi(testsim.maaru)
        
# ####
        testsim.moveToWaypoint(x-25, y-25)
        
        topLeft1 = testsim.s1.getRssi(testsim.maaru)
        topLeft2 = testsim.s2.getRssi(testsim.maaru)
        
        print str(topLeft1)
        print str(topLeft2)
        
        xTL = x-25
        yTL = y-25
        
        if topLeft1 >= topLeft2:
            topLeftValue = topLeft2
        if topLeft2 > topLeft1:
            topLeftValue = topLeft1
            
        if testsim.checkThresholdMet():
            break
        
        print "topLeftValue "+str(topLeftValue)
                
# ####
        testsim.moveToWaypoint(x, y-25)
        
        topMiddle1 = testsim.s1.getRssi(testsim.maaru)
        topMiddle2 = testsim.s2.getRssi(testsim.maaru)
        
        print str(topMiddle1)
        print str(topMiddle2)
        
        xTM = x
        yTM = y-25
        
        if topMiddle1 >= topMiddle2:
            topMiddleValue = topMiddle2
        if topMiddle2 > topMiddle1:
            topMiddleValue = topMiddle1
            
        if testsim.checkThresholdMet():
            break
        
        print "topMiddleValue "+str(topMiddleValue)
 
# ####        
        testsim.moveToWaypoint(x+25, y-25)
        
        topRight1 = testsim.s1.getRssi(testsim.maaru)
        topRight2 = testsim.s2.getRssi(testsim.maaru)
        
        print str(topRight1)
        print str(topRight2)
        
        xTR = x+25
        yTR = y-25
        
        if topRight1 >= topRight2:
            topRightValue = topRight2
        if topLeft2 > topRight1:
            topRightValue = topRight1
            
        if testsim.checkThresholdMet():
            break
        
        print "topRightValue "+str(topRightValue)
                        
# ####
        testsim.moveToWaypoint(x+25, y)
        
        rightMiddle1 = testsim.s1.getRssi(testsim.maaru)
        rightMiddle2 = testsim.s2.getRssi(testsim.maaru)
        
        print str(rightMiddle1)
        print str(rightMiddle2)
        
        xRM = x+25
        yRM = y
        
        if rightMiddle1 >= rightMiddle2:
            rightMiddleValue = rightMiddle2
        if rightMiddle2 > rightMiddle1:
            rightMiddleValue = rightMiddle1
            
        if testsim.checkThresholdMet():
            break
        
        print "rightMiddleValue "+str(rightMiddleValue)
 
# ####        
        testsim.moveToWaypoint(x+25, y+25)
        
        bottomRight1 = testsim.s1.getRssi(testsim.maaru)
        bottomRight2 = testsim.s2.getRssi(testsim.maaru)
        
        print str(bottomRight1)
        print str(bottomRight2)
        
        xBR = x+25
        yBR = y+25
        
        if bottomRight1 >= bottomRight2:
            bottomRightValue = bottomRight2
        if bottomRight2 > bottomRight1:
            bottomRightValue = bottomRight1
            
        if testsim.checkThresholdMet():
            break
        
        print "bottomRightValue "+str(bottomRightValue)
                        
# ####
        testsim.moveToWaypoint(x, y+25)
        
        bottomMiddle1 = testsim.s1.getRssi(testsim.maaru)
        bottomMiddle2 = testsim.s2.getRssi(testsim.maaru)
        
        print str(bottomMiddle1)
        print str(bottomMiddle2)
        
        xBM = x
        yBM = y+25
        
        if bottomMiddle1 >= bottomMiddle2:
            bottomMiddleValue = bottomMiddle2
        if bottomMiddle2 > bottomMiddle1:
            bottomMiddleValue = bottomMiddle1
            
        if testsim.checkThresholdMet():
            break
        
        print "bottomMiddleValue "+str(bottomMiddleValue)
 
# ####        
        testsim.moveToWaypoint(x-25, y+25)
        
        bottomLeft1 = testsim.s1.getRssi(testsim.maaru)
        bottomLeft2 = testsim.s2.getRssi(testsim.maaru)
        
        print str(bottomLeft1)
        print str(bottomLeft2)
        
        xBL = x-25
        yBL = y+25
        
        if bottomLeft1 >= bottomLeft2:
            bottomLeftValue = bottomLeft2
        if bottomLeft2 > bottomLeft1:
            bottomLeftValue = bottomLeft1
            
        if testsim.checkThresholdMet():
            break

        print "bottomLeftValue "+str(bottomLeftValue)
        
                        
# ####
        testsim.moveToWaypoint(x-25, y)
        
        leftMiddle1 = testsim.s1.getRssi(testsim.maaru)
        leftMiddle2 = testsim.s2.getRssi(testsim.maaru)
        
        print str(leftMiddle1)
        print str(leftMiddle2)
        
        xLM = x-25
        yLM = y
        
        if leftMiddle1 >= leftMiddle2:
            leftMiddleValue = leftMiddle2
        if leftMiddle2 > leftMiddle1:
            leftMiddleValue = leftMiddle1
            
        if testsim.checkThresholdMet():
            break
        
        print "leftMiddleValue "+str(leftMiddleValue)
 

# ### ###


        if topLeftValue == max(topLeftValue, topRightValue, bottomRightValue, bottomLeftValue, topMiddleValue, rightMiddleValue, bottomMiddleValue, leftMiddleValue):
            x = xTL
            y = yTL

        if topRightValue == max(topLeftValue, topRightValue, bottomRightValue, bottomLeftValue, topMiddleValue, rightMiddleValue, bottomMiddleValue, leftMiddleValue):
            x = xTR
            y = yTR

        if bottomRightValue == max(topLeftValue, topRightValue, bottomRightValue, bottomLeftValue, topMiddleValue, rightMiddleValue, bottomMiddleValue, leftMiddleValue):
            x = xBR
            y = yBR

        if bottomLeftValue == max(topLeftValue, topRightValue, bottomRightValue, bottomLeftValue, topMiddleValue, rightMiddleValue, bottomMiddleValue, leftMiddleValue):
            x = xBL
            y = yBL

        if topMiddleValue == max(topLeftValue, topRightValue, bottomRightValue, bottomLeftValue, topMiddleValue, rightMiddleValue, bottomMiddleValue, leftMiddleValue):
            x = xTM
            y = yTM

        if rightMiddleValue == max(topLeftValue, topRightValue, bottomRightValue, bottomLeftValue, topMiddleValue, rightMiddleValue, bottomMiddleValue, leftMiddleValue):
            x = xRM
            y = yRM

        if bottomMiddleValue == max(topLeftValue, topRightValue, bottomRightValue, bottomLeftValue, topMiddleValue, rightMiddleValue, bottomMiddleValue, leftMiddleValue):
            x = xBM
            y = yBM

        if leftMiddleValue == max(topLeftValue, topRightValue, bottomRightValue, bottomLeftValue, topMiddleValue, rightMiddleValue, bottomMiddleValue, leftMiddleValue):
            x = xLM
            y = yLM
        else:
            x = x+10
            y = y+10











        print "X: "+str(x)+" "+"Y: "+str(y)
        # Just printing the RSSI values
        #print "RSSI for station 1 = " + str(s1_rssi)
        #print "RSSI for station 2 = " + str(s2_rssi)

        
    # This line simply keeps the GUI up after the simulated copter stops
    # moving.  Without it, the program would simply exit.
    testsim.mainloop()
    
    
if __name__ == "__main__":
    main()

