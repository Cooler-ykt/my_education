import math
import turtle


def draw_star(Radius,n):

    angle=180-180/n
   
    for i in range(n):
           turtle.forward(Radius)
           turtle.right(angle)
    



turtle.shape('turtle')
draw_star(100,5)
turtle.penup()
turtle.seth(0)
turtle.forward(150)
turtle.pendown()
draw_star(100,11)




