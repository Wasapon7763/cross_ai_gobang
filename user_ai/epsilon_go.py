import const
import random
from user_ai_api import UserAi

class EpsilonGo:
    def __init__(self, user_ai_api_obj):
        self.api_obj = user_ai_api_obj

    def put_stone(self):
        board = self.api_obj.get_board()
        mycol = self.api_obj.get_color()
        opcol = mycol * -1

        score = [[0] * const.GRID_NUM for i in range(const.GRID_NUM)]

        for y in range(const.GRID_NUM):
            for x in range(const.GRID_NUM):

                score[x][y] = abs(const.GRID_NUM / 2 - x) + abs(const.GRID_NUM / 2 - y)

                if board[x][y] == opcol:
                    score[x][y] = -1

        maxval = 0
        candidate = []
        for y in range(const.GRID_NUM):
            for x in range(const.GRID_NUM):
                if score[x][y] == maxval:
                    candidate.append([x, y])
                elif score[x][y] > maxval:
                    candidate = [[x, y]]
                    maxval = score[x][y]

        retx, rety = candidate[random.randint(0, len(candidate) - 1)]

        return (retx, rety)
