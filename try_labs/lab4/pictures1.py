from graph import *
from random import randint
from math import pi, sin, cos



def walls(x, y, Width, Height): # x y - левый нижний угол
    brushColor(168,124,92)
    rectangle(x, y, x + Width, y - Height)
    brushColor(255,255,255)
    
    
    
def window(x, y, Width, Height): # x y - центр окна
    brushColor(200,228,255)
    rectangle(x + Width//2, y + Height//2, x - Width//2, y - Height//2)
    line(x, y + Height//2, x, y - Height//2)
    line(x + Width//2, y, x - Width//2, y)
    brushColor(255,255,255)

def roof(x, y, Width, Height): # x y - центр основания крыши
    brushColor("red")
    polygon([(x - Width//2 - 5, y), (x + Width//2 + 5, y), (x, y - Height)])
    brushColor("white")

def house(x, y, Width, Height):
    """# x y - левый нижний угол домика
    """
    k = 1.8 
    walls(x, y, Width, Height//k)
    window(x + Width//2, y - Height/k//2, Width//2, Height/k//2)
    roof(x + Width//2, y - Height/k, Width, Height*(1 - 1/k)//1)



def stvol(x, y, Height): # x y - центр основания ствола дерева
    brushColor("brown")
    rectangle(x-10, y, x+10, y-Height)
    brushColor("white")

def listya(x, y , Whidth, Height): # x y - центр листьев
    brushColor("green")
    j=int(Whidth*Height//100)
    for i in range(j):
        x1 = x - Whidth//2 + randint(0,Whidth)
        y1 = y - Height//2 + randint(0,Height)
        
        circle(x1, y1, 10)

    
    brushColor("white")
    


    
def tree(x, y, Height): # x y - центр основания ствола дерева
    stvol(x, y, Height//1.3)
    listya(x, y - Height//1.3, Height//2, Height//1.5)

def cloud(x, y, Whidth): # x y - центр облака
    brushColor('white')
    penColor('white')
    j=int(Whidth//10)
    for i in range (j):
        circle(x+randint(0,Whidth) - Whidth//2,y-randint(0,60)+30,25)
    penColor('black')
def sun(x, y, smallRadius, bigRadius, numberOfRays):
    D_alfa=pi/numberOfRays
    P=[]
    alfa=0
    for i in range(numberOfRays*2):
        alfa=alfa+D_alfa
        if i%2 == 0:
            x1=int((smallRadius*sin(alfa)//1)+x)
            y1=int((smallRadius*cos(alfa)//1)+y)
            P.append((x1,y1))
        else:
            x1=int((bigRadius*sin(alfa)//1)+x)
            y1=int((bigRadius*cos(alfa)//1)+y)
            P.append((x1,y1))
    brushColor("yellow")
    penColor("yellow")    
    polygon(P)
    brushColor("white")
    penColor("black")    
        
    

sun(220, 300, 50, 100, 15)
