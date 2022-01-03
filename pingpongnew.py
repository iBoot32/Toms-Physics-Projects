# chaotic ball bouncing and rolling inside a circle boundary
# by tom o'donnell 2021

from vpython import *
import random
import math

dt = 0.01
coeff_rest = 0.9

#set scene
scene1 = canvas(title='phys_py by tom o\'donnell',
width=900, height=600,
center=vector(0,0,0), background=color.black, autoscale = True)

#set up chaotic ball       
orig = vec(0,0,0)
b = sphere(pos=orig, radius=2, color = color.blue)
b.vel = vec(1, random.randint(-1,1),0)
b.mass = 10000


v1 = vec(-160, -100, 0)
v2 = vec(-190, 120, 0)

v3 = vec(160, -100, 0)
v4 = vec(190, 120, 0)
c1=curve(v1, v2)
c2=curve(v3, v4)


def run_phys():
    while(True):
        rate(1/dt)
        
        b.vel = vec(b.vel.x, (b.mass * b.vel.y + -9.81*b.mass*dt)/b.mass, 0)
        b.pos = vec(b.pos.x + b.vel.x, b.vel.y, 0)
    
        if(collision(b.pos.x, b.pos.y)):
            #inv tan of slope to get angle from vert
            print()

def collision(x, y):
    x1 = v1.x
    y1 = v1.y
    x2 = v2.x
    y2 = v2.y
    
    if (y - y1)/(y2 - y1) - (x - x1)/(x2 - x1) <= 0:
        return True
    else:
        x1 = v3.x
        y1 = v3.y
        x2 = v4.x
        y2 = v4.y
        
        if (y - y1)/(y2 - y1) - (x - x1)/(x2 - x1) <= 0:
            return True
    
if __name__ == "__main__":
    run_phys()