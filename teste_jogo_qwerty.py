# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 11:10:54 2015

@author: Usuario
"""

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
v = 0.15
#---------------------------------------------------------------------------------------------------------#
    
gameDisplay = pygame.display.set_mode((display_widht,display_height))  #cria janela no pygame
pygame.display.set_caption("QWERTY") #da titulo a janela

C_1 = pygame.image.load("Craquinho_parado.png")


C_2 = pygame.image.load("Craquinho_correndo_1.png")


C_3 = pygame.image.load("Craquinho_correndo_2.png")

C_4 = pygame.image.load("Craquinho_semicorrendo_1.png")

C_5 = pygame.image.load("Craquinho_semicorrendo_2.png")

aux = 0

gameDisplay.fill(white)

pygame.display.update()

    
    
while True:
    
    
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
        aux =0
        pygame.display.update()
        gameDisplay.fill(white)
    elif aux == 7:
        x = C_5
        gameDisplay.blit(x,(-70,500))
        time.sleep(v)
        aux=0
        pygame.display.update()
        gameDisplay.fill(white)
        
    

    
    
    
