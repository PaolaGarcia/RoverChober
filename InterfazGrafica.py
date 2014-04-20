# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 23:54:48 2012

@author: Paola y Diego
"""

import time
import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
import udpenvio as uuu

SCREEN_WIDTH = 690
SCREEN_WEIGHT = 400


#The following three definitions was used as a reference from the website: http://www.pygame.org/pcr/inputbox/
#---------------------------------------------------------------------------------------
def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message, x, y):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (255,255,255),(x,y,40,20), 0)
  pygame.draw.rect(screen, (255,255,255),(x,y,40,20), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (0,0,0)),
                (210, y+5))
  pygame.display.flip()

def ask(screen, question, y):
      "ask(screen, question) -> answer"
      pygame.font.init()
      current_string = []
      display_box(screen, question + "  " + string.join(current_string,""), 210,y)
      while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
          current_string = current_string[0:-1]
        elif inkey == K_RETURN:
          break
        elif inkey <= 57 and inkey >=48:
            if len(current_string) < 3:
              current_string.append(chr(inkey))
        display_box(screen, question + "  " + string.join(current_string,""), 210, y)
      return string.join(current_string,"")
    
#---------------------------------------------------------------------------------------
    

def metodo1(screen):
    # texto 1
    myfont = pygame.font.SysFont("Arial Black", 15)
    label = myfont.render("Distance (m): ", 1, (255,255,255))
    screen.blit(label, (80, 300))
    dato = ask(screen, "", 300)
    pygame.display.flip()
    return dato
    
def metodo2(screen):
    #texto 2
    myfont = pygame.font.SysFont("Arial Black", 15)
    label = myfont.render("    Degrees: ", 1, (255,255,255))
    screen.blit(label, (80, 300))
    dato = ask(screen, "", 300)
    pygame.display.flip()
    return dato

def instr(screen):
    myfont = pygame.font.SysFont("Arial Black", 16)
    label = myfont.render("Instructions: first, select the desired movement with the arrows of the ", 1, (255,255,255))
    screen.blit(label, (10, 10))
    label = myfont.render("keyboard. Then, enter desired distance/angle in the textbox below.", 1, (255,255,255))
    screen.blit(label, (10, 30))
    label = myfont.render("Press ESCAPE to return to menu", 1, (255,255,255))
    screen.blit(label, (10, 50))
    
    pygame.display.flip()

def flecha(screen, flechas, fondo, rover):
    screen.blit(fondo, (0,0))
    screen.blit(rover, (350,80))   
    screen.blit(flechas, (60,80))
    instr(screen)  
    pygame.display.flip()
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WEIGHT))
    pygame.display.set_caption("Rover")

    while True:
      tecla=pygame.key.get_pressed()
      inicio = pygame.image.load("inicio.png").convert()
      screen.blit(inicio, (0,0))
      pygame.display.flip()
      inkey = get_key()
      if inkey == K_1:
        delay = 1
        fondo = pygame.image.load("fondoLuna.png").convert_alpha()
        break
      elif inkey == K_2:
        delay = 294
        fondo = pygame.image.load("fondoMercurio.png").convert_alpha()
        break
      elif inkey == K_3:
        delay = 127
        fondo = pygame.image.load("fondoVenus.png").convert_alpha()
        break
      elif inkey == K_4:
        delay = 270
        fondo = pygame.image.load("fondoMarte.png").convert_alpha()
        break
      
    flechas1 = pygame.image.load("flechas1.png").convert_alpha()
    rover = pygame.image.load("rover.png").convert_alpha()

    screen.blit(fondo, (0,0))  
    screen.blit(flechas1, (60,80))
    screen.blit(rover, (350,80))
    pygame.display.flip()

    instr(screen)    
    
    while True:
        tecla=pygame.key.get_pressed()

        if tecla[K_ESCAPE]:
              while True:
                tecla=pygame.key.get_pressed()
                inicio = pygame.image.load("inicio.png").convert()
                screen.blit(inicio, (0,0))
                pygame.display.flip()
                inkey = get_key()
                if inkey == K_1:
                  delay = 1
                  fondo = pygame.image.load("fondoLuna.png").convert()
                  break
                elif inkey == K_2:
                  delay = 294
                  fondo = pygame.image.load("fondoMercurio.png").convert()
                  break
                elif inkey == K_3:
                  delay = 127
                  fondo = pygame.image.load("fondoVenus.png").convert()
                  break
                elif inkey == K_4:
                  delay = 270
                  fondo = pygame.image.load("fondoMarte.png").convert()
                  break
              screen.blit(fondo, (0,0))  
              screen.blit(flechas1, (60,80))
              screen.blit(rover, (350,80))
              pygame.display.flip()

              instr(screen) 
        
        elif tecla[K_LEFT]:
            flechas = pygame.image.load("flechas2.png").convert_alpha()   
            flecha(screen, flechas, fondo, rover) 
            dato = metodo2(screen)
            envio = "L%"+str(dato)
            flechas = pygame.image.load("flechas1.png").convert_alpha()
            flecha(screen, flechas, fondo, rover)
            time.sleep(delay)
            if len(envio) == 1:
                envio = "L%0"
            print envio
            #uuu.envia_udp(envio)

        elif tecla[K_RIGHT]:
            flechas = pygame.image.load("flechas3.png").convert_alpha()   
            flecha(screen, flechas, fondo, rover)
            dato = metodo2(screen)
            envio = "R%"+str(dato)
            flechas = pygame.image.load("flechas1.png").convert_alpha()
            flecha(screen, flechas, fondo, rover)
            time.sleep(delay)
            if len(envio) == 1:
                envio = "R%0"
            print envio
            #uuu.envia_udp(envio)

        elif tecla[K_DOWN]:
            flechas = pygame.image.load("flechas5.png").convert_alpha()
            flecha(screen, flechas, fondo, rover) 
            dato = metodo1(screen)
            envio = "D%"+str(dato)
            flechas = pygame.image.load("flechas1.png").convert_alpha()
            flecha(screen, flechas, fondo, rover)
            time.sleep(delay)
            if len(envio) == 1:
                envio = "D%0"
            print envio
            #uuu.envia_udp(envio)
                                
        elif tecla[K_UP]:    
            flechas = pygame.image.load("flechas4.png").convert_alpha()
            flecha(screen, flechas, fondo, rover)             
            dato = metodo1(screen)
            envio = "U%"+str(dato)
            flechas = pygame.image.load("flechas1.png").convert_alpha()
            flecha(screen, flechas, fondo, rover)
            time.sleep(delay)
            if len(envio) == 1:
                envio = "U%0"
            print envio
            #uuu.envia_udp(envio)


                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()


if __name__== "__main__":
    main()

    

