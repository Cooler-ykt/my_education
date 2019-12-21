#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():

    while not cell_is_filled():
        move_up()

    while True:
            move_left(n=1)
            if cell_is_filled():
                break
            move_right(n=2)
            if cell_is_filled():
                break


if __name__ == '__main__':
    run_tasks()
