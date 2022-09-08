"""
Calculates horizontal and vertical velocities along
with travel time and distance traveled
"""
import math

__author__ = "David Walker"
__version__ = "2/13/2019"
__pylint__ = "2.12.2"

if __name__ == '__main__':

    vel = float(input("Initial launch velocity in meters per second: "))
    launchangle = float(input("Launch Angle in degrees: "))

    if launchangle < 0:
        print('Error')

    if launchangle > 0:
        launchangle = float(math.radians(launchangle))
        vx = vel * math.cos(launchangle)
        vy = vel * math.sin(launchangle)
        print ("Horizontal Velocity: {vx}")
        print ("Veritcal Velocity: {vy}")
        option = (input("Enter Y if the object is landing at the same elevation it is launching from or N if the object is not landing on the same elevation: "))
        if option in ('y', 'Y'):
            h = vel**2 * math.sin(2 * launchangle)
            hr = float(h / 9.81)
            t = float(2 * vel * math.sin(launchangle))
            ti = float(t / 9.81)
            hi = float (hr * 1/2)
            print ("Horizontal Range: {hr} meters")
            print ("Time elapsed: {ti} sec")
            print ("Maximum height reached: {hi} meters")
        elif option in ('N', 'n'):
            el = float(input("Enter the elevation in meters: "))
            mht = float(vy / 9.81)
            ACC = (0.5 * 9.81)
            mh = float(vy*mht - ((ACC)*mht**2) + 10)
            print ("Time of max height: {mht} sec")
            d = ((vy **2) - (4 * (-ACC) * el))
            sol1 = float((-vy - math.sqrt(d))/(2*(-ACC)))
            sol2 = float((-vy + math.sqrt(d))/(2*(-ACC)))
            print("Flight Time in sec: {sol1} sec")
            hr = float(vx * sol1)
            print("Max Height: {mh} meters")
            print("Horizontal Range: {hr} meters")
