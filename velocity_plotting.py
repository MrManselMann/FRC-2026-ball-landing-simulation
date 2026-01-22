import math 
import matplotlib.pyplot as plt
import numpy as np
import mplcursors

G = 9.81 # acceleration due to gravity
KM = 0.0253 # the acceleration constant due to air resistance, 1/2((air density)*(drag coefficeint)*(crossectional area)) / mass of the ball
angle = math.radians(75)


##this is for calculating the affect the backspin has on the trajectory ,    The Magnus Effect
magnus = 0.00378 # magnus = (0.5 * air_density * ball_radius * cross_sectional_area) / ball_mass
spin_rate = 50 #rad/s

dt = 0.001
min = 0.7
max = 6

def find_distance_traveled(v1):
    x, y = 0.0, 0.0 # meters
    vx = v1 * math.cos(angle) # M/S
    vy = v1 * math.sin(angle)

    while (not(y <= 1.3 and vy < 0)): # change the y <= 1.3 to change how high you want the ball to land, that number is the vertical difference between the shooter and hub
        v = math.sqrt(vx * vx + vy * vy)

        ax = -KM * v * vx  +  magnus * spin_rate * vy
        ay = -G - KM * v * vy  -  magnus * spin_rate * vx

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
ax.axvline(x=min, color= 'r', linestyle='--') # ranges, so the min is the minimum distance to shoot from based on these calculation since if it was closer it would hit the hub
ax.axvline(x=6, color='r', linestyle='--') # maximum distance we would ever need to shoot from

#linear regression
x_np = np.array(x)
y_np = np.array(y)

mask = (x_np >= min) & (x_np <= max)
m, b = np.polyfit(x_np[mask], y_np[mask], 1) #using numpy to figure out the lin-reg model
print(m, b)
t = np.linspace(0, 8, 100)
ax.plot(t, m*t + b, label='linear')

#have a cursor on the graph
mplcursors.cursor(ax, hover=True)
plt.show() 


## for RPM conversion, v_BALL = 60* V_ANGULAR(rad/s) * Radius of Flywheel * some constant (n) which represents the effectiviness of the flywheel, can be tested
