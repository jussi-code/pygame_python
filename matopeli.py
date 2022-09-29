import pygame
import numpy as np
import time
import sys

pygame.init()
clock = pygame.time.Clock()

screen_width=1000
screen_height=500
screen=pygame.display.set_mode([screen_width,screen_height])

done=False
running=True
is_blue = True


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

#message("NEW GAME")


zero_point=np.array([300,300])
point_y_temp=zero_point
points_history=np.array([[300,310]])
x_val=0
y_val=-10
color = (255, 100, 0)
thickness=10
collision=False



        

#main part#

while not done:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
                    pygame.quit()

                
                

    
        
        

        #pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
        #pygame.draw.circle(screen,(0,250,0),(200,200),10,0)


        #pygame.draw.lines(screen, color, open, pointlist, thickness)


        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

        

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


        point_y_temp_new=np.array([point_y_temp[0]+x_val,point_y_temp[1]+y_val])
        points=np.vstack((point_y_temp,point_y_temp_new))
        
        
        pygame.draw.lines(screen, color, open, points, thickness)

        test_history=point_y_temp_new==points_history
        point_y_temp=point_y_temp_new

        if point_y_temp_new[0]==0 or point_y_temp_new[0]==screen_width:
                
                        
                pygame.time.delay(2000)
                message("GAME OVER")
                collision=True


        elif point_y_temp_new[1]==0 or point_y_temp_new[1]==screen_height:
                
                        
                pygame.time.delay(2000)
                message("GAME OVER")
                collision=True
                        


 
        for i in range(len(test_history)):
                
                if test_history[i][0]==True and test_history[i][1]==True:
                        
                        
                        
                        message("GAME OVER")
                        pygame.time.wait(2000)
                        
                        collision=True


                        
                else:
                     pass
                
        if collision==True:
                done=True
                pygame.quit()
                sys.exit()
        else:
                pass
        
        
        points_history=np.vstack((points_history,point_y_temp_new))
        #print(points_history)

          
        clock.tick(10)
        pygame.display.flip()
        

