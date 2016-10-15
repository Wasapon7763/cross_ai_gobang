#!/usr/bin/env python
#-*- coding: utf-8 -*-

# import game_sys_console
# from game_sys_console import GobangGameSystem
import graphics
from graphics import GobangGraphics

if __name__ == '__main__':
    # gobang_game = GobangGameSystem()
    # gobang_game.run_console()
    graphics = GobangGraphics()
    while True:
        graphics.run_game()
