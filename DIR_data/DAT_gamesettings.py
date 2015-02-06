#! /usr/bin/env python


# File Docstring
"""Chapter: Start

When you start the game, this sets
your game's parameters before starting."""


# Import Modules
import __init__
import sys
import random
import pygame
from pygame.locals import *

# Import Game Data
from DIR_audio.DAT_loadaudio import *


# Chapter Class
class CHP_gamesettings:
     """Chapter that starts the game."""
     def __init__(self):
          """Initialize and prepare the chapter."""
          # Put whatever details of the Chapter object you want here.
          self.Color = [(1, 219, 40, 40),
                        (42, 219, 40, 40),
                        (83, 219, 40, 40),
                        (124, 219, 40, 40),
                        (165, 219, 40, 40),
                        (206, 219, 40, 40),
                        (247, 219, 40, 40),
                        (288, 219, 40, 40),
                        (329, 219, 40, 40),
                        (370, 219, 40, 40),
                        (411, 219, 40, 40),
                        (452, 219, 40, 40)]

     def Start(self, screen, constant):
          """Start the chapter."""
          # Prepare any data before running the loop.
          
          pygame.event.get() # Purge the Input Queue.
          
          random.seed()

          bg = pygame.Surface(screen.RECT.size).convert()
          bg.fill((0, 0, 0))
          
          HEADER = constant['BigFont'].render("GAME SETTINGS", True,
                                              (255, 255, 255))
          RCT_HEADER = HEADER.get_rect()
          RCT_HEADER.midtop = bg.get_rect().midtop
          RCT_HEADER = RCT_HEADER.move((0, 20))
          bg.blit(HEADER, RCT_HEADER.topleft)

          # Apply the tokens to the side of the screen.
          for tilestep in range(0, 15):
               # Choose the colors.
               LEFT_color = random.choice(self.Color)
               RIGHT_color = random.choice(self.Color)
               # Apply the colors.
               LEFT_tile = constant['Spritesheet'].Apply_Graphic(LEFT_color)
               RIGHT_tile = constant['Spritesheet'].Apply_Graphic(RIGHT_color)
               # Get two rects from the graphic.
               RCT_LEFT_tile = LEFT_tile.get_rect()
               RCT_LEFT_tile.topleft = bg.get_rect().topleft
               RCT_LEFT_tile = RCT_LEFT_tile.move(0, tilestep*40)
               RCT_RIGHT_tile = RIGHT_tile.get_rect()
               RCT_RIGHT_tile.topright = bg.get_rect().topright
               RCT_RIGHT_tile = RCT_RIGHT_tile.move(0, tilestep*40)
               # Blit them.
               bg.blit(LEFT_tile, RCT_LEFT_tile.topleft)
               bg.blit(RIGHT_tile, RCT_RIGHT_tile.topleft)

          # Put Instructional Messages on the bottom of the screen.
          Escape = constant['Font'].render("Press ESC to return.", True,
                                           (255, 255, 255))
          RCT_Escape = Escape.get_rect()
          RCT_Escape.midbottom = screen.RECT.midbottom
          bg.blit(Escape, RCT_Escape.topleft)
          Begin = constant['Font'].render("Press ENTER or SPACE to begin.", True,
                                          (255, 255, 255))
          RCT_Begin = Begin.get_rect()
          RCT_Begin.midbottom = RCT_Escape.midtop
          bg.blit(Begin, RCT_Begin.topleft)

          # Token Select (6-10 pieces)
          RCT_Token_Container = pygame.Rect((0, 0), (400, 40))
          RCT_Token_Container.midtop = RCT_HEADER.midbottom
          RCT_Token_Container = RCT_Token_Container.move(0, 40)
          TokenCount = constant['Font'].render("Token Count:", True,
                                               (255, 255, 255))
          RCT_TokenCount = TokenCount.get_rect()
          RCT_TokenCount.midright = RCT_Token_Container.midleft
          bg.blit(TokenCount, RCT_TokenCount.topleft)
          
          # Special Token Select (None, Wild, Flash, Both)
          RCT_SpecialToken_Container = pygame.Rect((0, 0), (80, 40))
          RCT_SpecialToken_Container.midtop = RCT_Token_Container.midbottom
          RCT_SpecialToken_Container = RCT_SpecialToken_Container.move(0, 40)
          SpecialTokens = constant['Font'].render("Special Tokens:", True,
                                               (255, 255, 255))
          RCT_SpecialTokens = SpecialTokens.get_rect()
          RCT_SpecialTokens.midright = RCT_SpecialToken_Container.midleft
          RCT_SpecialTokens.left = RCT_TokenCount.left
          bg.blit(SpecialTokens, RCT_SpecialTokens.topleft)
          CaptionMessage = ['None', 'Wild Token', 'Flash Token', 'Both']
                    
          # Timer
          Time = constant['Font'].render("X Ticks", True, (0, 0, 0))
          RCT_Time = Time.get_rect()
          RCT_Time.midtop = RCT_SpecialToken_Container.midbottom
          RCT_Time = RCT_Time.move(0, 60)
          
          Timer = constant['Font'].render("Timer:", True,
                                          (255, 255, 255))
          RCT_Timer = Timer.get_rect()
          RCT_Timer.midleft = RCT_TokenCount.midleft
          RCT_Timer.centery = RCT_Time.centery
          bg.blit(Timer, RCT_Timer.topleft)
          
          # Random Drop Count (1-5 random pieces)
          RDC = constant['Font'].render("X Tokens", True, (0, 0, 0))
          RCT_RDC = RDC.get_rect()
          RCT_RDC.midtop = RCT_Time.midbottom
          RCT_RDC.left = RCT_Time.left
          RCT_RDC = RCT_RDC.move(0, 40)
          
          RandomDrop = constant['Font'].render("Random Drop Count:", True,
                                          (255, 255, 255))
          RCT_RandomDrop = RandomDrop.get_rect()
          RCT_RandomDrop.midleft = RCT_TokenCount.midleft
          RCT_RandomDrop.centery = RCT_RDC.centery
          bg.blit(RandomDrop, RCT_RandomDrop.topleft)
          
          # Height (2, 4, or 6)
          HeightCount = constant['Font'].render("X Blocks", True, (0, 0, 0))
          RCT_HeightCount = HeightCount.get_rect()
          RCT_HeightCount.midtop = RCT_RDC.midbottom
          RCT_HeightCount.left = RCT_RDC.left
          RCT_HeightCount = RCT_HeightCount.move(0, 40)

          Height = constant['Font'].render("Starting Height:", True,
                                           (255, 255, 255))
          RCT_Height = Height.get_rect()
          RCT_Height.midleft = RCT_TokenCount.midleft
          RCT_Height.centery = RCT_HeightCount.centery
          bg.blit(Height, RCT_Height.topleft)
          
          # Music (OFF, BRIX, BLOX)
          RCT_SongContainer = pygame.Rect((0, 0), (200, 40))
          RCT_SongContainer.midtop = RCT_HeightCount.midbottom
          RCT_SongContainer = RCT_SongContainer.move(0, 40)
          
          OFF = constant['Font'].render("OFF", True, (255, 255, 255))
          RCT_OFF = OFF.get_rect()
          RCT_OFF.midleft = RCT_SongContainer.midleft
          bg.blit(OFF, RCT_OFF.topleft)
          
          BRIX = constant['Font'].render("BRIX", True, (255, 255, 255))
          RCT_BRIX = BRIX.get_rect()
          RCT_BRIX.center = RCT_SongContainer.center
          bg.blit(BRIX, RCT_BRIX.topleft)
          
          BLOX = constant['Font'].render("BLOX", True, (255, 255, 255))
          RCT_BLOX = BLOX.get_rect()
          RCT_BLOX.midright = RCT_SongContainer.midright
          bg.blit(BLOX, RCT_BLOX.topleft)

          Song = constant['Font'].render("Song:", True, (255, 255, 255))
          RCT_Song = Song.get_rect()
          RCT_Song.midleft = RCT_TokenCount.midleft
          RCT_Song.centery = RCT_SongContainer.centery          
          bg.blit(Song, RCT_Song.topleft)

          
          # Settings Devices
          Selection = 0
          Parameter = [0, 0, 2, 0, 1, 0]
          SelectionArrow = constant['Spritesheet'].Apply_Graphic((575, 219, 26, 27),
                                                                 colorkey=(255, 0, 255))
          RCT_SelectionArrow = SelectionArrow.get_rect()

          MusicSelection = constant['Spritesheet'].Apply_Graphic((575, 247, 26, 12),
                                                                 colorkey=(255, 0, 255))
          RCT_MusicSelection = MusicSelection.get_rect()

          # Music
          MUS_Settings = Load_Music('MUS_Settings.ogg')
          pygame.mixer.music.play(-1)


          
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
                              return 'BREAK'
                         elif EVT.key == K_SPACE or EVT.key == K_RETURN:
                              return Parameter
                         elif EVT.key == K_UP:
                              Selection -= 1
                              if Selection < 0:
                                   Selection = 5
                         elif EVT.key == K_DOWN:
                              Selection += 1
                              if Selection > 5:
                                   Selection = 0
                         elif EVT.key == K_RIGHT:
                              Parameter[Selection] += 1
                              if Parameter[0] > 4:
                                   Parameter[0] = 4
                              elif Parameter[1] > 3:
                                   Parameter[1] = 0
                              elif Parameter[2] > 7:
                                   Parameter[2] = 7
                              elif Parameter[3] > 4:
                                   Parameter[3] = 4
                              elif Parameter[4] > 3:
                                   Parameter[4] = 3
                              elif Parameter[5] > 2:
                                   Parameter[5] = 2
                         elif EVT.key == K_LEFT:
                              Parameter[Selection] -= 1
                              if Parameter[0] < 0: Parameter[0] = 0
                              elif Parameter[1] < 0:
                                   Parameter[1] = 3
                              elif Parameter[2] < 0:
                                   Parameter[2] = 0
                              elif Parameter[3] < 0:
                                   Parameter[3] = 0
                              elif Parameter[4] < 1:
                                   Parameter[4] = 1
                              elif Parameter[5] < 0:
                                   Parameter[5] = 0
                         else: pass
                                   
                    
               # Update Data
               # Background
               screen.FRAME.blit(bg, (0, 0))
               
               # Selection Arrow
               if Selection == 0:
                    RCT_SelectionArrow.midright = RCT_TokenCount.midleft
                    screen.FRAME.blit(SelectionArrow, RCT_SelectionArrow.topleft)
               elif Selection == 1:
                    RCT_SelectionArrow.midright = RCT_SpecialTokens.midleft
                    screen.FRAME.blit(SelectionArrow, RCT_SelectionArrow.topleft)
               elif Selection == 2:
                    RCT_SelectionArrow.midright = RCT_Timer.midleft
                    screen.FRAME.blit(SelectionArrow, RCT_SelectionArrow.topleft)
               elif Selection == 3:
                    RCT_SelectionArrow.midright = RCT_RandomDrop.midleft
                    screen.FRAME.blit(SelectionArrow, RCT_SelectionArrow.topleft)
               elif Selection == 4:
                    RCT_SelectionArrow.midright = RCT_Height.midleft
                    screen.FRAME.blit(SelectionArrow, RCT_SelectionArrow.topleft)
               elif Selection == 5:
                    RCT_SelectionArrow.midright = RCT_Song.midleft
                    screen.FRAME.blit(SelectionArrow, RCT_SelectionArrow.topleft)
                    
               # Token Count
               for count in range(1, 7+Parameter[0]):
                    newtoken = constant['Spritesheet'].Apply_Graphic(self.Color[count-1])
                    RCT_newtoken = newtoken.get_rect()
                    RCT_newtoken.topleft = RCT_Token_Container.topleft
                    RCT_newtoken = RCT_newtoken.move((count*40, 0))
                    screen.FRAME.blit(newtoken, RCT_newtoken.topleft)
                    
               # Special Tokens
               CAP_SpecialToken = constant['Font'].render(CaptionMessage[Parameter[1]], True,
                                                          (255, 255, 255))
               RCT_CAP_SpecialToken = CAP_SpecialToken.get_rect()
               RCT_CAP_SpecialToken.midtop = RCT_SpecialToken_Container.midbottom
               RCT_CAP_SpecialToken = RCT_CAP_SpecialToken.move(0, 10)
               if Parameter[1] == 0:
                    pass
               elif Parameter[1] == 1:
                    WildToken = constant['Spritesheet'].Apply_Graphic(self.Color[10])
                    RCT_WildToken = WildToken.get_rect()
                    RCT_WildToken.midtop = RCT_SpecialToken_Container.midtop
                    screen.FRAME.blit(WildToken, RCT_WildToken.topleft)
               elif Parameter[1] == 2:
                    FlashToken = constant['Spritesheet'].Apply_Graphic(self.Color[11])
                    RCT_FlashToken = FlashToken.get_rect()
                    RCT_FlashToken.midtop = RCT_SpecialToken_Container.midtop
                    screen.FRAME.blit(FlashToken, RCT_FlashToken.topleft)
               elif Parameter[1] == 3:
                    WildToken = constant['Spritesheet'].Apply_Graphic(self.Color[10])
                    RCT_WildToken = WildToken.get_rect()
                    RCT_WildToken.topleft = RCT_SpecialToken_Container.topleft
                    screen.FRAME.blit(WildToken, RCT_WildToken.topleft)
                    FlashToken = constant['Spritesheet'].Apply_Graphic(self.Color[11])
                    RCT_FlashToken = FlashToken.get_rect()
                    RCT_FlashToken.topright = RCT_SpecialToken_Container.topright
                    screen.FRAME.blit(FlashToken, RCT_FlashToken.topleft)
               screen.FRAME.blit(CAP_SpecialToken, RCT_CAP_SpecialToken.topleft)
               
               # Timer
               TimeTicks = Parameter[2]+3
               MSG_Time = "%s Ticks" % TimeTicks
               Color = None
               if TimeTicks == 3: Color = (255, 0, 0)
               elif TimeTicks == 4: Color = (255, 127, 0)
               elif TimeTicks == 5: Color = (255, 255, 0)
               elif TimeTicks == 6: Color = (0, 255, 0)
               elif TimeTicks == 7: Color = (0, 0, 255)
               elif TimeTicks == 8: Color = (0, 255, 255)
               elif TimeTicks == 9: Color = (255, 0, 255)
               elif TimeTicks == 10: Color = (127, 0, 127)
               Time = constant['Font'].render(MSG_Time, True, Color)
               screen.FRAME.blit(Time, RCT_Time.topleft)
               
               # Random Drop Count
               RandomDropCount = Parameter[3]+1
               MSG_RDC = ""
               if RandomDropCount == 1:
                    MSG_RDC = "%s Token" % RandomDropCount
               elif RandomDropCount > 1:
                    MSG_RDC = "%s Tokens" % RandomDropCount
               Color = None
               if RandomDropCount == 1: Color = (0, 0, 255)
               elif RandomDropCount == 2: Color = (0, 255, 0)
               elif RandomDropCount == 3: Color = (255, 255, 0)
               elif RandomDropCount == 4: Color = (255, 127, 0)
               elif RandomDropCount == 5: Color = (255, 0, 0)
               RDC = constant['Font'].render(MSG_RDC, True, Color)
               screen.FRAME.blit(RDC, RCT_RDC.topleft)
               
               # Height
               HeightStart = Parameter[4]*2
               MSG_Height = "%s Tokens High" % HeightStart
               Color = None
               if HeightStart == 2: Color = (255, 255, 255)
               elif HeightStart == 4: Color = (127, 127, 127)
               elif HeightStart == 6: Color = (60, 60, 60)
               HeightCount = constant['Font'].render(MSG_Height, True, Color)
               screen.FRAME.blit(HeightCount, RCT_HeightCount)
               
               # Music
               if Parameter[5] == 0:
                    RCT_MusicSelection.midtop = RCT_OFF.midbottom
               elif Parameter[5] == 1:
                    RCT_MusicSelection.midtop = RCT_BRIX.midbottom
               elif Parameter[5] == 2:
                    RCT_MusicSelection.midtop = RCT_BLOX.midbottom
               RCT_MusicSelection = RCT_MusicSelection.move(0, 5)
               screen.FRAME.blit(MusicSelection, RCT_MusicSelection.topleft)
                    
               # Update Screen
               screen.Update()
