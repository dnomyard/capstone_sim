#!/usr/bin/python

import MaaruSim

def main():
    testsim = MaaruSim.MaaruSim(1000, 650)
    testsim.setRssiThresholds(220)
    testsim.randomTest()
    #while not testsim.checkThresholdMet():
    #    testsim.moveToWaypoint(500, 325)
    testsim.mainloop()


if __name__ == "__main__":
    main()

