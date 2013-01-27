#!/usr/bin/python
import MaaruSim

def main():
    testsim = MaaruSim.MaaruSim(1000, 650)
    
    # In your actual code, you will need to set a local variable for the
    # RSSI threshhold and then check the threshhold values in your 'main loop'
    # This method was just easier for this simulation . . .
    testsim.setRssiThresholds(20)
    
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

        testsim.moveToWaypoint(x-50, y-50)
        if testsim.checkThresholdMet():
            break
        
        testsim.moveToWaypoint(x+50, y-50)
        if testsim.checkThresholdMet():
            break
        
        testsim.moveToWaypoint(x+50, y+50)
        if testsim.checkThresholdMet():
            break
        
        testsim.moveToWaypoint(x-50, y+50)
        if testsim.checkThresholdMet():
            break

        # Here's how you get the current RSSI values from the two endpoints.
        s1_rssi = testsim.s1.getRssi(testsim.maaru)
        s2_rssi = testsim.s2.getRssi(testsim.maaru)

        # Just printing the RSSI values
        print "RSSI for station 1 = " + str(s1_rssi)
        print "RSSI for station 2 = " + str(s2_rssi)

        
    # This line simply keeps the GUI up after the simulated copter stops
    # moving.  Without it, the program would simply exit.
    testsim.mainloop()
    
    
if __name__ == "__main__":
    main()

