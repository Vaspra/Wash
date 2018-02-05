# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:33:07 2018

@author: cold-
"""

from config import cfg_disp, cfg_input, cfg_color
from functions import Pix_To_Coords, Coords_To_Pix
import pygame
from phys_object import Particle

class Run():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode(\
                        (cfg_disp['width'], cfg_disp['height']))
        pygame.display.set_caption(cfg_disp['caption'])
        
        self.obj_list = []
        self.exit = False
        self.gameLoop()
        pygame.quit()
        
        
    def gameLoop(self):
        while not self.exit:
            self.check_events()
            self.apply_input()
            for obj in self.obj_list:
                obj.update_physics()
            self.update_display()
            self.clock.tick(120)
            
        
    def check_events(self):
        cfg_input['mouse_x'], cfg_input['mouse_y'] = Pix_To_Coords((pygame.mouse.get_pos()))
        cfg_input['mouse_0'], cfg_input['mouse_1'], cfg_input['mouse_2'] =\
            pygame.mouse.get_pressed()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True
                print(event)
                
            elif event.type == pygame.KEYDOWN:
                if event.key in cfg_input.keys():
                    cfg_input[event.key] = True
                        
            elif event.type == pygame.KEYUP:
                if event.key in cfg_input.keys():
                    cfg_input[event.key] = False
                    
                    
    def apply_input(self):
        if cfg_input['mouse_0'] == True:
            new_obj = Particle( [(cfg_input['mouse_x'], cfg_input['mouse_y'])], self.obj_list)
            self.obj_list.append(new_obj)
            
        if cfg_input[pygame.K_RIGHT]:
            for obj in self.obj_list:
                obj.x_force += 0.001
                
        if cfg_input[pygame.K_LEFT]:
            for obj in self.obj_list:
                obj.x_force -= 0.001
                
        if cfg_input[pygame.K_UP]:
            for obj in self.obj_list:
                obj.y_force += 0.001
                
        if cfg_input[pygame.K_DOWN]:
            for obj in self.obj_list:
                obj.y_force -= 0.001
                
        if cfg_input[pygame.K_SPACE]:
            self.obj_list.clear()
            print('Clearing object list')
            

        
    def update_display(self):
        # Fill background
        self.display.fill(cfg_color['black'])
        
        # Other display features
        for obj in self.obj_list:
            pygame.draw.circle(self.display, (0, 230, 230), Coords_To_Pix(obj.points[0]), round(obj.radius))
        
        # Update display
        pygame.display.update()
        
        
run = Run()
                
                
                
                
                
                
                
                