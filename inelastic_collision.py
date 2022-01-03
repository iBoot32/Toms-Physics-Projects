# inelastic collision of two objects
# with zero drag/friction or vertical vel/acc
# by tom o'donnell 2021

from vpython import *

dt = 0.0001
t = 0
c = 0

#set scene
scene1 = canvas(title='phys_py by tom o\'donnell',
width=900, height=600,
center=vector(0,0,0), background=color.black, autoscale = False)

#set moving box        
b = box(size=vector(2,2,2), pos=vector(8,0,0), color=color.green)
b.mass = 30000
b.vel = vec(-250,0,0)
  
#set static box   
stat = box(size=vector(1,1,1), pos=vector(0,0,0), color=color.blue)
stat.mass = 5
stat.vel = vec(0,0,0)
    
#wall 
wallL = box(pos=vector(-10,0,0), size=vector(1,12,12), color=color.green) 



def set_scene():
    run_phys()
    return
    
def run_phys():
    global b
    global c
    global stat

    
    while True:
        rate(150)
        
        # collision detection
        print(f'{b.pos - stat.pos} tot={b.size.x + stat.size.x}')
        if touching(b, stat):
            # velocity update of an inelastic collision
            new_b_vel = ((b.mass - stat.mass) / (b.mass + stat.mass))*b.vel.x + ((2*stat.mass)/(b.mass + stat.mass))*stat.vel.x
            stat.vel.x = ((2*b.mass)/(b.mass + stat.mass))*b.vel.x + ((stat.mass - b.mass)/(b.mass+stat.mass))*stat.vel.x
            b.vel.x = new_b_vel
            
            #count number of collisions
            c = c + 1
            print(c)
            
        #collision detection with wall 
        if touching(stat, wallL):
            stat.vel.x = -stat.vel.x
        
        # position updates
        b.pos = b.pos + b.vel*dt
        stat.pos = stat.pos + stat.vel*dt         
    return

def touching(obj1, obj2):
    # if the absolute value of the difference in the x component of their position vectors is less then the sum of their radii
    # then they must be touching
    if abs(obj2.pos.x - obj1.pos.x) < abs(obj1.size.x/2 + obj2.size.x/2):
        return True
    return False



if __name__ == "__main__":
    set_scene()