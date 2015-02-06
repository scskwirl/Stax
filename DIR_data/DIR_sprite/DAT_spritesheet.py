#! /usr/bin/env python


# File Docstring
"""Spritesheet Data

This module contains the Spritesheet() object
to create a source for sprite displays. For
best results, use .png files, as they can use
alpha channels."""


# Import Modules
import __init__
import os
import pygame



# Spritesheet Class
class Spritesheet:
    """A Spritesheet object used to contain and manage sprite images."""
    def __init__(self, filename='IMG_mainsheet.png'):
        """Initialize the Spritesheet object."""
        self.SHEET = pygame.image.load(os.path.join('DIR_data', 'DIR_sprite', filename)).convert()

    def Set_Colorkey(self, image, colorkey=None):
        """Set a colorkey for transparency."""
        if colorkey is not None: # If there is a colorkey used...
            if colorkey is -1: # If the flag is -1...
                colorkey = image.get_at((0, 0)) # Get the topleft pixel color.
            image.set_colorkey(colorkey, pygame.RLEACCEL) # Apply the colorkey
        return image # Return the image data.
    

    def Apply_Graphic(self, rect, colorkey=None):
        """Cut a section of the spritesheet to apply a sprite graphic."""
        cut_rect = pygame.Rect(rect) # Set the size of the rect to cut out the graphic.
        graphic = None
        graphic = pygame.Surface(cut_rect.size).convert()
        graphic.blit(self.SHEET, (0, 0), cut_rect) # Draw the graphic on the new surface.
        graphic = self.Set_Colorkey(graphic, colorkey)
        return graphic # Return the graphic.
    
    def Apply_Frames(self, rect_list, colorkey=None):
        """Return a list of graphics to use for frames."""
        frames = [] # An empty list to hold the frames.
        for rect in rect_list: frames.append(self.Apply_Graphic(rect, colorkey))
        # For every rect provided, append that graphic to the frame list.
        return frames # Return the frame list.
