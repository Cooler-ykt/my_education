import math
import turtle


def draw_rectangle(Radius,pos_angle,n):


        storona=2*Radius*math.sin(math.pi/n)
        angle=360/n
        nach_povorot=pos_angle+180/n
        turtle.seth(nach_povorot)
        for i in range(n):
           turtle.forward(storona)
           turtle.left(angle)

turtle.shape('turtle')

kolvo=6
radius=5
shag=15

for i in range(kolvo):
      draw_rectangle(radius+(i+1)*shag,90,i+3)
      turtle.penup()
      turtle.seth(0)
      turtle.forward(shag)
      turtle.pendown()

	
    
