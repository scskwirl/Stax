#! /usr/bin/env python


# File Docstring
"""Chapter: Main Menu

The main menu chapter of the game."""


# Import Modules
import __init__
import sys

import pygame
from pygame.locals import *

# Import Game Data
from DIR_audio.DAT_loadaudio import *



# Chapter Class
class CHP_mainmenu:
     """The Main Menu."""
     def __init__(self):
          """Initialize and prepare the chapter."""
          # Put whatever details of the Chapter object you want here.
          pass

     def Start(self, screen, constant):
          """Start the chapter."""
          # Prepare any data before running the loop.
          
          pygame.event.get() # Purge the Input Queue.

          # Set Background
          bg = pygame.Surface(screen.RECT.size).convert()
          bg.fill((0, 127, 127))
          
          # Set Title
          IMG_title = constant['Spritesheet'].Apply_Graphic((1, 1, 600, 217),
                                                            colorkey=(255, 0, 255))
          RCT_title = IMG_title.get_rect()
          RCT_title.midtop = screen.RECT.midtop
          RCT_title = RCT_title.move((0, 50))

          # Set Copyright Notice
          COPYRIGHT = constant['Font'].render('Copyright \xa9 2010 Santo Ciaravino',
                                              True,
                                              (0, 0, 0))
          RCT_COPYRIGHT = COPYRIGHT.get_rect()
          RCT_COPYRIGHT.midbottom = screen.RECT.midbottom


          # Set Up Options
          CHC = [[constant['BigFont'].render("Start Game", True,
                                                (255, 255, 255)),
                  constant['BigFont'].render("Start Game", True,
                                                (255, 255, 255), (0, 0, 0))],
                 [constant['BigFont'].render("Quit", True,
                                                (255, 255, 255)),
                  constant['BigFont'].render("Quit", True,
                                                (255, 255, 255), (0, 0, 0))]]
          # Position Start Rect
          RCT_start = CHC[0][1].get_rect()
          RCT_start.midtop = RCT_title.midbottom
          RCT_start = RCT_start.move((0, 90))
          CHC[0].append(RCT_start)
          # Position Quit Rect
          RCT_quit = CHC[1][1].get_rect()
          RCT_quit.midtop = RCT_title.midbottom
          RCT_quit = RCT_quit.move((0, 125))
          CHC[1].append(RCT_quit)

          # High Score
          HS = constant['Font'].render("High Score: %s" % constant['HighScore'], True,
                                       (255, 255, 255))
          RCT_HS = HS.get_rect()
          RCT_HS.midtop = RCT_quit.midbottom
          RCT_HS = RCT_HS.move(0, 50)

          # Music
          MUS_Title = Load_Music('MUS_Title.ogg')
          pygame.mixer.music.play(-1)
          

          CHOICE = 0
          # Main Loop
          LS = True # Loop Switch
          while LS:
               constant['Clock'].tick(60) # Clock 60 Frames Per Second
               
               # Event Catch
               for EVT in pygame.event.get():
                    if EVT.type == QUIT:
                         pygame.quit()
                         sys.exit() # Hard Exit
                    elif EVT.type == KEYDOWN:
                         if EVT.key == K_ESCAPE:
                              return 1 # Soft Exit
                         elif EVT.key == K_SPACE or EVT.key == K_RETURN:
                              return CHOICE
                         elif EVT.key == K_UP:
                              CHOICE -= 1
                              if CHOICE <= 0:
                                   CHOICE = 0
                         elif EVT.key == K_DOWN:
                              CHOICE += 1
                              if CHOICE >= 1:
                                   CHOICE = 1
                         else:
                              pass

               
               # Update Data
               screen.FRAME.blit(bg, screen.RECT.topleft)
               screen.FRAME.blit(IMG_title, RCT_title.topleft)
               screen.FRAME.blit(COPYRIGHT, RCT_COPYRIGHT.topleft)
               for choice in range(0, len(CHC)):
                    if choice == CHOICE:
                         screen.FRAME.blit(CHC[choice][1], CHC[choice][2])
                    screen.FRAME.blit(CHC[choice][0], CHC[choice][2])
                    
               screen.FRAME.blit(HS, RCT_HS.topleft)
          
               # Update Screen
               screen.Update()
