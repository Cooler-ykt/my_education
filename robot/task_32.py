#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    Number_of_filled_cells=0
    while True:
        if wall_is_on_the_right():
            break
        elif not wall_is_above():
            while not wall_is_above():
                move_up()
                if cell_is_filled():
                    Number_of_filled_cells+=1
                else:
                    fill_cell()
            while not wall_is_beneath():
                move_down()
        else:
            fill_cell()
        move_right()
    mov("ax",Number_of_filled_cells)
if __name__ == '__main__':
    run_tasks()
