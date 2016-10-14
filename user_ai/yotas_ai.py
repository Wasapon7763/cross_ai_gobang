import const
from user_ai.user_ai_api import UserAi
from user_ai.yota import *
class Yotaisthebest:

    def __init__(self, user_ai_api_obj):
        self.api_obj = user_ai_api_obj
    def neg(self,l):
    	inv=[[0 for i in range(len(l))]for i in range(len(l[0]))]
    	for i in range(len(l)):
        	for j in range(len(l[0])):
        		inv[i][j]=-1*l[i][j]
    	return inv

    def put_stone(self):
        board = self.api_obj.get_board()
        turn=1
        for i in board:
        	for j in i:
        		if(j!=const.SPACE):
        			turn=turn*-1
        if(turn==-1):
        	return yota(neg(board))
        else:
        	return yota(board)
       



