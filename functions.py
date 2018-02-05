# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:26:07 2018

@author: doug.lawrence
"""
from config import cfg_disp

# Conversion functions between pix and coords
def Coords_To_Pix(coordinates:tuple):
    x_coord, y_coord = coordinates
    x_pix = int(cfg_disp['width'] / 2 + x_coord * cfg_disp['mult'])
    y_pix = int(cfg_disp['height'] / 2 - y_coord * cfg_disp['mult'])
    return (x_pix, y_pix)


def Pix_To_Coords(pix:tuple):
    x_pix, y_pix = pix
    x_coord = (x_pix - cfg_disp['width'] / 2) / cfg_disp['mult']
    y_coord = (cfg_disp['height'] / 2 - y_pix) / cfg_disp['mult']
    return (x_coord, y_coord)
