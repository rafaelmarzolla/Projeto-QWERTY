# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:24:18 2015

@author: Lucas
"""
import pygame
import os
import time

pygame.init()

black = (0,0,0)
green = (0,200,0)
white = (255,255,255)
red = (255,0,0)


display_width = 800
display_height = 672

dez = 10

pos_x = display_width/2
pos_y = display_height/2

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Temple Crack")

font = pygame.font.SysFont(None, 25)

C_1 = pygame.image.load("Craquinho_parado.png")


C_2 = pygame.image.load("Craquinho_correndo_1.png")


C_3 = pygame.image.load("Craquinho_correndo_2.png")

C_4 = pygame.image.load("Craquinho_semicorrendo_1.png")

C_5 = pygame.image.load("Craquinho_semicorrendo_2.png")
C_6 = pygame.image.load ("craquinho_voando.png")
        
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

    

fundo = pygame.image.load(os.path.join('level_1.png'))

def loopjogo():
    aux = 0
    




        

    gameExit = False
    gameOver = False
    
    posi_x = 0
    posi_y = 0
    
    vel_inicial = 0
    
    crack_y = 500
    vel_pulo = 0

    
   
    
    while gameExit == False:
        while gameOver == True:
            
            gameDisplay.fill((255,255,255))
            message_to_screen("Fim de jogo, pressione P para jogar denovo ou S para sair", (red))
            pygame.display.update()
            
            
            for i in pygame.event.get():
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_s:
                        gameOver = False
                        gameExit = True
    
                    if i.key == pygame.K_p:
                        loopjogo()
                  
                        
                        
                         

        
        
        for i in pygame.event.get():
            
            
            if i.type == pygame.QUIT:
                gameExit = True
            if i.type == pygame.KEYDOWN:
                
                if i.key == pygame.K_p:
                     vel_inicial = 10
                if i.key == pygame.K_SPACE:
                     vel_pulo = 20
        
        
        crack_y -= vel_pulo 
        posi_x -= vel_inicial
        
        if crack_y >= 500:
            vel_pulo = 0
            if aux == 0:
                x = C_1
    
            elif aux == 3:
                x = C_4
        
            elif aux == 6:
                x = C_2
        
            elif aux == 9:
                x = C_4
        
            elif aux == 12:
                x = C_1
        
            elif aux == 15:
                x = C_5
        
            elif aux == 18:
                x = C_3
        
            elif aux == 21:
                x = C_5
            
            


        gameDisplay.fill((255,255,255))

        gameDisplay.blit(fundo, (posi_x,posi_y))
        
        gameDisplay.blit(x,(-70,crack_y))
        
        if aux == 21:
            aux = 0
        else:
            aux+=1
        
        if crack_y<500:
            vel_pulo -=1
            x = C_6
            
        
        
        if posi_x == -10000:
            gameOver = True
        
        pygame.display.update()

        print(crack_y)   

        clock.tick(30)



    pygame.quit()
    quit()
    


loopjogo()
        
            
            