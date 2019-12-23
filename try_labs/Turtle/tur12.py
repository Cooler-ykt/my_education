import math
import turtle


def draw_circle(Radius,pos_angle,rotation):

    n=4
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
    

def draw_duga(Radius,pos_angle,rotation):

    n=36
    storona=2*Radius*math.sin(math.pi/n)
    angle=360/n
   
    if rotation=='Left':
        nach_povorot=pos_angle+180/n
        turtle.seth(nach_povorot)
        for i in range(n//2):
           turtle.forward(storona)
           turtle.left(angle)
    else:        
        nach_povorot=pos_angle-180/n
        turtle.seth(nach_povorot)
        for i in range(n//2):
           turtle.forward(storona)
           turtle.right(angle)


radius_bolshoy=20
radius_maliy=5
kovlo_vitkov=5

turtle.shape('turtle')
for i in range(kovlo_vitkov):
     draw_duga(radius_bolshoy,90,'Right')
     draw_duga(radius_maliy,270,'Right')
