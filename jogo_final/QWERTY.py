
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:24:18 2015

@author: Lucas
"""
import pygame
import os
import time
import sys
import random

pygame.init()

black = (0,0,0)
green = (0,200,0)
white = (255,255,255)
red = (255,0,0)


display_width = 800
display_height = 626


clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Temple Crack")



C_1 = pygame.image.load("Craquinho_parado.png")
C_2 = pygame.image.load("Craquinho_correndo_1.png")
C_3 = pygame.image.load("Craquinho_correndo_2.png")
C_4 = pygame.image.load("Craquinho_semicorrendo_1.png")
C_5 = pygame.image.load("Craquinho_semicorrendo_2.png")
C_6 = pygame.image.load("craquinho_voando.png")
C_7 = pygame.image.load("Craquinho_slide.png")

pygame.mixer.music.load(os.path.join('the_trooper.mp3'))
fundo = pygame.image.load(os.path.join('levelcrack.png'))


def gerador_texto(msg,color,y_displace=0,size= "small"):   #texto na tela e cor
    def text_objects(text,color,size):
        smallfont = pygame.font.SysFont("comicsnsms", 25) #Tamanho da fonte
        medfont = pygame.font.SysFont("comicsnsms", 50)
        largefont = pygame.font.SysFont("comicsnsms", 80)
        if size=="small":
            textSurface = smallfont.render(text,True,color)
        if size=="medium":
            textSurface = medfont.render(text,True,color)
        if size=="large":
            textSurface = largefont.render(text,True,color)
       
        return textSurface, textSurface.get_rect()
    
    textSurf, textRect = text_objects(msg,color,size)
        
       
    textRect.center = (display_width/2), (display_height /2)+y_displace
    gameDisplay.blit(textSurf, textRect)


    
    
    
def gerador_objetos(counter, trajetoria_objeto, lista_movimento, random_objeto_cor, random_objeto_pos_y, random_objeto_tamanho_x, objeto_tamanho_y):
            
    if len(lista_movimento) >= 1 and len(lista_movimento) < 300:
        lista_movimento.append(counter)
        pygame.draw.rect(gameDisplay, random_objeto_cor, [trajetoria_objeto, random_objeto_pos_y, random_objeto_tamanho_x, objeto_tamanho_y])
    if len(lista_movimento) >= 300:
        del lista_movimento[:]
       
            
            
            


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
#        gerador_texto("If you run into the edges or yourself,you die!", red, y_displace = -50,size = "small")
        gerador_texto("Press P to play or Q to quit",black,y_displace=10,size = "medium")
    
        pygame.display.update()
        
        


def loopjogo():
    objeto_tamanho_x = [100,120,180]
    objeto_tamanho_y = 100
    objeto_cor = [green, red, black]
    objeto_pos_y = [430,477]
    
    random_objeto_tamanho_x = random.choice(objeto_tamanho_x)
    random_objeto_cor = random.choice(objeto_cor)
    random_objeto_pos_y = random.choice(objeto_pos_y)
    
    
    aux = 0
    counter = 0
    placar = 0
 
    aux_slide = 0
    aux_andar = True


    gameExit = False
    gameOver = False

    lista_movimento = []

    beginmove = False

    
    posi_y = -50
    
    vel_inicial = 0
    trajetoria_objeto = 840
    y_fundo = 840
   
    crack_x = 0

    crack_y = 430
    vel_pulo = 0
    
    pygame.mixer.music.play()

    
   
    
    while gameExit == False:
        while gameOver == True:
            pygame.mixer.music.stop()
            gameDisplay.fill((255,255,255))
            gerador_texto("You lost! Press P to play again or S to quit", red, y_displace = 40, size="small")
            gerador_texto("Your score was:", red, y_displace = -150, size="medium")
            gerador_texto(str(placar), black, y_displace = -70, size="large")
            
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
                    vel_inicial = 14
                    beginmove = True
                    
                     
                if crack_y >=430:
                    if i.key == pygame.K_UP:
                         vel_pulo = 28
                         
                    if i.key == pygame.K_DOWN:
                        slide = True
                        
                        if slide:
                            aux_slide = 50
                            x = C_7
            
        
        crack_y -= vel_pulo      #gravidade
        trajetoria_objeto -= vel_inicial #movimento dos objetos
        y_fundo -= vel_inicial

        
        
        if aux_andar:
            if crack_y >= 430:      #definindo a ordem dos sprites do personagem
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
            
        
        
        if counter % 156 == 0:       
            y_fundo = 840
        gameDisplay.blit(fundo, (y_fundo-840,posi_y))
        gameDisplay.blit(fundo, (y_fundo+200,posi_y))
        
 
       
        gameDisplay.blit(x,(crack_x,crack_y + 50))
        


        if counter % 150 == 0:
            lista_movimento.append(counter)
            trajetoria_objeto = 840
            random_objeto_tamanho_x = random.choice(objeto_tamanho_x)
            random_objeto_cor = random.choice(objeto_cor)
            random_objeto_pos_y = random.choice(objeto_pos_y)
        gerador_objetos(counter, trajetoria_objeto, lista_movimento, random_objeto_cor, random_objeto_pos_y, random_objeto_tamanho_x, objeto_tamanho_y)

        
        
    
        
        if aux == 21:   #o executador dos sprites
            aux = 0
        else:
            aux+=0.5
            
        
        if aux_slide > 0:
            x = C_7
            aux_slide-=1
            aux_andar = False
        if aux_slide == 0:
            slide = False
            aux_andar = True  
           
           

        if crack_y<430:  #o executador da gravidade do pulo do personagem
            vel_pulo -=2
            x = C_6

        
        if beginmove == False:
            gerador_texto("Are your ready? press P again and good luck!", black, y_displace = -30, size="small")
        if beginmove == True:
            counter+=1     #contador "relogio" do game. Usado para multiplas funcionalidades

            if counter % 10 == 0:
                placar+=1
                
        gerador_texto(str(placar), black, y_displace = -300, size="small")
        
        if slide:
            if crack_y + 47 == random_objeto_pos_y:
                if trajetoria_objeto == crack_x + 11*vel_inicial:
                    gameOver = True
            
                
        else:
            for i in range(crack_y, crack_y + 48):
                if i == random_objeto_pos_y:
                    for i in range (trajetoria_objeto,trajetoria_objeto + random_objeto_tamanho_x + 50):
                        if i == crack_x + 9*vel_inicial:
                            gameOver = True
            
            

        pygame.display.update()
        clock.tick(60)



    pygame.quit()
    sys.exit()
    

game_intro()
loopjogo()
        
            