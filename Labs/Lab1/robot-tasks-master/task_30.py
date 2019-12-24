#!/usr/bin/python3

from pyrob.api import *


def measure_size():
    size = 1
    while not wall_is_on_the_right():
        move_right()
        size += 1
    return size


def fill_walls(size):  # старт покраски стен правый верхниий угол
    for i in range(size-2):
        move_down()
        fill_cell()
    move_down()

    for i in range(size-2):
        move_left()
        fill_cell()
    move_left()

    for i in range(size-2):
        move_up()
        fill_cell()
    move_up()

    for i in range(size-2):
        move_right()
        fill_cell()

    move_down()  # переход на старт внутреннего квадрата



def fill_square(size): # старт покраски правый угол, конец - центр квадрата
    for i in range(size,1,-2):
        fill_walls(i)


def run_home(size):
    for i in range(size,1,-2):
        move_down()
        move_left()


@task(delay=0.01)
def task_9_3():
    size = measure_size()
    fill_square(size)
    run_home(size)


if __name__ == '__main__':
    run_tasks()
