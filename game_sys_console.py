#!/usr/bin/env python
#-*- coding: utf-8 -*-

class GobangGameSystem:
    GRID_NUM = 15
    BLACK = '●'
    WHITE = '○'
    SPACE = '･'

    def __init__(self):
        self.board = [[self.SPACE] * self.GRID_NUM for i in range(self.GRID_NUM)]

    def run_console(self):
        self.cur_color = self.BLACK
        game_set_flg = False

        while not game_set_flg:
            print(self.get_color_str(self.cur_color) + '\'s turn')
            self.print_board_console()

            while True:
                x, y = self.get_user_input_console()

                err_msg = self.validation(x, y)
                if err_msg == None:
                    self.board[x][y] = self.cur_color
                    break;
                else:
                    print(err_msg)

            win_msg = self.get_winner()
            if win_msg != None:
                print(win_msg)
                print('\n')
                self.print_board_console()
                game_set_flg = True

            if self.is_board_full():
                print("TIE")
                game_set_flg = True

            self.change_turns()

    def print_board_console(self):
        for y in range(0, self.GRID_NUM):
            print('%02d' % y, end = ' ')
            for x in range(0, self.GRID_NUM):
                print(self.board[x][y] + ' ', end = ' ')
            print('')

        print('  ', end = ' ')
        for x in range(0, self.GRID_NUM):
            print('%02d' % x, end = ' ')
        print('')

    def get_user_input_console(self):
        x = ''
        while x == '':
            x = input('x = ')
        y = ''
        while y == '':
            y = input('y = ')
        print('')
        return (int(x), int(y))

    def validation(self, x, y):
        if x not in range(0, self.GRID_NUM) or y not in range(0, self.GRID_NUM):
            return 'Error: Out of range'

        if self.board[x][y] == self.BLACK or self.board[x][y] == self.WHITE:
            return 'Error: Stone already exists in (' + str(x) + ', ' + str(y) + ')'

    def is_board_full(self):
        for y in range(0, self.GRID_NUM):
            for x in range (0, self.GRID_NUM):
                if self.board[x][y] == self.BLACK or self.board[x][y] == self.WHITE:
                    return False

        return True

    def get_winner(self):
        for y in range(0, self.GRID_NUM):
            for x in range(0, self.GRID_NUM):
                if self.check_for_five(x, y):
                    return self.get_color_str(self.board[x][y]) + ' WON'

        return None

    def check_for_five(self, x, y):
        if self.board[x][y] == self.SPACE:
            return False

        dx_list = [0, 1, 1]
        dy_list = [1, 0, 1]
        for (dx, dy) in zip(dx_list, dy_list):
            five_flg = True
            for i in range(5):
                if x + dx * i in range(0, self.GRID_NUM) and y + dy * i in range(0, self.GRID_NUM):
                    if self.board[x + dx * i][y + dy * i] != self.board[x][y]:
                        five_flg = False
                        break
            if five_flg == True:
                return True

        return False

    def change_turns(self):
        self.cur_color = self.WHITE if self.cur_color == self.BLACK else self.BLACK

    def get_color_str(self, stone):
        return 'BLACK' if stone == self.BLACK else 'WHITE'
