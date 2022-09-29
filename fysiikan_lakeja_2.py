import numpy as np
import pygame
import time
import sys

g=9.81

#fysiikan lakeja


#painovoima
def gravity(mass, gravity):
    Fg=mass*gravity
    return Fg

#liikekitka
def m_friction(yk,F_normal):
    Fyk=yk*F_normal
    return Fyk

#lepokitka
def s_friction(ys, F_normal):
    Fys=ys*F_normal
    return Fys

#tasaisesti muuttuva liike
def motion(x0,v0,a,t):
    x=x0+v0*t+0.5*a*t**2
    return x

def speed(v0,a,t):
    v=v0+a*t
    return v

#vino heittoliike
def angular_motion(g,v0,x0,y0,alfa0,t):
    angle=np.pi*alfa0/180
    v0x=v0*np.cos(angle)
    v0y=v0*np.sin(angle)

    x=x0+v0x*t
    y=y0+v0y*t-0.5*g*t**2
    
    return x,y

#kahden kappaleen vektori
def vector(x1,y1,x2,y2):
    a=x2-x1
    b=y2-y1

    c=np.sqrt(a**2+b**2)

    vectx=a/c
    vecty=b/c

    return vectx,vecty,c

#gravitaatiolaki
def gravity(m1,m2,r):
    G=6.672e-11

    F=G*(m1*m2)/(r**2)
    a1=F/m1
    a2=F/m2

    return F,a1,a2


#PYGAME initiointi
    
pygame.init()
clock = pygame.time.Clock()

screen_width=1500
screen_height=1000
center=(screen_width/2,screen_height/2)

black = (0,0,0)
done=False

screen=pygame.display.set_mode([screen_width,screen_height])
pygame.font.init()

#main part#

x1=0
y1=500
 
x2=1500
y2=500

v1x=0
v1y=3

v2x=0
v2y=-3

alfa0=-70
t=0

m1=9e14
m2=9e14

rc=0
gc=0
bc=0

while not done:



        ball_color1=(rc,gc,bc)
        ball_color2=(rc,gc,bc)
        pygame.draw.circle(screen,ball_color1,(int(x1),int(y1)),10,0)
        pygame.draw.circle(screen,ball_color2,(int(x2),int(y2)),10,0)
        

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
                    pygame.quit()
                    sys.exit()

        clock.tick(24)
        pygame.display.flip()
        #screen.fill((0,0,0))

        vectx,vecty,r=vector(x1,y1,x2,y2)
        F,a1,a2=gravity(m1,m2,r)

        a1x=a1*vectx
        a1y=a1*vecty

        a2x=a2*-vectx
        a2y=a2*-vecty

        v1x=speed(v1x,a1x,1)
        v1y=speed(v1y,a1y,1)

        v2x=speed(v2x,a2x,1)
        v2y=speed(v2y,a2y,1)       

        x1=motion(x1,v1x,a1x,1)
        y1=motion(y1,v1y,a1y,1)

        x2=motion(x2,v2x,a2x,1)
        y2=motion(y2,v2y,a2y,1)

        if rc<=254:   
                rc=rc+1
        elif rc==255 and gc<=254:
                gc=gc+1
        elif gc==255 and bc<=254:
                bc=bc+1

        if bc==255:
            rc=0
            gc=0
            bc=0

        #print(rc)
            
            
        



