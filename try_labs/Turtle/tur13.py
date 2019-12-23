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
    

def draw_duga(Radius,pos_angle,rotation):

    n=180
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



turtle.shape('turtle')
turtle.color("black", "yellow")
turtle.begin_fill()
draw_circle(100,90,"Left")
turtle.end_fill()
turtle.seth(180)
turtle.penup()
turtle.forward(100)
turtle.seth(90)
turtle.forward(45)
turtle.seth(180)
turtle.forward(30)
turtle.seth(90)
turtle.color("black", "blue")
turtle.pendown()
turtle.begin_fill()
draw_circle(10,90,"Left")
turtle.end_fill()
turtle.penup()
turtle.seth(0)
turtle.forward(60)
turtle.pendown()
turtle.begin_fill()
draw_circle(10,90,"Right")
turtle.end_fill()
turtle.penup()
turtle.seth(180)
turtle.forward(30)
turtle.seth(270)
turtle.forward(55)
turtle.seth(90)
turtle.width(10)
turtle.pendown()
turtle.forward(40)
turtle.penup()
turtle.backward(45)
turtle.color("red", "black")
turtle.seth(180)
turtle.forward(50)
turtle.pendown()
draw_duga(50,270,"Left")



