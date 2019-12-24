#!/usr/bin/python3

from pyrob.api import *
from fill_figure import *


def move_to_next_right_cross():  # переходим в начало следующего правого
                                 # крестика после покраски,

    for i in range(4):
        if not wall_is_on_the_right():
            move_right()
        else:
            return False
    move_down(2)
    return True




def fill_row_of_10_cross(): # красим ряд из 10 крестиков и возвращаемся
                            # на исходную

    move_down(2)
    move_right()

    for i in range(9):
        fill_cross()
        move_to_next_right_cross()
    fill_cross()
    move_left(37)

def fill_row_of_cross(): # красим ряд крестиков из любого количества
                        # крестиков и возвращаемся на исходную
    move_down(2)
    move_right()

    fill_cross()
    while move_to_next_right_cross():
        fill_cross()
    else:
        while not wall_is_on_the_left():
            move_left()


@task(delay=0.02)
def task_2_4():
    for i in range(4):
        #fill_row_of_10_cross()
        fill_row_of_cross()
        move_down(4)
    fill_row_of_10_cross()

if __name__ == '__main__':
    run_tasks()
