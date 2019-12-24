#!/usr/bin/python3

from pyrob.api import *


def find_exit(): # робот ищет выход в стене сверху так же может выйти и с торцов если там есть выход

    while not wall_is_on_the_left():  # робот ищет выход при движении на лево
        if not wall_is_above():
            return True
        else: move_left()

    while not wall_is_on_the_right():  # робот ищет выход при движении на право
        if not wall_is_above():
            return True
        else: move_right()
    else:
        if not wall_is_above():
            return True

    return False # сверху и торцов выхода нет


def run_home():
    while not wall_is_above():
        move_up()
    else:
        while not wall_is_on_the_left():
            move_left()


@task(delay=0.04)
def task_8_29():
    if find_exit():
       run_home()



if __name__ == '__main__':
    run_tasks()
