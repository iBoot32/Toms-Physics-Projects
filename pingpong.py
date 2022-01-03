from vpython import *

dt = 0.001
stat = box(size=vector(2,.1,2), pos=vector(0,0,0), color=color.red)
stat.vel = vec(0,0,0)

ball = sphere(pos=vector(0,2,0), radius=0.05)
ball.vel = vec(0,0,0)
ball.mass = 100
    


def update():
    global ball
    
    while(True):
        rate(150)
        
        # momentum and velocity update
        pf = ball.mass * ball.vel.y + -9.81*dt
        ball.vel.y = pf / ball.mass
        
        #position update
        ball.pos.y = ball.pos.y + ball.vel.y
        detect_collision("", "")
        
def detect_collision(obj1, obj2,):
    print()


if __name__ == "__main__":
    update()