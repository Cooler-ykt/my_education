#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    move_down(n=2)
    move_right()

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
    move_left()
    

if __name__ == '__main__':
    run_tasks()
