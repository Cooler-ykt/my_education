#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():

    while not wall_is_beneath():
        move_down()
    x=0

    while wall_is_beneath():
        move_right()
        x+=1


    move_down()

    for i in range(x):
        move_left()

    


if __name__ == '__main__':
    run_tasks()
