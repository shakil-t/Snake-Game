# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 23:14:42 2017

@author: shakil
"""

import pygame 
import random
pygame.init()

#colors
black=(0,0,0)
darkgrey=(169,169,169)
gold=(240,230,140)
lavender=(230,230,250)
lightcoral=(240,128,128)
lightyellow=(250,250,210)
maroon=(128,0,0)
mediumvioletred=(199,21,133)
navy=(0,0,128)
orange=(255,165,0)
paleturquoise=(175,238,239)
royalblur=(65,105,225)
white=(255,255,255)

display_width=800
display_height=600

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Snake Game")

icon=pygame.image.load('c:/Users/shakil/Downloads/snake.jpg')
pygame.display.set_icon(icon)

clock=pygame.time.Clock()

block_size=10
fps=23
#fps stands for frames per second

smallfont=pygame.font.SysFont(None,25)
medfont=pygame.font.SysFont(None,50)
largefont=pygame.font.SysFont(None,80)

hedgeX=[]
hedgeY=[]
for i in range(0,6):
    x=round(random.randrange(0,display_width-block_size)/10.0)*10.0
    hedgeX.append(x)
    y=round(random.randrange(0,display_height-block_size)/10.0)*10.0
    hedgeY.append(y)

def pause():
    pause=True
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    pause=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message_to_screen("Paused",navy,-120,size="large")
        message_to_screen("Press A to continue or Q to quit",royalblur,20,size="medium")
        pygame.display.update()


def score(score):
    text=smallfont.render("Score:"+str(score),True,lavender)
    gameDisplay.blit(text,[0,0])


def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    intro=False
                if event.type==pygame.K_q:
                    pygame.quit()
                    quit()
                    
                
        gameDisplay.fill(white)
        message_to_screen("Welcome to Snake",mediumvioletred,-120,size="large")
        message_to_screen("Eat the Apple!",orange,-30,size="large")
        message_to_screen("Press A to play or Q to quit and P to pause if necessary",lightcoral,100,size="small")
        pygame.display.update()


def snake(block_size,snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay,maroon,[XnY[0],XnY[1],block_size,block_size])
    
def text_objects(text,color,size):
    if size=="small":
        textSurface=smallfont.render(text,True,color)
    elif size=="medium":
        textSurface=medfont.render(text,True,color)
    elif size=="large":
        textSurface=largefont.render(text,True,color)
    return textSurface,textSurface.get_rect()


def message_to_screen(msg,color,y_displace=0,size="small"):
    textSurf,textRect=text_objects(msg,color,size)
    textRect.center=(display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)
   
    
def gameLoop():
    gameExit=False
    gameOver=False
    
    lead_x=display_width/2
    lead_y=display_height/2
    
    lead_x_change=0
    lead_y_change=0
    
    snakeList=[]
    snakeLength=10
    
    randAppleX=round(random.randrange(0,display_width-block_size)/10.0)*10.0
    randAppleY=round(random.randrange(0,display_height-block_size)/10.0)*10.0
                    
    
    while not gameExit:
        
        while gameOver==True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",paleturquoise,-50,size="large")
            message_to_screen("Press A to play again or Q to quit",lightyellow,50,size="medium")
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameExit=True
                    gameOver=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False
                    if event.key==pygame.K_a:
                        gameLoop()
                        
            
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    lead_x_change=block_size
                    lead_y_change=0
                elif event.key==pygame.K_LEFT:
                    lead_x_change=-block_size
                    lead_y_change=0
                elif event.key==pygame.K_UP:
                    lead_y_change=-block_size
                    lead_x_change=0
                elif event.key==pygame.K_DOWN:
                    lead_y_change=block_size
                    lead_x_change=0
                elif event.key==pygame.K_p:
                    pause()
                    
        if lead_x>=display_width or lead_x<0 or lead_y>=display_height or lead_y<0:
            gameOver=True
            
        lead_x+=lead_x_change
        lead_y+=lead_y_change
        
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,gold,[randAppleX,randAppleY,block_size,block_size])
        
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        
        if len(snakeList)>snakeLength:
            del snakeList[0]
        
        for eachSegment in snakeList[:-1]:
            if eachSegment==snakeHead:
                gameOver=False
        
        snake(block_size,snakeList)
        
        score(snakeLength-10)
        
        pygame.display.update()
        
        if lead_x==randAppleX and lead_y==randAppleY:
            pygame.mixer.music.load('c:/Users/shakil/Downloads/eat.wav')
            pygame.mixer.music.play(1)
            randAppleX=round(random.randrange(0,display_width-block_size)/10.0)*10.0
            randAppleY=round(random.randrange(0,display_height-block_size)/10.0)*10.0
            snakeLength+=1
            
        if snakeLength>11:
            for j in range(0,6):
                pygame.draw.rect(gameDisplay,darkgrey,[hedgeX[j],hedgeY[j],block_size,block_size])
                for a in hedgeX:
                    for b in hedgeY:
                        if lead_x==a and lead_y==b:
                            pygame.mixer.music.load('c:/Users/shakil/Downloads/boom.wav')
                            pygame.mixer.music.play(1)
                            gameOver=True
            pygame.display.update()
            
            
        
        clock.tick(fps)
    
    pygame.quit()
    quit()
    
    
game_intro()      
gameLoop()