# chaotic ball bouncing and rolling inside a circle boundary
# by tom o'donnell 2021

from vpython import *
import random
import math

dt = 0.009
coeff_rest = 0.90

#set scene
scene1 = canvas(title='phys_py by tom o\'donnell',
width=900, height=600,
center=vector(0,0,0), background=color.black, autoscale = True)

#set up chaotic ball       
orig = vec(400,-300,0)
b = sphere(pos=orig, radius=35, color = color.blue)
b.vel = vec(20, 20,0)
b.mass = 100

# set up circular boundary
thick = vec(0.001, 0.001, 0.001)
radius = 700
c = shapes.circle(radius=radius, thickness=thick.x)
disc = extrusion( path = [vector(0,0,0), vector(0,0,30)], shape = c)
    
def run_phys():
    global b

    
    while True:
        #real-time
        rate(1/dt)
        
        # momentum and velocity update
        pf = b.mass * b.vel.y + -7.81*b.mass*dt
        b.vel.y = pf / b.mass
        
        #position update
        b.pos.x = b.pos.x + b.vel.x
        b.pos.y = b.pos.y + b.vel.y
        
        # collision detection with wall
        if(wall_collision(b)):
            b.vel = vec(-coeff_rest*b.vel.y, coeff_rest*b.vel.x, 0)
    return

def wall_collision(obj):
    while abs(mag(obj.pos) + obj.radius) > abs(radius - thick.x*radius):
        # ball is now a point on the insode of circle
        # now how to we calculate the resulting motion?
        # we need the slope of the tangent line at that point
        
        # probably use arctan to get angle from horiz
        # then orig vel * sin(angle) for new x
        #slope = -obj.pos.x / obj.pos.y
        #c = curve([vec(obj.pos.x, obj.pos.y, 0), vec(obj.pos.x+100, obj.pos.y+slope*100, 0)])
        #ang = (degrees(atan(slope)))
        #print(ang)
        #d = curve([vec(0,0,0), vec(obj.pos.x, obj.pos.y, 0)])
        #print(getAngle(orig, vec(obj.pos.x, obj.pos.y, 0), vec(0,0,0)))
        
        
        return True
    

def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c.y-b.y, c.x-b.x) - math.atan2(a.y-b.y, a.x-b.x))
    return ang



if __name__ == "__main__":
    run_phys()