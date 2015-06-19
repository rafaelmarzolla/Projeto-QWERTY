
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:24:18 2015

@author: Lucas
"""
import pygame
import os
import time
import sys

pygame.init()

black = (0,0,0)
green = (0,200,0)
white = (255,255,255)
red = (255,0,0)


display_width = 800
display_height = 672


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
C_7 = pygame.image.load("Craquinho_slide.png")
        
def gerador_texto(msg, color,y_displace = 0, size = "small"):
        textSurf, textRect = text_objects(msg,color,size)
        
        textRect.center = (display_width/2), (display_height /2)+y_displace
        gameDisplay.blit(textSurf, textRect)
    
smallfont = pygame.font.SysFont("comicsnsms", 25) #Tamanho da fonte
medfont = pygame.font.SysFont("comicsnsms", 50)
largefont = pygame.font.SysFont("comicsnsms", 80)



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
        gerador_texto("QWERTY",green,y_displace=-100,size="large")
    
        gerador_texto("The objective of the game is to reach the end", black, y_displace = -30, size="small")
    
       
        gerador_texto("Press P to play or Q to quit",black,y_displace=10,size = "medium")
    
        pygame.display.update()


def text_objects(text,color,size):
    if size=="small":
        textSurface = smallfont.render(text,True,color)
    if size=="medium":
        textSurface = medfont.render(text,True,color)
    if size=="large":
        textSurface = largefont.render(text,True,color)
    
    
    
    
    
    return textSurface, textSurface.get_rect()
    
pygame.mixer.music.load(os.path.join('rainning_blood.mp3'))
fundo = pygame.image.load(os.path.join('level_1.png'))

def loopjogo():
    aux = 0
    counter = 0
    craquinho = []
    aux_slide = 0
    gameExit = False
    gameOver = False
    
    beginmove = False
    
    posi_x = 0
    posi_y = 0
    
    vel_inicial = 0
    trajetoria_objeto = 840
    crack_y = 500
    vel_pulo = 0
    
    pygame.mixer.music.play()

    
   
    
    while gameExit == False:
        while gameOver == True:
            pygame.mixer.music.stop()
            gameDisplay.fill((255,255,255))
            gerador_texto("Fim de jogo, pressione P para jogar denovo ou S para sair", (red))
            
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
                    vel_inicial = 7
                    beginmove = True
                    
                     
                if crack_y >=500:
                    if i.key == pygame.K_SPACE:
                         vel_pulo = 22
                    if i.key == pygame.K_DOWN:
                        while aux_slide<20:
                            x = C_7
                            aux_slide+=1
                            if aux_slide == 20:
                                aux_slide = 0
                        
            
        
        crack_y -= vel_pulo      #gravidade
        posi_x -= vel_inicial      #movimento horizontal da tela
        
        if crack_y >= 500:      #definindo a ordem dos sprites do personagem
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
        
        craquinho.append(gameDisplay.blit(x,(-10,crack_y)))
        craquinho[0]
        

        
    
        
        if aux == 21:   #o executador dos sprites
            aux = 0
        else:
            aux+=0.5


        if crack_y<500:
            vel_pulo -=1
            x = C_6
        
        counter+=1
        if beginmove == True:
            trajetoria_objeto -=7
        
        
        if posi_x == -9793:
            gameOver = True
        
        pygame.display.update()

        del craquinho[-1]
 

        clock.tick(60)



    pygame.quit()
    sys.exit()
    

game_intro()
loopjogo()
        
            