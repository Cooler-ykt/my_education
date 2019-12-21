#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():

    while not wall_is_on_the_right():
        if wall_is_above() and wall_is_beneath():
            fill_cell()
        move_right()
    else:
        if wall_is_above() and wall_is_beneath():
            fill_cell()


    while wall_is_above():
        move_left()
    move_up()


    while not wall_is_on_the_left():
        if not wall_is_beneath():
            fill_cell()
        move_left()
    else:
        if not wall_is_beneath():
            fill_cell()



    while wall_is_beneath():
        move_right()
    move_down()



    while not wall_is_on_the_left():
        move_left()
        

    while wall_is_beneath():
        move_right()
    else:
        move_down()


    while not wall_is_on_the_right():
        if not wall_is_above():
            fill_cell()
        move_right()
    else:
        if not wall_is_above():
            fill_cell()


    while wall_is_above():
        move_left()
    move_up()
    while not wall_is_on_the_right():
        move_right()
            


if __name__ == '__main__':
    run_tasks()
