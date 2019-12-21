import turtle
from random import randint

def mnogougolnik(storona,kolvoUglov):
    turtle.shape('turtle')
    if 360%kolvoUglov == 0 :
        ugol=360/kolvoUglov
        for i in range(0,360,int(ugol//1)):
            turtle.forward(storona)
            turtle.left(ugol)
    else:
        ugol=360/kolvoUglov
        for i in range(10,360,int(ugol//1)):
            turtle.forward(storona)
            turtle.left(ugol)

number_of_iterations = 20    # <- Это количество витков спирали
size = 20                    # <- Это размер спирали
step_in_degrees = 70        # <- Тут можешь написать любое число от 1 до 360
                        # интересные 120 90 72 60 51 45 , и близкие к ним числа
                        # Напрпимер 122 118  88 92  70 74  62 58  49 53  43 47
                        # Это градус на который будет поворачиваться черепашка
                        # перед каждым забегом


#-------------------Снизу задание черепашке рисовать спираль---------------------
                        
for  i  in  range(number_of_iterations): # <-этот цикл делает количество витков
    for  j  in  range(0, 360, step_in_degrees):  #<-этот цикл делает один виток
         run_distance=( (i + j/360)*size ) # <-вычисляется по формуле растояние
         turtle.forward(run_distance) # <- черепашка бежит на это растояние
         mnogougolnik(80,5)
         turtle.left(step_in_degrees) # <- черепашка поворачивается на градус
                                     



        
   
        
