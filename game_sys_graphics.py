#!/usr/bin/env python
#-*- coding: utf-8 -*-
import const

class GobangGameSystem:
    def __init__(self):
        self.board = [[const.SPACE] * const.GRID_NUM for i in range(const.GRID_NUM)]

    def put_stone(self, x, y, color):
        if self.__is_valid(x, y):
            self.board[x][y] = color
            return True
        else:
            return False

    def get_board(self):
        return self.board

    def is_board_full(self):
        for y in range(0, const.GRID_NUM):
            for x in range (0, const.GRID_NUM):
                if self.board[x][y] == const.BLACK or self.board[x][y] == const.WHITE:
                    return False

        return True

    def get_winner(self):
        for y in range(0, const.GRID_NUM):
            for x in range(0, const.GRID_NUM):
                if self.check_for_five(x, y):
                    return self.board[x][y]

        return None

    def check_for_five(self, x, y):
        if self.board[x][y] == const.SPACE:
            return False

        dx_list = [0, 1, 1, -1]
        dy_list = [1, 0, 1, 1]
        for (dx, dy) in zip(dx_list, dy_list):
            five_flg = True
            for i in range(5):
                if x + dx * i in range(0, const.GRID_NUM) and y + dy * i in range(0, const.GRID_NUM):
                    if self.board[x + dx * i][y + dy * i] != self.board[x][y]:
                        five_flg = False
                        break
                else:
                    five_flg = False
            if five_flg == True:
                return True

        return False

    def change_turns(self):
        self.cur_color = const.WHITE if self.cur_color == const.BLACK else const.BLACK

    def get_color_str(self, stone):
        return 'BLACK' if stone == const.BLACK else 'WHITE'

    def __is_valid(self, x, y):
        if x not in range(0, const.GRID_NUM) or y not in range(0, const.GRID_NUM):
            return False

        if self.board[x][y] == const.BLACK or self.board[x][y] == const.WHITE:
            return False

        return True
