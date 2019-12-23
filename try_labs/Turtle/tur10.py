import math
import turtle


def draw_circle(Radius,pos_angle,rotation):

    n=18
    storona=2*Radius*math.sin(math.pi/n)
    angle=360/n
   
    if rotation=='Left':
        nach_povorot=pos_angle+180/n
        turtle.seth(nach_povorot)
        for i in range(n):
           turtle.forward(storona)
           turtle.left(angle)
    else:        
        nach_povorot=pos_angle-180/n
        turtle.seth(nach_povorot)
        for i in range(n):
           turtle.forward(storona)
           turtle.right(angle)
    


turtle.shape('turtle')
kolvo=6
radius=50
shag=180/kolvo

for i in range(kolvo):
      draw_circle(radius,i*shag,'Left')
      draw_circle(radius,i*shag,'right')
	
    
