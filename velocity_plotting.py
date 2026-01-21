import math 
import matplotlib.pyplot as plt
import numpy as np
import mplcursors

G = 9.81 # acceleration due to gravity
KM = 0.0253 # the acceleration constant due to air resistance, 1/2((air density)*(drag coefficeint)*(crossectional area)) / mass of the ball
angle = math.radians(75)
dt = 0.001


def find_distance_traveled(v1):
    x, y = 0.0, 0.0 # meters
    vx = v1 * math.cos(angle) # M/S
    vy = v1 * math.sin(angle)

    while (not(y <= 1.3 and vy < 0)): # change the y <= 1 to change how high you want the ball to land
        v = math.sqrt(vx * vx + vy * vy)

        ax = -KM * v * vx
        ay = -G - KM * v * vy

        # the smaller dt is the more accurate the model
        vx += ax * dt
        vy += ay * dt

        x += vx * dt
        y += vy * dt

    return x

x = [0.0]
y = [0.0]
i = 0.1

while(x[len(x) - 1] <= 8):
    x.append(find_distance_traveled(i/10)) # flips the x and the y so the x is the distance traveled and the y is the initial velocity
    y.append(i/10)
    i += 0.1

fig, ax = plt.subplots() 
ax.plot(x, y)
ax.axvline(x=0.7, color= 'r') # ranges, so the 0.7 is the minimum distance to shoot from based on these calculation since if it was closer it would hit the hub
ax.axvline(x=6, color='r') # maximum distance we would ever need to shoot from

t = np.linspace(0, 8, 100)
ax.plot(t, 1.4101*t + 5.3292, label='linear')
#have a cursor on the graph
mplcursors.cursor(ax, hover=True)
plt.show() 
