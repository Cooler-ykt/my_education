#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():

    x=1
    while not wall_is_beneath():
        x+=1
        move_down()
        j=x
    while True:
        j-=2
        for i in range(j):
            move_up()
            fill_cell()
        else:
            move_up()
    
        for i in range(j):
            move_right()
            fill_cell()
        else:
            move_right()
    
        for i in range(j):
            move_down()
            fill_cell()
        else:
            move_down()
    
        for i in range(j):
            move_left()
            fill_cell()
        else:
            move_left()

        if j==1:
            break
        move_up()
        move_right()

    for i in range((x-3)//2):
        move_left()
        move_down()
        

if __name__ == '__main__':
    run_tasks()
