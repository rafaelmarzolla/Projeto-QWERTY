

import pygame
import time
import sys
from pygame.locals import *
import random
import pygame.mixer
pygame.init()


pygame.time.get_ticks()


white = (255,255,255) #definindo cores pelo espectro rgb( red, green, blue)
black=(0,0,0)
red=(255,0,0) 
green=(0,200,0)
blue=(0,0,255)
yellow=(255,255,0)
display_widht = 800
display_height = 600
v = 0.15  # velocidade da andada
#---------------------------------------------------------------------------------------------------------#

gameDisplay = pygame.display.set_mode((display_widht,display_height))  #cria janela no pygame
pygame.display.set_caption("QWERTY") #da titulo a janela

smallfont = pygame.font.SysFont("comicsnsms", 25) #Tamanho da fonte
medfont = pygame.font.SysFont("comicsnsms", 50)
largefont = pygame.font.SysFont("comicsnsms", 80)


C_1 = pygame.image.load("Craquinho_parado.png")


C_2 = pygame.image.load("Craquinho_correndo_1.png")


C_3 = pygame.image.load("Craquinho_correndo_2.png")

C_4 = pygame.image.load("Craquinho_semicorrendo_1.png")

C_5 = pygame.image.load("Craquinho_semicorrendo_2.png")

def text_objects(text,color,size):
    if size=="small":
        textSurface = smallfont.render(text,True,color)
    if size=="medium":
        textSurface = medfont.render(text,True,color)
    if size=="large":
        textSurface = largefont.render(text,True,color)
    
    
    
    
    
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color,y_displace=0,size= "small"):   #texto na tela e cor
        textSurf, textRect = text_objects(msg,color,size)
        
        textRect.center = (display_widht/2), (display_height /2)+y_displace
        gameDisplay.blit(textSurf, textRect)

gameDisplay.fill(white)

pygame.display.update()

def game_intro():
    
    intro = True
    
    while intro:
        
        for event in pygame.event.get():  #clicar no X e sair
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    intro = False
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        
        
        
        
        
        gameDisplay.fill(white)
        message_to_screen("QWERTY",green,y_displace=-100,size="large")
    
        message_to_screen("The objective of the game is to reach the end", black, y_displace = -30, size="small")
    
        #message_to_screen("If you run into the edges or yourself,you die!", red, y_displace = -50,size = "small")
        
        message_to_screen("Press P to play or Q to quit",black,y_displace=10,size = "medium")
    
        pygame.display.update() 

def gameLoop ():  #funçao para definir o jogo
    gameExit = False
    gameOver = False
    aux = 0
# Craquinho andando   
    while not gameExit:
        
        
        while gameOver == True:  # antes de fechar da opçoes de voltar a jogar
            #pygame.mixer.music.stop()
         
            
            for event in pygame.event.get():  #se n quer jogar
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                        
                    if event.key == pygame.K_p: #se quer jogar
                        gameLoop()
                        
        if aux == 0:
            x = C_1
            gameDisplay.blit(x,(-70,500))
            time.sleep(v)
            aux+=1
            pygame.display.update()
            gameDisplay.fill(white)
        elif aux == 1:
            x = C_4
            gameDisplay.blit(x,(-70,500))
            time.sleep(v)
            aux+=1
            pygame.display.update()
            gameDisplay.fill(white)
        elif aux == 2:
            x = C_2
            gameDisplay.blit(x,(-70,500))
            time.sleep(v)
            aux+=1
            pygame.display.update()
            gameDisplay.fill(white)
        elif aux == 3:
            x = C_4
            gameDisplay.blit(x,(-70,500))
            time.sleep(v)
            aux+=1
            pygame.display.update()
            gameDisplay.fill(white)
        elif aux == 4:
            x = C_1
            gameDisplay.blit(x,(-70,500))
            time.sleep(v)
            aux+=1
            pygame.display.update()
            gameDisplay.fill(white)
        elif aux == 5:
            x = C_5
            gameDisplay.blit(x,(-70,500))
            time.sleep(v)
            aux+=1
            pygame.display.update()
            gameDisplay.fill(white)
        elif aux == 6:
            x = C_3
            gameDisplay.blit(x,(-70,500))
            time.sleep(v)
            aux +=1
            pygame.display.update()
            gameDisplay.fill(white)
        elif aux == 7:
            x = C_5
            gameDisplay.blit(x,(-70,500))
            time.sleep(v)
            aux=0
            pygame.display.update()
            gameDisplay.fill(white)
        
    
game_intro()
gameLoop()
    
    
    