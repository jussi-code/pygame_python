import numpy as np
import pygame
import time
import sys

g=9.81/100

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

    return vectx,vecty

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

x=0
x0=x
y=500
y0=y

v0=2
alfa0=-70
t=0

while not done:


        ball_color=(255,0,0)
        pygame.draw.circle(screen,ball_color,(int(x),int(y)),50,0)

        

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
                    pygame.quit()
                    sys.exit()

        clock.tick(24)
        pygame.display.flip()
        screen.fill((0,0,0))

        x,y=angular_motion(-g,v0,x,y,alfa0,t)
        t=t+1



