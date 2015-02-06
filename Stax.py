#! /usr/bin/env python

# File Docstring
"""STAX
Copyright (c) 2010 by Santo Ciaravino"""
print __doc__
print


# Initialize Psyco
try:
    import psyco
    psyco.full()
except ImportError:
    print "NOTICE: 'Psyco' could not be initialized!"


# Import Python Standard Libraries
import __init__ # Directory Import
import os # Operating System
import sys # Python System
import random # Random Generator

# Import Pygame & Other Libraries
import wx
import pygame
from pygame.locals import *


# Import Game Data
from DIR_data.DAT_mainmenu import CHP_mainmenu
from DIR_data.DAT_gamesettings import CHP_gamesettings
from DIR_data.DAT_game import CHP_game

from DIR_data.DIR_sprite.DAT_spritesheet import Spritesheet


# Display Object
class DISPLAY:
    """The Display Window Object."""
    def __init__(self, # Object Instance
                 resolution=(800, 600), # Display Default Resolution
                 disp_sets=0, # Display Default Video Settings
                 title='STAX: Action Puzzle Game', # Display Default Title
                 icon=('DIR_data\\disp_icon.ico', # Display Default Icon
                       (255, 0, 255)), # Icon Transparency Colorkey (R, G, B)
                 mouse_vis=False): # Default Mouse Visibility
                 
        
        """Initializes the Display."""
        # Single Instance Checker
        self.app_iden = "APP IDEN - %s" % wx.GetUserId()
        self.instance = wx.SingleInstanceChecker(self.app_iden)
        if(self.instance.IsAnotherRunning()): sys.exit()

        # Screen Attributes
        self.RESOLUTION = resolution
        self.DISP_SETS = disp_sets
        self.TITLE = title
        self.ICON = icon
        self.MOUSE_VIS = mouse_vis

        # Screen Methods
        self.Set_Caption = pygame.display.set_caption
        self.Set_Icon = pygame.display.set_icon
        self.Set_Mouse_Vis = pygame.mouse.set_visible
        self.Set_Mode = pygame.display.set_mode

        # Start The Display
        self.Set_Caption(self.TITLE) # Set Title
        try:
            self.Set_Icon(self.Icon_Data(self.ICON[0], self.ICON[1])) # Set Icon
        except:
            pass
        self.Set_Mouse_Vis(self.MOUSE_VIS) # Set Mouse Visibility
        self.FRAME = self.Set_Mode(self.RESOLUTION, self.DISP_SETS) # Activate Display
        self.SURFACE = pygame.display.get_surface() # Get Frame Surface
        self.RECT = self.FRAME.get_rect() # Get Frame Rect
        
    # Local Method to prepare icon data in initialization.
    def Icon_Data(self, icon_name, colorkey):
        """Prepares an icon to use on the Display window."""
        Icon_Image = pygame.image.load(icon_name) # Icon Image (Surface)
        Icon_Done = pygame.Surface((32, 32)) # New Surface
        Icon_Done.set_colorkey(colorkey) # Transparency Colorkey
        for X in range(0, 32): # X Coordinate Pixels
            for Y in range(0, 32): # Y Coordinate Pixels
                Icon_Done.set_at((X, Y), Icon_Image.get_at((X, Y))) # Transfer Pixels
        return Icon_Done # Return Value


    # Screen Methods (for in-game use)
    def Update(self):
        pygame.display.update()

    def Flush_Buffer(self, color=(0, 0, 0)):
        """Flushes the back buffer with a blank surface."""
        SFC_flush = pygame.Surface(self.RESOLUTION).convert()
        SFC_flush.fill(color)
        self.FRAME.blit(SFC_flush, (0, 0))





# Start Game
if __name__ == "__main__":
    # Initialize Game Data
    pygame.init() # Set Pygame
    os.environ['SDL_VIDEO_CENTERED'] = '1' # Center all displays.
    

    # Splash Screen
    IMG_splash = pygame.image.load('DIR_data\\splashscreen.png')
    RCT_splash = IMG_splash.get_rect()
    Splash = pygame.display.set_mode(RCT_splash.size, NOFRAME)
    pygame.mouse.set_visible(False) # This line is optional.
    Splash.blit(IMG_splash, (0, 0))
    pygame.display.update()
    # Choose either wait(milliseconds) or delay(milliseconds), and remove the other.
    pygame.time.wait(2000) # Use this to 'wait' a specific amount of time.
    # Actually it doesn't matter. They do the same thing. Still good to keep consistent.
    pygame.display.quit()
    
    # Activate Display
    pygame.display.init() # Re-initialize the Pygame Display module.
    SCREEN = DISPLAY() # Make a new DISPLAY.

    # Prepare Constants
    GameConstant = {'Clock': pygame.time.Clock(),
                    'Spritesheet': Spritesheet(),
                    'Font': pygame.font.Font(None, 20),
                    'BigFont': pygame.font.SysFont(None, 40),
                    'HighScore': 0}
    

    # Main Loop
    MLS = True # Main Loop Switch
    while MLS:
        # Purge Input Queue
        pygame.event.get()

        # Main Menu Object & Start
        MainMenu = CHP_mainmenu()
        GameSettings = CHP_gamesettings()
        
        RESULT = MainMenu.Start(SCREEN, GameConstant)
        if RESULT is 1:
            MLS = False
        elif RESULT is 0:
            GameLoop = True
            while GameLoop:
                StartParams = GameSettings.Start(SCREEN, GameConstant)
                if StartParams != 'BREAK':
                    Game = CHP_game(StartParams)
                    GAME = Game.Start(SCREEN, GameConstant)
                elif StartParams == 'BREAK':
                    GameLoop = False
        else:
            pass
