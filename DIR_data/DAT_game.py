#! /usr/bin/env python


# File Docstring
"""Chapter: Game

This is where the actual meat of the game
takes place."""

# Import Modules
import __init__
import sys
import random

import pygame
from pygame.locals import *

# Import Game Data
from DIR_sprite.DAT_token import SPT_token
from DIR_sprite.DAT_spotselector import SPT_spotselector
from DIR_audio.DAT_loadaudio import *


# Chapter Class
class CHP_game:
     """The game chapter."""
     def __init__(self, param):
          """Initialize."""
          # Token Count
          self.TokenPool = ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red',
                            'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange',
                            'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow',
                            'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green',
                            'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue',
                            'purple', 'purple', 'purple', 'purple', 'purple', 'purple', 'purple']
          if param[0] == 0: pass
          elif param[0] > 0:
               self.TokenPool.append('cyan')
               self.TokenPool.append('cyan')
               self.TokenPool.append('cyan')
               self.TokenPool.append('cyan')
               self.TokenPool.append('cyan')
               self.TokenPool.append('cyan')
               if param[0] > 1:
                    self.TokenPool.append('magenta')
                    self.TokenPool.append('magenta')
                    self.TokenPool.append('magenta')
                    self.TokenPool.append('magenta')
                    self.TokenPool.append('magenta')
                    if param[0] > 2:
                         self.TokenPool.append('brown')
                         self.TokenPool.append('brown')
                         self.TokenPool.append('brown')
                         self.TokenPool.append('brown')
                         if param[0] > 3:
                              self.TokenPool.append('gray')
                              self.TokenPool.append('gray')
                              self.TokenPool.append('gray')
                                   
          # Special Tokens
          if param[1] == 0: pass
          elif param[1] == 1:
               self.TokenPool.append('black')
               self.TokenPool.append('black')
          elif param[1] == 2:
               self.TokenPool.append('white')
          elif param[1] == 3:
               self.TokenPool.append('black')
               self.TokenPool.append('black')
               self.TokenPool.append('white')
               
          # Timer
          self.Timer = (param[2] + 3)
          
          # Random Drop Count
          self.RDC = param[3] + 1
          
          # Height
          self.Height = param[4] * 2
          
          # Music
          if param[5] == 0:
               self.Music = False
          elif param[5] == 1:
               self.Music = MUS_Brix = Load_Music('MUS_Brix.ogg')
          elif param[5] == 2:
               self.Music = MUS_Blox = Load_Music('MUS_Blox.ogg')
          else:
               pass
          

     def Start(self, screen, constant):
          """Start the chapter."""
          # Prepare any data before running the loop.
          
          pygame.event.get() # Purge the Input Queue.
          
          random.seed()
          random.shuffle(self.TokenPool)

          if self.Music != False:
               pygame.mixer.music.play(-1)
          elif self.Music == False:
               pygame.mixer.music.stop()

          CLEARING = False
          PAUSED = False
          GAME_OVER = False
          ROUND_CLEAR = False

          BLACK_CLEAR = None
          WHITE_CLEAR = False

          SCORE = 0
          HISCORE = constant['HighScore']
          TIMER = self.Timer
          DELAY = 60
          ROUNDS = 0
          
          

          
          # PAUSE SCREEN
          PauseScreen = pygame.Surface(screen.RECT.size).convert()
          PauseScreen.fill((0, 0, 0))
          RCT_PauseScreen = PauseScreen.get_rect()
          # Pause Font
          PauseFont = constant['BigFont'].render("P A U S E", True, (255, 255, 255))
          RCT_PauseFont = PauseFont.get_rect()
          RCT_PauseFont.center = RCT_PauseScreen.center
          PauseScreen.blit(PauseFont, RCT_PauseFont.topleft)
          # Return to the game
          ReturnInfo = constant['Font'].render("Press ESC to unpause.", True,
                                               (255, 255, 255))
          RCT_ReturnInfo = ReturnInfo.get_rect()
          RCT_ReturnInfo.midtop = RCT_PauseFont.midbottom
          PauseScreen.blit(ReturnInfo, RCT_ReturnInfo.topleft)
          # Exit the game
          ExitInfo = constant['Font'].render("Press SPACE or ENTER to quit this round.", True,
                                             (255, 255, 255))
          RCT_ExitInfo = ExitInfo.get_rect()
          RCT_ExitInfo.midtop = RCT_ReturnInfo.midbottom
          PauseScreen.blit(ExitInfo, RCT_ExitInfo.topleft)



          # GAME OVER SCREEN
          GameOver = constant['BigFont'].render("GAME OVER", True,
                                         (255, 255, 255), (0, 0, 0))
          RCT_GameOver = GameOver.get_rect()
          RCT_GameOver.center = screen.RECT.center
          

          # ROUND CLEAR SCREEN
          RoundClear = constant['BigFont'].render("ROUND CLEAR", True,
                                         (255, 255, 255), (0, 0, 0))
          RCT_RoundClear = RoundClear.get_rect()
          RCT_RoundClear.center = screen.RECT.center
          
          

               

          # Background
          bg = pygame.Surface(screen.RECT.size).convert()
          bg.fill((random.randrange(100,201), random.randrange(100, 201), random.randrange(100, 201)))
          
          # Token Container
          TokenContainer = constant['Spritesheet'].Apply_Graphic((602, 1, 280, 480))
          RCT_TokenContainer = TokenContainer.get_rect()
          RCT_TokenContainer.center = screen.RECT.center
          bg.blit(TokenContainer, RCT_TokenContainer.topleft)
          VisualGrid = pygame.Rect(0, 0, 200, 440)
          VisualGrid.midtop = RCT_TokenContainer.midtop

          # Score
          CPT_Score = constant['BigFont'].render("SCORE:", True,
                                                 (255, 255, 255))
          RCT_CPT_Score = CPT_Score.get_rect()
          RCT_CPT_Score.topleft = RCT_TokenContainer.topright
          bg.blit(CPT_Score, RCT_CPT_Score.topleft)
          Score = constant['BigFont'].render('%s' % SCORE, True,
                                             (0, 255, 0), (0, 0, 0))
          RCT_Score = Score.get_rect()
          RCT_Score.topleft = RCT_CPT_Score.bottomleft

          # High Score
          CPT_HiScore = constant['BigFont'].render("HIGH SCORE:", True,
                                                 (255, 255, 255))
          RCT_CPT_HiScore = CPT_HiScore.get_rect()
          RCT_CPT_HiScore.topleft = RCT_Score.bottomleft
          bg.blit(CPT_HiScore, RCT_CPT_HiScore.topleft)
          HiScore = constant['BigFont'].render('%s' % HISCORE, True,
                                               (255, 0, 0), (0, 0, 0))
          RCT_HiScore = Score.get_rect()
          RCT_HiScore.topleft = RCT_CPT_HiScore.bottomleft

          # Timer
          CPT_Timer = constant['BigFont'].render("TIME:", True,
                                                 (255, 255, 255))
          RCT_CPT_Timer = CPT_Timer.get_rect()
          RCT_CPT_Timer.topleft = RCT_HiScore.bottomleft
          bg.blit(CPT_Timer, RCT_CPT_Timer.topleft)
          Timer = constant['BigFont'].render('0', True,
                                             (255, 255, 0), (0, 0, 0))
          RCT_Timer = Timer.get_rect()
          RCT_Timer.topleft = RCT_CPT_Timer.bottomleft


          # Next Token
          CPT_NextToken = constant['BigFont'].render("NEXT:", True,
                                                     (255, 255, 255))
          RCT_CPT_NextToken = CPT_NextToken.get_rect()
          RCT_CPT_NextToken.topleft = RCT_Timer.bottomleft
          bg.blit(CPT_NextToken, RCT_CPT_NextToken.topleft)
          NT_Container = pygame.Rect(0, 0, 40, 40)
          NT_Container.midtop = RCT_CPT_NextToken.bottomright

          # Current Token
          CPT_CurrentToken = constant['BigFont'].render("CURRENT:", True,
                                                     (255, 255, 255))
          RCT_CPT_CurrentToken = CPT_CurrentToken.get_rect()
          RCT_CPT_CurrentToken.midtop = NT_Container.midbottom
          RCT_CPT_CurrentToken.left = RCT_CPT_NextToken.left
          bg.blit(CPT_CurrentToken, RCT_CPT_CurrentToken.topleft)
          CT_Container = pygame.Rect(0, 0, 40, 40)
          CT_Container.midtop = RCT_CPT_CurrentToken.bottomright
          CT_Container.centerx = NT_Container.centerx


          # RDC
          CPT_RDC = constant['BigFont'].render("Random Drop:", True,
                                                 (255, 255, 255))
          RCT_CPT_RDC = CPT_RDC.get_rect()
          RCT_CPT_RDC.topright = RCT_TokenContainer.topleft
          bg.blit(CPT_RDC, RCT_CPT_RDC.topleft)
          RDC = constant['BigFont'].render('%s' % self.RDC, True,
                                             (255, 255, 255))
          RCT_RDC = RDC.get_rect()
          RCT_RDC.midtop = RCT_CPT_RDC.midbottom
          bg.blit(RDC, RCT_RDC.topleft)

          # Rounds
          CPT_Rounds = constant['BigFont'].render("Rounds:", True,
                                                 (255, 255, 255))
          RCT_CPT_Rounds = CPT_Rounds.get_rect()
          RCT_CPT_Rounds.left = RCT_CPT_RDC.left
          RCT_CPT_Rounds.top = RCT_RDC.bottom
          bg.blit(CPT_Rounds, RCT_CPT_Rounds.topleft)
          Rounds = constant['BigFont'].render('%s' % ROUNDS, True,
                                             (255, 255, 255))
          RCT_Rounds = Rounds.get_rect()
          RCT_Rounds.topleft = RCT_CPT_Rounds.bottomleft
          RCT_Rounds.centerx = RCT_RDC.centerx

          
          
          # Spot Selector
          SS = SPT_spotselector(constant['Spritesheet'])
          SpotChoice = []
          for _ in range(0, 5):
               SpotChoice.append(pygame.Rect(0, 0, 40, 40))
          SpotChoice[0].bottomleft = VisualGrid.bottomleft
          for _ in range(1,5):
               SpotChoice[_].bottomleft = SpotChoice[_-1].bottomright
          SpotSelector = pygame.sprite.RenderUpdates()
          SpotSelector.add(SS)
          Spot = 2


          # Data Grid
          DataGrid = [[], [], [], [], []]
          AllTokens = pygame.sprite.RenderUpdates()
          # Add tokens to...
          for column in DataGrid: # Data Grid
               for heightcount in range(0, self.Height):
                    newtoken = SPT_token(constant['Spritesheet'],
                                         random.choice(self.TokenPool))
                    column.append(newtoken)
               for _ in column: # Group
                    AllTokens.add(_)
          # Apply the tokens to the Visual Grid.
          for colcount in range(0, 5):
               DataGrid[colcount][0].RECT.center = SpotChoice[colcount].center
               for nextcount in range(1, self.Height):
                    DataGrid[colcount][nextcount].RECT.midbottom = \
                    DataGrid[colcount][nextcount-1].RECT.midtop
                    
          

          # Prepare for action...
          NextToken = random.choice(self.TokenPool)
          CurrentToken = random.choice(self.TokenPool)
          
          Ready = constant['BigFont'].render("R E A D Y", True,
                                             (255, 255, 255), (255, 0, 0))
          RCT_Ready =  Ready.get_rect()
          RCT_Ready.center = screen.RECT.center
          screen.FRAME.blit(bg, (0, 0))
          screen.FRAME.blit(Ready, RCT_Ready.topleft)
          screen.Update()
          pygame.time.wait(1000)
          SFC_NextToken = constant['Spritesheet'].\
                          Apply_Graphic(SPT_token.DIC_color[NextToken][1])
          SFC_CurrentToken = constant['Spritesheet'].\
                          Apply_Graphic(SPT_token.DIC_color[CurrentToken][1])


          # Sound Effects
          SND_GameOver = Load_Sound('SND_GameOver.ogg') ; SND_GameOver_Flag = False
          SND_Pause = Load_Sound('SND_Pause.ogg')
          SND_SpotSelect = Load_Sound('SND_SpotSelect.ogg')
          SND_SpotRotate = Load_Sound('SND_SpotRotate.ogg')
          SND_Place = Load_Sound('SND_Place.ogg')
          SND_NoPlace = Load_Sound('SND_NoPlace.ogg')
          SND_Clear = Load_Sound('SND_Clear.ogg') ; SND_Clear_Flag = False
          SND_RoundClear = Load_Sound('SND_RoundClear.ogg') ; SND_RoundClear_Flag = False
          SND_RandomDrop = Load_Sound('SND_RandomDrop.ogg')

          
          

          
          # Main Loop
          LS = True # Loop Switch
          while LS:
               constant['Clock'].tick(60) # Clock 60 Frames Per Second

               # In the event of a token-placing bug, remove any token higher than 11...
               for column in DataGrid:
                    if len(column) > 11:
                         ExtraTokens = column[11:]
                         del column[11:]
                         for _ in ExtraTokens:
                              _.kill()
                         


               # Check the grid for clear columns.
               FullGrid = [None, None, None, None, None]
               for colcount in range(5):
                    if len(DataGrid[colcount]) == 11:
                         FullGrid[colcount] = True
                    elif len(DataGrid[colcount]) > 0 and len(DataGrid[colcount]) < 11:
                         FullGrid[colcount] = False
                    elif len(DataGrid[colcount]) == 0:
                         FullGrid[colcount] = 'CLEAR'

               if FullGrid == [True, True, True, True, True]: # If the entire grid is full...
                    GAME_OVER = True

               elif 'CLEAR' in FullGrid: # If at least one stack is cleared...
                    ROUND_CLEAR = True

               # Random Drop Count
               if TIMER == 0 and DELAY == 60 and GAME_OVER == False:
                    SND_RandomDrop.play()
                    RemainingSpace = 0
                    # For every column in the data grid...
                    for column in DataGrid:
                         RemainingSpace += (11 - len(column))

                    TokenDrops = 0
                    if RemainingSpace > self.RDC:
                         TokenDrops = self.RDC
                    elif RemainingSpace <= self.RDC:
                         TokenDrops = RemainingSpace
                         
                    for _ in range(TokenDrops):
                         StackCheck = True
                         while StackCheck == True:
                              RandomSpot = random.choice(DataGrid)
                              if len(RandomSpot) == 11:
                                   pass
                              else:
                                   StackCheck = False


                         RandomToken = SPT_token(constant['Spritesheet'],
                                                 random.choice(self.TokenPool))
                         RandomSpot.append(RandomToken)
                         AllTokens.add(RandomSpot[-1])

               # Black Clear
               if BLACK_CLEAR:
                    for col in DataGrid:
                         for token in col:
                              if token.IDEN == BLACK_CLEAR:
                                   token.CLEAR = True
                    BLACK_CLEAR = None
                    
               # White Clear
               if WHITE_CLEAR == True:
                    for col in DataGrid:
                         for token in col[2:]:
                              token.CLEAR = True
                    WHITE_CLEAR = False


               
               # Game Over
               if GAME_OVER == True and CLEARING == False: # If the game is over...
                    if SND_GameOver_Flag == True:
                         pass
                    elif SND_GameOver_Flag == False:
                         pygame.mixer.music.stop()
                         SND_GameOver.play()
                         SND_GameOver_Flag = True
                    for EVT in pygame.event.get():
                         if EVT.type == QUIT: # Hard Exit
                              pygame.quit()
                              sys.exit()
                         elif EVT.type == KEYDOWN:
                              if EVT.key == K_ESCAPE or \
                                 EVT.key == K_RETURN or \
                                 EVT.key == K_SPACE:
                                      constant['HighScore'] = HISCORE
                                      LS = False
                         else:
                              pass
                    screen.FRAME.blit(GameOver, RCT_GameOver.topleft)

               
               elif ROUND_CLEAR == True: # If one stack has been cleared...
                    if SND_RoundClear_Flag == True:
                         pass
                    elif SND_RoundClear_Flag == False:
                         pygame.mixer.music.stop()
                         SND_RoundClear.play()
                         SND_RoundClear_Flag = True
                    for EVT in pygame.event.get():
                         if EVT.type == QUIT: # Hard Exit
                              pygame.quit()
                              sys.exit()
                         elif EVT.type == KEYDOWN:
                              if EVT.key == K_ESCAPE:
                                   constant['HighScore'] = HISCORE
                                   LS = False
                              elif EVT.key == K_RETURN or \
                                   EVT.key == K_SPACE:
                                   constant['HighScore'] = HISCORE
                                   ROUND_CLEAR = False
                                   SND_RoundClear_Flag = False
                                   if self.Music != False:
                                        pygame.mixer.music.play(-1)
                                   # Reset All
                                   ROUNDS += 1
                                   TIMER = self.Timer
                                   DataGrid = [[], [], [], [], []]
                                   AllTokens = pygame.sprite.RenderUpdates()
                                   # Reset BG
                                   bg.fill((random.randrange(100,201), random.randrange(100, 201), random.randrange(100, 201)))
                                   bg.blit(TokenContainer, RCT_TokenContainer.topleft)
                                   bg.blit(CPT_Score, RCT_CPT_Score.topleft)
                                   bg.blit(CPT_HiScore, RCT_CPT_HiScore.topleft)
                                   bg.blit(CPT_Timer, RCT_CPT_Timer.topleft)
                                   bg.blit(CPT_NextToken, RCT_CPT_NextToken.topleft)
                                   bg.blit(CPT_CurrentToken, RCT_CPT_CurrentToken.topleft)
                                   bg.blit(CPT_RDC, RCT_CPT_RDC.topleft)
                                   bg.blit(RDC, RCT_RDC.topleft)
                                   bg.blit(CPT_Rounds, RCT_CPT_Rounds.topleft)
                                   # Add tokens to...
                                   for column in DataGrid: # Data Grid
                                        for heightcount in range(0, self.Height):
                                             newtoken = SPT_token(constant['Spritesheet'],
                                                                  random.choice(self.TokenPool))
                                             column.append(newtoken)
                                        for _ in column: # Group
                                             AllTokens.add(_)
                                   # Apply the tokens to the Visual Grid.
                                   for colcount in range(0, 5):
                                        DataGrid[colcount][0].RECT.center = SpotChoice[colcount].center
                                        for nextcount in range(1, self.Height):
                                             DataGrid[colcount][nextcount].RECT.midbottom = \
                                             DataGrid[colcount][nextcount-1].RECT.midtop
                         else:
                              pass
                    screen.FRAME.blit(RoundClear, RCT_RoundClear.topleft)


               elif PAUSED == True: # If the game is paused...
                    for EVT in pygame.event.get():
                         if EVT.type == QUIT: # Hard Exit
                              pygame.quit()
                              sys.exit()
                         elif EVT.type == KEYDOWN:
                              if EVT.key == K_ESCAPE:
                                   PAUSED = False
                                   if self.Music != False:
                                        pygame.mixer.music.unpause()
                              elif EVT.key == K_RETURN or EVT.key == K_SPACE:
                                   constant['HighScore'] = HISCORE
                                   LS = False
                         else: pass
                    screen.FRAME.blit(PauseScreen, (0, 0))
                    
                    
               elif PAUSED == False: # If the game is running...
                    # Don't forget to pass a CLEARING flag as False.
                    for EVT in pygame.event.get():
                         if EVT.type == QUIT: # Hard Exit
                              pygame.quit()
                              sys.exit()
                         elif EVT.type == KEYDOWN:
                              if EVT.key == K_ESCAPE:
                                   PAUSED = True
                                   pygame.mixer.music.pause()
                                   SND_Pause.play()
                              elif EVT.key == K_LEFT and CLEARING == False:
                                   Spot -= 1
                                   if Spot < 0:
                                        Spot = 0
                                        SND_NoPlace.play()
                                   else:
                                        SND_SpotSelect.play()
                              elif EVT.key == K_RIGHT and CLEARING == False:
                                   Spot += 1
                                   if Spot > 4:
                                        Spot = 4
                                        SND_NoPlace.play()
                                   else:
                                        SND_SpotSelect.play()
                              elif EVT.key == K_UP and CLEARING == False:
                                   DataGrid[Spot].insert(0, DataGrid[Spot].pop())
                                   SND_SpotRotate.play()
                              elif EVT.key == K_DOWN and CLEARING == False:
                                   DataGrid[Spot].append(DataGrid[Spot].pop(0))
                                   SND_SpotRotate.play()
                              elif EVT.key == K_1 and CLEARING == False:
                                   Spot = 0
                                   SND_SpotSelect.play()
                              elif EVT.key == K_2 and CLEARING == False:
                                   Spot = 1
                                   SND_SpotSelect.play()
                              elif EVT.key == K_3 and CLEARING == False:
                                   Spot = 2
                                   SND_SpotSelect.play()
                              elif EVT.key == K_4 and CLEARING == False:
                                   Spot = 3
                                   SND_SpotSelect.play()
                              elif EVT.key == K_5 and CLEARING == False:
                                   Spot = 4
                                   SND_SpotSelect.play()
                              elif (EVT.key == K_RETURN or EVT.key == K_SPACE) \
                                   and CLEARING == False:
                                   if FullGrid[Spot] == True:
                                        SND_NoPlace.play()
                                   elif FullGrid[Spot] == False:
                                        SND_Place.play()
                                        DataGrid[Spot].insert(0,
                                                              SPT_token(constant['Spritesheet'],
                                                                        CurrentToken))
                                        AllTokens.add(DataGrid[Spot][0])
                                        CurrentToken = NextToken
                                        NextToken = random.choice(self.TokenPool)
                                        SFC_NextToken = constant['Spritesheet'].\
                                         Apply_Graphic(SPT_token.DIC_color[NextToken][1])
                                        SFC_CurrentToken = constant['Spritesheet'].\
                                         Apply_Graphic(SPT_token.DIC_color[CurrentToken][1])
                         else:
                              pass
                                        

                    # Pop out any tokens that are cleared to go.
                    for col in DataGrid:
                         if len(col) == 0: pass
                         elif len(col) >= 1:
                              for token in col:
                                   if token.ALPHA <= 0:
                                        removedtoken = col.pop(col.index(token))
                                        SCORE += removedtoken.SCORE
                                        removedtoken.kill()
                                        
                                        
                                        
                    # Attach the token stacks on each other.
                    for colcount in range(5):
                         if len(DataGrid[colcount]) == 0: pass
                         else:
                              DataGrid[colcount][0].RECT.center = SpotChoice[colcount].center
                              for nextcount in range(1, len(DataGrid[colcount])):
                                   DataGrid[colcount][nextcount].RECT.midbottom = \
                                   DataGrid[colcount][nextcount-1].RECT.midtop

                    # Mandatory Line-Clearing Check.
                    HeightCheck = [] # A list of each column's height.
                    for col in DataGrid:
                         HeightCheck.append(len(col))
                    MinimumHeight = min(HeightCheck)
                    ValidCount = 0
                    if MinimumHeight == 0:
                         ROUND_CLEAR = True
                    elif MinimumHeight >= 1:
                         for rowcheck in range(MinimumHeight):
                              ValidCheck = []
                              for col in DataGrid:
                                   ValidCheck.append(col[rowcheck])
                              ColorPool = []
                              for _ in ValidCheck:
                                   if _.IDEN in ColorPool:
                                        pass
                                   else:
                                        ColorPool.append(_.IDEN)
                              ColorCount = 0
                              for _ in ColorPool:
                                   if _ == 'black' or _ == 'white':
                                        pass
                                   else:
                                        ColorCount += 1
                              if ColorCount > 1:
                                   pass
                              elif ColorCount == 1:
                                   for token in ValidCheck:
                                        token.CLEAR = True
                                   if 'black' in ColorPool:
                                        for _ in ColorPool:
                                             if _ == 'black' or _ == 'white':
                                                  pass
                                             else:
                                                  BLACK_CLEAR = _
                                   if 'white' in ColorPool:
                                        WHITE_CLEAR = True
                                   ValidCount += 1
                                   
                              
                    if ValidCount >= 1:
                         CLEARING = True
                         if SND_Clear_Flag == True:
                              pass
                         else:
                              SND_Clear.play()
                              SND_Clear_Flag = True
                    elif ValidCount == 0:
                         CLEARING = False
                         SND_Clear_Flag = False
                                   
                    # Background Info
                    screen.FRAME.blit(bg, (0, 0))
                    Score = constant['BigFont'].render('%s' % SCORE, True,
                                                       (0, 255, 0), (0, 0, 0))
                    screen.FRAME.blit(Score, RCT_Score.topleft)
                    if SCORE >= HISCORE: HISCORE = SCORE
                    HiScore = constant['BigFont'].render('%s' % str(HISCORE), True,
                                                         (255, 0, 0), (0, 0, 0))
                    screen.FRAME.blit(HiScore, RCT_HiScore.topleft)

                    # Timer Info
                    if CLEARING == False:
                         DELAY -= 1
                         if DELAY < 0:
                              DELAY = 60
                              TIMER -= 1
                              if TIMER < 0:
                                   TIMER = self.Timer                                                                               
                    Timer = constant['BigFont'].render('%s' % (TIMER), True,
                                                       (255, 255, 0), (0, 0, 0))
                    screen.FRAME.blit(Timer, RCT_Timer.topleft)


                    # Next & Current Tokens
                    screen.FRAME.blit(SFC_NextToken, NT_Container.topleft)
                    screen.FRAME.blit(SFC_CurrentToken, CT_Container.topleft)

                    # Rounds Count
                    Rounds = constant['BigFont'].render('%s' % ROUNDS, True,
                                             (255, 255, 255))
                    screen.FRAME.blit(Rounds, RCT_Rounds.topleft)
                    # Tokens
                    AllTokens.update()
                    AllTokens.draw(screen.FRAME)
                    # Spot Selector
                    SS.RECT.center = SpotChoice[Spot].center
                    SpotSelector.update()
                    SpotSelector.draw(screen.FRAME)


                              
               # Update Screen
               screen.Update()
