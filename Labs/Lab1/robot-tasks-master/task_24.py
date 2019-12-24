#!/usr/bin/python3

from pyrob.api import *
from fill_figure import *


def go_to_start(): # переходим в начало крестика это нижний конец креста
    move_down(3)
    move_right(2)






@task(delay=0.04)
def task_2_1():

    go_to_start()
    fill_cross()
    move_left()


if __name__ == '__main__':
    run_tasks()
