#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import game_sys_graphics
from game_sys_graphics import GobangGameSystem
import const

from user_ai import *

class GobangGraphics:
    def run_game(self):
        self.gamesys = GobangGameSystem()
        self.gamesys.cur_color = const.BLACK

        pygame.init()
        self.screen = pygame.display.set_mode(const.SCR_RECT.size)
        pygame.display.set_caption('CROSS AI GOBANG')
        clock = pygame.time.Clock()

        self.black_stone_img = pygame.image.load('img/black_stone.png').convert_alpha()
        self.white_stone_img = pygame.image.load('img/white_stone.png').convert_alpha()
        self.bg_img = pygame.image.load('img/bg.png').convert()

        self.screen.fill((255, 255, 255))
        self.screen.blit(self.bg_img, (0, 0))
        self.draw_board()
        pygame.display.update()

        # load AI
        ai_api = user_ai_api.UserAi(self.gamesys)
        yota_ai = yotas_ai.Yotaisthebest(ai_api)
        yota_ai2 = yotas_ai.Yotaisthebest(ai_api)

        game_over_flg = False
        while True:
            clock.tick(30)
            # 

            # player black
            if self.gamesys.cur_color == const.BLACK:
                print("BLACK's turn!")
                coordx, coordy = yota_ai.put_stone()
                pygame.time.wait(100)

            # player white
            if self.gamesys.cur_color == const.WHITE:
                # print("WHITE's turn!")
                # coordx, coordy = yota_ai2.put_stone()
                
                event = pygame.event.wait()
                if event.type == const.MOUSEBUTTONUP and event.button == 1:
                    posx, posy = event.pos
                    coordx, coordy = self.get_coord_from_pos(posx, posy)

            if coordx != None and coordy != None:
                if self.gamesys.put_stone(coordx, coordy, self.gamesys.cur_color):
                    self.draw_stone(coordx, coordy, self.gamesys.cur_color)
                    if self.gamesys.get_winner() != None:
                        self.draw_win_text(self.gamesys.cur_color)
                        game_over_flg = True
                    self.gamesys.change_turns()
                pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == const.QUIT:
                    sys.exit()

            if game_over_flg:
                self.wait_for_click()
                sys.exit()

    def wait_for_click(self):
        while True:
            event = pygame.event.wait()
            if event.type == const.MOUSEBUTTONUP and event.button == 1:
                break
            if event.type == const.QUIT:
                sys.exit()

    def draw_win_text(self, color):
        sysfont = pygame.font.SysFont(None, 80)
        win_str = "WINNER " + self.gamesys.get_color_str(color)
        win_msg = sysfont.render(win_str, True, (255, 0, 0))
        size = sysfont.size(win_str)
        self.screen.blit(win_msg, (const.SCR_SIZE / 2 - size[0] / 2, const.SCR_SIZE / 2 - size[1] / 2))

    def draw_board(self):
        for i in range(0, const.GRID_NUM):
            point = const.BOARD_MARGIN + i * const.GRID_WIDTH
            pygame.draw.line(self.screen, (0, 0, 0), (point, const.BOARD_MARGIN), (point, const.SCR_SIZE - const.BOARD_MARGIN))
            pygame.draw.line(self.screen, (0, 0, 0), (const.BOARD_MARGIN, point), (const.SCR_SIZE - const.BOARD_MARGIN, point))

    def draw_stone(self, x, y, color):
        posx = const.BOARD_MARGIN + x * const.GRID_WIDTH
        posy = const.BOARD_MARGIN + y * const.GRID_WIDTH
        if color == const.BLACK:
            self.screen.blit(self.black_stone_img, (posx - const.STONE_RAD, posy - const.STONE_RAD))
        else:
            self.screen.blit(self.white_stone_img, (posx - const.STONE_RAD, posy - const.STONE_RAD))

    def get_coord_from_pos(self, posx, posy):
        coordx = -1
        coordy = -1

        for i in range(0, const.GRID_NUM):
            grid_coord = const.BOARD_MARGIN + i * const.GRID_WIDTH
            if posx in range(grid_coord - const.STONE_RAD, grid_coord + const.STONE_RAD):
                coordx = i
            if posy in range(grid_coord - const.STONE_RAD, grid_coord + const.STONE_RAD):
                coordy = i

            if coordx != -1 and coordy != -1:
                return (coordx, coordy)

        return (None, None)
