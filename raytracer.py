# a simple 3d-space raytracing algorithm
# operates on principle that incident angle = refl ang
# so in a 3d vector space (x, y, z), a collision on the x face of the constraint surface
# results in reflection velcotiy vector (-x, y, z) which retains incident angle
# by tom o'donnell

from vpython import *
import random

# set boundaries of system by making a 3d open-inside box
xlen, ylen, zlen = 100, 100, 100
boundaries = [
    box(pos = vector(0,-ylen/2,0), size = vector(xlen, .2, zlen)),
    box(pos = vector(0,ylen/2,0), size = vector(xlen, .2, zlen)),
    box(pos = vector(-xlen/2,0,0), size = vector(.2, ylen, zlen)),
    box(pos = vector(xlen/2,0,0), size = vector(.2, ylen, zlen)),
    box(pos = vector(0,0,-zlen/2), size = vector(xlen, ylen, .2))
    ]

# time delta between loops
dt = 0.001
old_pos = vec(0, 0, 0)


def main():
    
    # create sphere initialized at random loc/vel to act as photon
    old_pos = vec(random.randint(2, 45), random.randint(2, 45), random.randint(2, 45))
    b = sphere(pos=old_pos, radius=0.05, make_trail=True)
    b.vel = vec(random.randint(20, 25), random.randint(20, 25), random.randint(20, 25))
    c = curve(old_pos, old_pos)
   
    while True:
        # iteratively update position based on velocity
        rate(1/dt)
    
        update_pos(b, b.vel, b.pos, dt)
        
        # if ball collides with wall, we need to calculate the reflection vector
        col = wall_collision(b)
        if col != 0:
            update_vel(b, b.vel, b.pos, dt, col)

# simple position update formula
def update_pos(obj, vel, pos, dt):
    obj.pos = obj.pos + obj.vel*dt
    
# update velocity if experience a collision
def update_vel(obj, vel, pos, dt, col_type):
    if col_type == 1:
        # x collision
        obj.vel = vec(-obj.vel.x, obj.vel.y, obj.vel.z)
    if col_type == 2:
        # y collision
        obj.vel = vec(obj.vel.x, -obj.vel.y, obj.vel.z)
    if col_type == 3:
        # z collision
        obj.vel = vec(obj.vel.x, obj.vel.y, -obj.vel.z)

# rudimentary implementation of wall collision detection
# just determines of collision occurs tangent to sphere's surface
def wall_collision(obj):
    if obj.pos.x - obj.radius <= -(xlen/2) or obj.pos.x + obj.radius >= xlen/2:
        return 1
    elif obj.pos.y - obj.radius <= -(ylen/2) or obj.pos.y + obj.radius >= ylen/2:
        return 2
    elif obj.pos.z - obj.radius <= -(zlen/2) or obj.pos.z + obj.radius >= zlen/2:
        return 3
    return 0

if __name__ == "__main__":
    main()