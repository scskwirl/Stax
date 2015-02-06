#! /usr/bin/env python


# File Docstring
"""Sprite: Token

The tokens that you have to clear in the game."""


# Import Modules
import __init__
import os
import pygame



# Sprite Class
class SPT_token(pygame.sprite.Sprite):
     """The Token Object."""
     # Color Dictionary ('Iden', (x, y, w, h), Score, )
     DIC_color = {'red': ('red', (1, 219, 40, 40), 1),
                  'orange': ('orange', (42, 219, 40, 40), 2),
                  'yellow': ('yellow', (83, 219, 40, 40), 5),
                  'green': ('green', (124, 219, 40, 40), 10),
                  'blue': ('blue', (165, 219, 40, 40), 20),
                  'purple': ('purple', (206, 219, 40, 40), 50),
                  'cyan': ('cyan', (247, 219, 40, 40), 100),
                  'magenta': ('magenta', (288, 219, 40, 40), 200),
                  'brown': ('brown', (329, 219, 40, 40), 500),
                  'gray': ('gray', (370, 219, 40, 40), 1000),
                  'black': ('black', (411, 219, 40, 40), 2000),
                  'white': ('white', (452, 219, 40, 40), 5000)}
     def __init__(self, spritesheet, color):
          """Initialize."""
          pygame.sprite.Sprite.__init__(self) # Initialize Sprite Module
          self.image = spritesheet.Apply_Graphic(SPT_token.DIC_color[color][1])
          self.rect = self.image.get_rect()
          self.IMAGE, self.RECT = self.image, self.rect

          self.IDEN = SPT_token.DIC_color[color][0]
          self.SCORE = SPT_token.DIC_color[color][2]
          
          self.CLEAR = False
          self.ALPHA = 255
          
     def update(self):
          """Update."""
          if self.CLEAR is True:
               self.ALPHA -= 10
               self.IMAGE.set_alpha(self.ALPHA, pygame.RLEACCEL)
               if self.ALPHA <= 0:
                    self.ALPHA = 0
