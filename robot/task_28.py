#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():

    x=0
    x=x+cell_is_filled()    
    while x<5:
        move_right()
        x=x+cell_is_filled()



if __name__ == '__main__':
    run_tasks()
