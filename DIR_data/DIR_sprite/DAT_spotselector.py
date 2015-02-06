#! /usr/bin/env python


# File Docstring
"""Sprite: Spot Selector

When playing the game, you can select
5 different spots. This is the animated
cursor that does that."""


# Import Modules
import __init__
import os
import pygame



# Sprite Class
class SPT_spotselector(pygame.sprite.Sprite):
     """The Spot Selector."""
     def __init__(self, spritesheet):
          """Initialize."""
          pygame.sprite.Sprite.__init__(self) # Initialize Sprite Module
          self.FrameList = spritesheet.Apply_Frames([(493, 219, 40, 40),
                                                     (534, 219, 40, 40)],
                                                    colorkey=(255, 0, 255))
          self.image = self.FrameList[1]
          self.rect = self.image.get_rect()
          self.IMAGE, self.RECT = self.image, self.rect

          self.SELECTED = False
          
          self.Frame = 0
          self.Pause = 0
          self.Delay = 10
          
          # Include other attributes for manipulation, animation, etc.
     def update(self):
          """Do a simple flicker."""
          self.Pause += 1
          if self.Pause >= self.Delay:
               self.Pause = 0
               self.Frame += 1
               if self.Frame >= len(self.FrameList):
                    self.Frame = 0
               self.image = self.FrameList[self.Frame]
