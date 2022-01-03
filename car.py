from vpython import *
import random
import math

dt = 0.01

#set scene
scene1 = canvas(title='phys_py by tom o\'donnell',
width=900, height=600,
center=vector(0,0,0), background=color.black, autoscale = True)

#set cars 
a = box(size=vector(15,15,15), pos=vector(250,-200,0), color=color.green)
a.mass = 35
a.vel = vec(-65,50,0)
       
b = box(size=vector(10,10,10), pos=vector(-250,-200,0), color=color.green)
b.mass = 30
b.vel = vec(65,50,0)


def run_phys():
    while True:
        rate(1/dt)
        a.pos = a.pos + a.vel*dt
        b.pos = b.pos + b.vel*dt
        
        if a.pos.x - a.size.x/2 - b.pos.x -b.size.x/2 <= 0:
           new_vel = (a.mass*a.vel + b.mass*b.vel)  / (a.mass + b.mass)
           a.vel = new_vel
           b.vel = a.vel

if __name__ == "__main__":
    run_phys()

