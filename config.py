# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:33:42 2018

@author: cold-
"""
import pygame

cfg_disp = {'width':            800,
            'height':           200,
            'mult':             60,
            'caption':          'Kek'}


cfg_walls = {'xLow':            (-cfg_disp['width'] / 2) / cfg_disp['mult'],
            'xHigh':            (cfg_disp['width'] / 2) / cfg_disp['mult'],
            'yLow' :            (-cfg_disp['height'] / 2) / cfg_disp['mult'],
            'yHigh':            (cfg_disp['height'] / 2) / cfg_disp['mult']}


cfg_input = {pygame.K_UP:       False,
             pygame.K_DOWN:     False,
             pygame.K_LEFT:     False,
             pygame.K_RIGHT:    False,
             
             pygame.K_SPACE:    False,
             
             'mouse_x':         0,
             'mouse_y':         0,
             'mouse_0':         False,
             'mouse_1':         False,
             'mouse_2':         False}


cfg_color = {'black':           (20,20,20),
              'white':          (235,235,235),
              'red':            (230,0,0),
              'green':          (0,230,0),
              'blue':           (0,0,230)}