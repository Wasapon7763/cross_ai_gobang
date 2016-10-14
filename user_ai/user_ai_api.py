#!/usr/bin/env python
#-*- coding: utf-8 -*-

from game_sys_graphics import GobangGameSystem

class UserAi:
    def __init__(self, gamesys_obj):
        self.__gamesys = gamesys_obj

    def get_board(self):
        return self.__gamesys.get_board()

    def put_stone(self, x, y):
        color = self.__gamesys.cur_color
        self.__gamesys.put_stone(x, y, color)
