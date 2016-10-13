#!/usr/bin/env python
#-*- coding: utf-8 -*-

from game_sys_graphics import GobangGameSystem

class UserAi:
    def __init__(self, gamesys_obj):
        self.__gamesys = gamesys_obj

    def get_color(self):
        return self.__gamesys.cur_color

    def get_board(self):
        return self.__gamesys.get_board()
