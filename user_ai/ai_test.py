import const
from user_ai_api import UserAi

class AiTest:
    def __init__(self, user_ai_api_obj):
        self.api_obj = user_ai_api_obj

    def put_stone(self):
        board = self.api_obj.get_board()
        score=[[0 for i in range(const.GRID_NUM)] for i in range(const.GRID_NUM)]

        for y in range(0, const.GRID_NUM):
            for x in range(0, const.GRID_NUM):
                score[x][y]-=abs(const.GRID_NUM/2-x)+abs(const.GRID_NUM/2-y)
                #if board[x][y] == const.SPACE:
                #    return (x, y)
        max_score=score[0][0]
        rx=0
        ry=0
        for y in range(0, const.GRID_NUM):
            for x in range(0, const.GRID_NUM):
                if(score[x][y]>=max_score and board[x][y]==const.SPACE):
                    max_score=score[x][y]
                    rx=x
                    ry=y
        return (rx,ry)



