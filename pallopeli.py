import pygame
import numpy as np
import time
import sys

pygame.init()
pygame.mixer.init()
effect=pygame.mixer.music.load(open("D:\\boing2.wav","rb"))

clock = pygame.time.Clock()



screen_width=1000
screen_height=500
center=(screen_width/2,screen_height/2)

black = (0,0,0)

screen=pygame.display.set_mode([screen_width,screen_height])
pygame.font.init()

done=False
running=True
is_blue = True

left_bounce=False
right_bounce=False
floor_bounce=False
ball_created=False
collide=False

ball_dia=30
g=9.81
ball_velocity=np.array([5,0])
damping=0.9

def totuple(temp_array):
	try:
		return tuple(totuple(i) for i in temp_array)
	except TypeError:
		return temp_array

pygame.font.init()

def text_objects(text,font):
        textSurface=font.render(text, True, (0,0,255))
        return textSurface, textSurface.get_rect()

def message(text):
        myfont=pygame.font.SysFont("Calibri",60)
        TextSurf,TextRect=text_objects(text,myfont)
        TextRect.center=((screen_width/2)-(TextRect.width/2),(screen_height/2)-(TextRect.height/2))
        screen.blit(TextSurf,TextRect.center)
        pygame.display.update()

message("UUSI PELI PAINA VÄLILYÖNTIÄ")
    
def random_color():
        color_arr=np.random.random_integers(0,255, size=(3))
        color_array=totuple(color_arr)
        return color_array

def ball_create():
        ball_color=random_color()
        init_pos=pygame.mouse.get_pos()
        print(init_pos)
        pygame.draw.circle(screen,ball_color,init_pos,ball_dia,0)

        ball_color_np=np.asarray(ball_color)
        init_pos_np=np.asarray(init_pos)
        print(init_pos_np)
        return ball_color_np,init_pos_np


def ball_bounce(ball_p,ball_v,left_bounce,right_bounce,floor_bounce,ball_dia,damping):

        x=ball_v[0]
        y=ball_v[1]

        if ball_p[0]<=0+(ball_dia) and x<0:
                left_bounce=True
        if ball_p[0]>=screen_width-(ball_dia) and x>0:
                right_bounce=True
        if ball_p[1]>=screen_height-(ball_dia) and y>0:
                floor_bounce=True
        
        if left_bounce==True:
                ball_v=np.array([-x*damping,y])
        if right_bounce==True:
                ball_v=np.array([-x*damping,y])
        if floor_bounce==True:
                ball_v=np.array([x,-y*damping*damping])
        else:
                pass

        ball_v=ball_v.astype(int)
        
        return ball_v


def ball_collision(ball_p1,ball_p2,ball_v1,ball_v2,ball_dia,collide):

        
        
        x1=ball_p1[0]
        y1=ball_p1[1]
        x2=ball_p2[0]
        y2=ball_p2[1]
        vx1=ball_v1[0]
        vy1=ball_v1[1]
        vx2=ball_v2[0]
        vy2=ball_v2[1]

        dist=np.sqrt((x1-x2)**2+(y1-y2)**2)

        if dist<=(2*ball_dia):
                collide=True

        if collide==True and vx1>0 and vx2<0:
                vx1=-vx1
                vx2=-vx2
                

        elif collide==True and vx1<0 and vx2>0:
                vx1=-vx1
                vx2=-vx2
        elif collide==True and vx1>0 and vx2>0:
                vx1=vx1
                vx2=-vx2
        elif collide==True and vx1<0 and vx2<0:
                vx1=vx1
                vx2=-vx2
        else:
                collide=False
                

                #if x1>x2:
                        #x1=x1+ball_dia
                #else:
                        #x1=x1-ball_dia

        ball_v1_temp=np.array([vx1,vy1])
        ball_v2_temp=np.array([vx2,vy2])
        #ball_p1_temp=np.array([x1,y1])

        return ball_v1_temp,ball_v2_temp#,ball_p1_temp




def ball_pos(ball_p,ball_v):

        x_new=ball_p[0]+ball_v[0]
        y_new=ball_p[1]+ball_v[1]
        
        ball_pos_new=np.array([x_new,y_new])
        ball_pos_new=ball_pos_new.astype(int)
        return ball_pos_new
        
def ball_vel(ball_v):
        #print("ball_v[0] %s"%ball_v)
        x_vel=ball_v[0]
        y_vel=ball_v[1]+g
        
        ball_v_new=np.array([x_vel,y_vel])
        ball_v_new=ball_v_new.astype(int)
        return ball_v_new


def draw_ball(ball_color_tuple,ball_dia):
        
        ballsurface=pygame.Surface((ball_dia*2,ball_dia*2))
        ball=pygame.draw.circle(ballsurface,ball_color_tuple,(ball_dia,ball_dia),ball_dia,0)
        ballsurface.set_colorkey((0,0,0))

        return ballsurface

balls=0

while not done:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
                    pygame.quit()

                

        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                ball_color,ball_position=ball_create()
                #print(ball_color)
                #print(ball_position)
                ball_color_tuple=totuple(ball_color)
                ball_created=True
                ball_velocity=np.random.random_integers(20,50,size=(2))

                #print("ball velocity %s"%ball_velocity)

                if balls>50:
                        ball_cs=np.delete(ball_cs,0,0)
                        ball_vs=np.delete(ball_vs,0,0)
                        ball_ps=np.delete(ball_ps,0,0)
                        balls=balls-1

                if balls>100:
                        message("GAME OVER")
                        pygame.time.wait(2000)
                        done=True
                        pygame.quit()

                
                if balls==0:
                        ball_cs=ball_color
                        ball_vs=ball_velocity
                        ball_ps=ball_position

                else:
                        ball_cs=np.vstack((ball_cs,ball_color))
                        ball_vs=np.vstack((ball_vs,ball_velocity))
                        ball_ps=np.vstack((ball_ps,ball_position))

                balls=balls+1
                

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                x_val=0
                y_val=-10
                #point_y_temp_new=np.array([point_y_temp[0],point_y_temp[1]-10])
                #points=np.vstack((point_y_temp,point_y_temp_new))
                #point_y_temp=point_y_temp_new
                #pygame.draw.lines(screen, color, open, points, thickness)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                x_val=0
                y_val=10
                #point_y_temp_new=np.array([point_y_temp[0],point_y_temp[1]+10])
                #points=np.vstack((point_y_temp,point_y_temp_new))
                #point_y_temp=point_y_temp_new
                #pygame.draw.lines(screen, color, open, points, thickness)



        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                x_val=-10
                y_val=0
                #point_y_temp_new=np.array([point_y_temp[0]-10,point_y_temp[1]])
                #points=np.vstack((point_y_temp,point_y_temp_new))
                #point_y_temp=point_y_temp_new
                #pygame.draw.lines(screen, color, open, points, thickness)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                x_val=10
                y_val=0
                #point_y_temp_new=np.array([point_y_temp[0]+10,point_y_temp[1]])
                #points=np.vstack((point_y_temp,point_y_temp_new))
                #point_y_temp=point_y_temp_new
                #pygame.draw.lines(screen, color, open, points, thickness)


        if ball_created==True:

                if balls==1:

                        for i in range(balls):

                                        #screen.fill((0,0,0))
                                        velocity=ball_vel(ball_vs)
                                        position=ball_ps
                                        velocity_bounce=ball_bounce(position,velocity,left_bounce,right_bounce,floor_bounce,ball_dia,damping)
                                        position_final=ball_pos(position,velocity_bounce)

                                        ball_vs=velocity_bounce
                                        ball_ps=position_final

                                        ball_pos_tuple=totuple(position_final)
                                        ball_color_tuple=totuple(ball_cs)

                                        
                                        #effect.play()
                                                     

                                        ballsurface=draw_ball(ball_color_tuple,ball_dia)
                                        
                                        screen.blit(ballsurface,ball_pos_tuple)

                                        

                                        left_bounce=False
                                        right_bounce=False
                                        floor_bounce=False

                                        
                        
                
                if balls>1:
                
                        for i in range(balls):

                                        #screen.fill((0,0,0))
                                        velocity=ball_vel(ball_vs[i])
                                        position=ball_ps[i]
                                        
                                        
                                        #collision test
                                        for n in range(i,balls):
                                                velocity2=ball_vs[n]
                                                position2=ball_ps[n]
                                                velocity_1,velocity_2=ball_collision(position,position2,velocity,velocity2,ball_dia,ball_collision)
                                                ball_vs[n]=velocity_2
                                                collide=False


                                        velocity_bounce=ball_bounce(position,velocity_1,left_bounce,right_bounce,floor_bounce,ball_dia,damping)

                                        
                                        
                                        position_final=ball_pos(position,velocity_bounce)

                                        ball_vs[i]=velocity_bounce
                                        
                                        ball_ps[i]=position_final

                                        ball_pos_tuple=totuple(position_final)
                                        ball_color_tuple=totuple(ball_cs[i])

                                        ballsurface=draw_ball(ball_color_tuple,ball_dia)
                                        
                                        screen.blit(ballsurface,ball_pos_tuple)

                                        left_bounce=False
                                        right_bounce=False
                                        floor_bounce=False
                                        
                                        
                                

                clock.tick(48)
                pygame.display.flip()
                #pygame.display.update()
                screen.fill((0,0,0))

                
                        
                #ball_velocity=ball_vel(ball_velocity)
                #ball_velocity=ball_bounce(ball_position,ball_velocity,left_bounce,right_bounce,floor_bounce)
                #ball_position=ball_pos(ball_position,ball_velocity)

                #ball_pos_tuple=totuple(ball_position)
                #print(ball_pos_tuple)

                #ballsurface=draw_ball(ball_color_tuple,ball_dia)

                #screen.fill((0,0,0))
                #screen.blit(ballsurface,ball_pos_tuple)
                
                #left_bounce=False
                #right_bounce=False
                #floor_bounce=False

                
        else:
                pass
        

        
        #
        

