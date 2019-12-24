from pyrob.api import *


def fill_cross(): # начинаем красить крестик снизу, заканчиваем сверху
    fill_cell()
    move_left()
    move_up()
    fill_cell()
    move_right()
    fill_cell()
    move_right()
    fill_cell()
    move_left()
    move_up()
    fill_cell()