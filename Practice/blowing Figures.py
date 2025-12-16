# #############################################
# Date: 12-2-25
# Exercises - blowing points 
# Name: Omar Ali
# #############################################

####Purpose: Make a simple picture of dots that look like leaves being blown by wind from the left side of the screen.

####Output: A matplotlib window that shows the final picture. 

###Feature tasks completed 
###1 - The dots have multiple colors.
###2 - The colors follow a pattern that matches the "leaves in the wind" idea.
###3 - The program has a few easy parameters the user can change.


#  First I'll do my imports and path setup 

import sys
sys.path.append(r"C:\Users\omarali\python\lib") 

from geom.point import Point        
import random                       # for random starting locations
import matplotlib.pyplot as plt     # for plotting the points


# easy parameters that I changed

# how many dots / how many rounds the wind blows / basic wind speed near the source / controls how fast dots move

NUM_POINTS = 800       
NUM_STEPS = 20        
SPEED_AT_SOURCE = 1.5 
FRACTION = 0.01       


# make the starting dots and split them into color groups
# bottom = green, middle = orange, top = red
# this fits the idea of leaves at different heights
# near the ground
# middle band
# top band

points = []
low_points = []    
mid_points = []    
high_points = []

for _ in range(NUM_POINTS):
    x = random.uniform(0, 10)
    y = random.uniform(0, 10)
    p = Point(x, y)
    points.append(p)

    if y < 10.0 / 3:
        low_points.append(p)
    elif y < 2 * 10.0 / 3:
        mid_points.append(p)
    else:
        high_points.append(p)


# simple speed function same idea as the sample code
# distance : distance from wind source to the point

def speed(distance, speed0, fraction):
    return speed0 * fraction * distance

# wind source on the left side
source = Point(-5, 5)


# set up the plot and draw the starting positions

fig, ax = plt.subplots()

ax.scatter([p.x for p in low_points],
           [p.y for p in low_points],
           edgecolors="none", facecolors="green", marker="o", alpha=0.3)

ax.scatter([p.x for p in mid_points],
           [p.y for p in mid_points],
           edgecolors="none", facecolors="orange", marker="o", alpha=0.3)

ax.scatter([p.x for p in high_points],
           [p.y for p in high_points],
           edgecolors="none", facecolors="red", marker="o", alpha=0.3)


# main loop: move dots away from the wind source
# direction is from the source to the point
# I use distance and simple x,y math 

for step in range(NUM_STEPS):
    for p in points:
        d = source.distance(p)   
        if d == 0:
            continue           

        move = speed(d, SPEED_AT_SOURCE, FRACTION)

     
        dx = (p.x - source.x) / d
        dy = (p.y - source.y) / d

      
        p.x += dx * move
        p.y += dy * move

    
    alpha = 0.1 + 0.9 * (step + 1) / NUM_STEPS

    ax.scatter([p.x for p in low_points],
               [p.y for p in low_points],
               edgecolors="none", facecolors="green", marker="o", alpha=alpha)

    ax.scatter([p.x for p in mid_points],
               [p.y for p in mid_points],
               edgecolors="none", facecolors="orange", marker="o", alpha=alpha)

    ax.scatter([p.x for p in high_points],
               [p.y for p in high_points],
               edgecolors="none", facecolors="red", marker="o", alpha=alpha)


# tidy up axes similar to examples in the notes

ax.set_aspect(1)       
ax.set_xlim(0, 20)      
ax.set_ylim(0, 12)

ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
ax.set_frame_on(False)

plt.show()
