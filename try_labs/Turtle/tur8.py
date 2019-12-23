import turtle

turtle.shape('turtle')

kolvo_vitkov=10
shag=20
speed=90   # 1,2,3,4,5,6,9,10,12,15,18,20,30,36,40,45,60,72,90,120 
turtle.left(90)
for i in range(kolvo_vitkov):
    for j in range(0,360,speed):
         shag_pauka=((i+j/360)*shag)
         turtle.forward(shag_pauka)
         turtle.left(speed) 
 
