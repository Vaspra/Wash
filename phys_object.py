# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:11:48 2018

@author: doug.lawrence
"""

from config import cfg_walls

class Particle():
    def __init__(self, points:list, obj_list:list):
        self.points = points
        self.obj_list = obj_list
        
        self.x_speed = 0
        self.x_accel = 0
        self.x_force = 0
        
        self.y_speed = 0
        self.y_accel = 0
        self.y_force = 0
                
        self.speedLim = 2
        
        self.radius = 0
        self.mass = 0
        self.add_mass(1)
        
        
    def update_physics(self):
        self._apply_speedLim(self.speedLim)
        self._apply_forces()
        self._apply_accels()
        self._apply_speeds()
        self._check_walls('custom')
        
        
    def add_mass(self, mass_to_add):
        self.mass += mass_to_add
        self.radius = self.mass**(1/3) * 5
        
        
    def _apply_speedLim(self, speedLim):
        if abs(self.x_speed) > speedLim:
            self.x_speed / abs(self.x_speed) * speedLim
        if abs(self.y_speed) > speedLim:
            self.y_speed / abs(self.y_speed) * speedLim
            
            
    def _apply_forces(self):
        self.x_accel = self.x_force / self.mass
        self.y_accel = self.y_force / self.mass
        self.x_force = 0
        self.y_force = 0
        
        
    def _apply_accels(self):
        self.x_speed += self.x_accel
        self.y_speed += self.y_accel
        
        
    def _apply_speeds(self):
        self.move_points((self.x_speed, self.y_speed))
        
        
    def move_points(self, vector:tuple):
        dx, dy = vector
        for i in range(len(self.points)):
            point = self.points[i]
            x, y = point
            new_point = (x + dx, y + dy)
            self.points[i] = new_point
            
            
    def _check_walls(self, wall_type):
        wall_type_list = ['teleport', 'leave', 'bounce', 'custom']
        if wall_type not in wall_type_list:
            print('check_walls(wall_type) using invalid wall_type: \'%s\'\n\
                  use a type from the list: %s' % (wall_type, str(wall_type_list)))
                    
        for point in self.points:
            x, y = point
            if wall_type == 'bounce':
                if x < cfg_walls['xLow']:
                    dx = cfg_walls['xLow'] - x 
                    self.move_points((dx, 0))
                    self.x_speed *= -1
                elif x > cfg_walls['xHigh']:
                    dx = cfg_walls['xHigh'] - x
                    self.move_points((dx, 0))
                    self.x_speed *= -1
                
                if y < cfg_walls['yLow']:
                    dy = cfg_walls['yLow'] - y
                    self.move_points((0, dy))
                    self.y_speed *= -1
                elif y > cfg_walls['yHigh']:
                    dy = cfg_walls['yHigh'] - y
                    self.move_points((0, dy))
                    self.y_speed *= -1
                    
            elif wall_type == 'teleport':
                pass
            
            elif wall_type == 'leave':
                if x < cfg_walls['xLow'] or x > cfg_walls['xHigh']\
                or y < cfg_walls['yLow'] or y > cfg_walls['yHigh']:
                    self.obj_list.remove(self)
                    break
            
            elif wall_type == 'custom':
                # Bouncing ceiling, teleporting sides
                if x < cfg_walls['xLow']:
                    self.move_points((cfg_walls['xHigh'] - cfg_walls['xLow'], 0))
                elif x > cfg_walls['xHigh']:
                    self.move_points((cfg_walls['xLow'] - cfg_walls['xHigh'], 0))
                    
                if y < cfg_walls['yLow']:
                    dy = cfg_walls['yLow'] - y
                    self.move_points((0, dy))
                    self.y_speed *= -1
                elif y > cfg_walls['yHigh']:
                    dy = cfg_walls['yHigh'] - y
                    self.move_points((0, dy))
                    self.y_speed *= -1
                    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        