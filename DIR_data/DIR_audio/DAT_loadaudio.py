#! /usr/bin/env python


# File Docstring
"""LoadAudio Data

This module holds the audio-loading objects
to create sound and music for the game."""


# Import Modules
import __init__
import os
import pygame.mixer



# Load Sound
def Load_Sound(filename):
    """Returns a Sound object."""
    class NoneSound:
        """A "Dummy" Sound Effect if a sound could not be loaded."""
        def play(self):
            """Do nothing, in place of playing sound."""
            pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    filepath = os.path.join('DIR_data', 'DIR_audio', filename) # Create the filepath.
    try: sound = pygame.mixer.Sound(filepath) # Apply the new Sound file.
    except pygame.error, message: # If there is an error...
        print "ERROR - Cannot load Sound file:", filepath # Notify which file.
        raise SystemExit, message # Exit
    return sound # Return the sound data.

# Load Music
def Load_Music(filename):
    """Returns a Music object."""
    class NoneMusic:
        """A "Dummy" Song if a song could not be loaded."""
        def play(self):
            """Do nothing, in place of playing sound."""
            pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneMusic()
    filepath = os.path.join('DIR_data', 'DIR_audio', filename) # Create the filepath.
    try: sound = pygame.mixer.music.load(filepath) # Apply the new Sound file.
    except pygame.error, message: # If there is an error...
        print "ERROR - Cannot load Music file:", filepath # Notify which file.
        raise SystemExit, message # Exit
    return sound # Return the sound data.

