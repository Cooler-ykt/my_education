#!/usr/bin/python3

from pyrob.api import *
from fill_figure import *

def go_to_start(): # переходим в начало крестика это нижний конец креста
    move_down(3)
    move_right()

def move_to_next_right_cross(): # переходим в начало следующего правого
                                # крестика после покраски
    move_down(2)
    move_right(4)


@task(delay=0.04)
def task_2_2():
    go_to_start()
    for i in range(4):
        fill_cross()
        move_to_next_right_cross()
    fill_cross()
    move_left()


if __name__ == '__main__':
    run_tasks()
