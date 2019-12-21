#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():

        move_down()
        while True:

            fill_cell()
            move_down()
            move_right()
            fill_cell()
            move_right()
            move_up()
            fill_cell()
            move_left()
            fill_cell()
            move_up()
            fill_cell()
            for i in range(3):
                if wall_is_on_the_right():
                    break
                move_right()
            if wall_is_on_the_right():
                    break
            move_down()
     
        for j in range(4):
            move_down(5)
            move_left(38)
                
            while True:

                fill_cell()
                move_down()
                move_right()
                fill_cell()
                move_right()
                move_up()
                fill_cell()
                move_left()
                fill_cell()
                move_up()
                fill_cell()
                for i in range(3):
                    if wall_is_on_the_right():
                        break
                    move_right()
                if wall_is_on_the_right():
                        break
                move_down()
        move_left(38)
     

if __name__ == '__main__':
    run_tasks()
