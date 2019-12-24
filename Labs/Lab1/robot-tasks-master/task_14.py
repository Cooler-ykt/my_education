#!/usr/bin/python3

from pyrob.api import *

def init_global_params():
    global lenth_of_corridor, \
           exit_to_up_cell, from_up_enter_cell, \
           exit_to_down_cell, from_down_enter_cell
    from_up_enter_cell = 0
    exit_to_up_cell = 0
    from_down_enter_cell = 0
    exit_to_down_cell = 0
    lenth_of_corridor = 1

def find_from_up_enter():
    global from_up_enter_cell, lenth_of_corridor
    if not wall_is_above():
        if from_up_enter_cell == 0:
            from_up_enter_cell = lenth_of_corridor


def find_exit_to_up():
    global exit_to_up_cell, lenth_of_corridor
    if not wall_is_above():
        exit_to_up_cell = lenth_of_corridor


def find_exit_to_down():
    global exit_to_down_cell, lenth_of_corridor
    if not wall_is_beneath():
        if exit_to_down_cell == 0:
            exit_to_down_cell = lenth_of_corridor


def find_fom_down_enter():
    global from_down_enter_cell, lenth_of_corridor
    if not wall_is_beneath():
        from_down_enter_cell = lenth_of_corridor



def explore_and_paint_corridor():
    """ ротбот закрашивает клетки в корридоре, измеряет длину и ищет вход и
    выход в корридор сверху и снизу, первая клетка в которой нет стены
    сверху будет входом в корридор сверху, последняя клетка в которой
    нет стены сверху будет выходом из корридора вверх, для низа
    наоборот первая выход из корридора вниз, последняя вход снизу"""
    global lenth_of_corridor
    while not wall_is_on_the_right():
        find_from_up_enter()
        find_exit_to_up()
        find_exit_to_down()
        find_fom_down_enter()
        if wall_is_above() and wall_is_beneath():
            fill_cell()
        lenth_of_corridor += 1
        move_right()
    else:
        find_from_up_enter()
        find_exit_to_up()
        find_exit_to_down()
        find_fom_down_enter()
        if wall_is_above() and wall_is_beneath():
            fill_cell()


def exit_to_up():
    global exit_to_up_cell, lenth_of_corridor
    if exit_to_up_cell == 0:
        return False  # Либо выход наверх из корридора еще не найден,
                      # либо наверх выхода нет
    else:
        for i in range(lenth_of_corridor - exit_to_up_cell):
            move_left()
        move_up()
        return True


def paint_up():
    """робот красит верхние клетки и заходит в коридор на последней"""
    global from_up_enter_cell, exit_to_up_cell
    for i in range(exit_to_up_cell - from_up_enter_cell):
        if not wall_is_beneath():
            fill_cell()
        move_left()
    fill_cell()
    move_down()



def exit_to_down():
    global exit_to_down_cell, from_up_enter_cell, lenth_of_corridor
    if exit_to_down_cell == 0:
        return False  # Либо выход вниз из корридора еще не найден,
                      # либо вниз выхода нет
    else:
        if from_up_enter_cell == 0:  # на случай когда наверх выхода
                                     # нет
            move_left(lenth_of_corridor - exit_to_down_cell)
            move_down()
        elif from_up_enter_cell > exit_to_down_cell:
            move_left(from_up_enter_cell - exit_to_down_cell)
            move_down()
        elif from_up_enter_cell < exit_to_down_cell:
            move_right(exit_to_down_cell - from_up_enter_cell)
            move_down()
        else:
            move_down()

        return True



def pait_down():
    """робот красит нижние клетки и заходит в коридор на последней"""
    global from_down_enter_cell, exit_to_down_cell
    for i in range(from_down_enter_cell - exit_to_down_cell):
        if not wall_is_above():
            fill_cell()
        move_right()
    fill_cell()
    move_up()

def run_home():
    """ротбот бежит по коридору пока не упрется в стену"""
    while not wall_is_on_the_right():
        move_right()



def paint_out_cells():
    #global lenth_of_corridor, exit_to_up_cell, from_up_enter_cell, \
    # exit_to_down_cell, from_down_enter_cell
    """ ротбот бежит назад до выхода вверх, выходит из корридора и
    бежит до входа по пути закрашивая клетки, входит в корридор, затем
    бежит до выхода вниз, проделывает то же самое внизу, и бежит в
    конец корридора или попростому красит клетки против часовой стрелки,
    если выход не найден при исследовании коридора то красить не надо """
    if exit_to_up():
        paint_up()
    if exit_to_down():
        pait_down()
    run_home()



@task(delay=0.04)
def task_8_11():
    init_global_params()
    explore_and_paint_corridor()
    #print(lenth_of_corridor, from_up_enter_cell, exit_to_up_cell, \
    # exit_to_down_cell, from_down_enter_cell)
    paint_out_cells()

if __name__ == '__main__':
    run_tasks()
