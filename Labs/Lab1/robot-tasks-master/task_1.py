#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.04)
def task_1_1():
    move_right(2)
    move_down()



if __name__ == '__main__':
    run_tasks()
