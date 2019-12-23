import math
import turtle


def draw_circle(Radius,pos_angle,rotation):

    n=36
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

radius=10
kovlo_par_lepestkov=8
shag=4
for i in range(kovlo_par_lepestkov):
     draw_circle(radius+shag*i,90,'Left')
     draw_circle(radius+shag*i,90,'Right')
