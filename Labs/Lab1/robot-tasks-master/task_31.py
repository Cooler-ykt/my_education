#!/usr/bin/python3

from pyrob.api import *


def find_right_exit():
    if not wall_is_beneath():
        return True

    while wall_is_beneath() and not wall_is_on_the_right():
        move_right()
        if not wall_is_beneath():
            return True
    else:
        return False



def find_left_exit():
    if not wall_is_beneath():
        return True

    while wall_is_beneath() and not wall_is_on_the_left():
        move_left()
        if not wall_is_beneath():
            return True
    else:
        return False



def find_exit():
    if find_right_exit():
        return True
    elif find_left_exit():
        return True
    else:
        return False


@task(delay=0.031)
def task_8_30():
    while find_exit():
        while not wall_is_beneath():
            move_down()


if __name__ == '__main__':
    run_tasks()

