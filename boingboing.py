# dvd logo go boing boing
# by tom o'donnell 2021

from vpython import *
import random

dt = 0.01
coeff_rest = 0.95

#set scene
scene1 = canvas(title='phys_py by tom o\'donnell',
width=900, height=600,
center=vector(0,0,0), background=color.black, autoscale = True)

thick = 0.01
tall = 300
wide = 500
rt = shapes.rectangle(width=wide, height=tall, thickness=thick)
disc = extrusion( path = [vector(0,0,0), vector(0,0,thick)], shape = rt)

b = box(pos=vector(0,0,0), length=5, height=5, width=5, make_trail=True)
b.mass = 1000
rand_vel = random.randint(-10, 10)
rand_vel = rand_vel + 1
b.vel = vec(rand_vel, rand_vel, 0)

def main():
    global b

    while True:
        #real-time
        rate(1/dt)
        
        pf = b.mass * b.vel.y + -2.81*b.mass*dt
        b.vel.y = pf / b.mass

        #position update
        b.pos.x = b.pos.x + b.vel.x
        b.pos.y = b.pos.y + b.vel.y

      
        if abs(b.pos.x) + b.length - (wide/2 - thick*tall) > 0:
            b.vel.x = -coeff_rest*b.vel.x
        if abs(b.pos.y) + b.length - (tall/2 - thick*tall) > 0:
            b.vel.y = -coeff_rest*b.vel.y
        
           
if __name__ == "__main__":
    main()