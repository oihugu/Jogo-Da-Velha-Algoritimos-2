import pygame
from pygame.locals import *
import os

def iniciar_pygame(tamanho):
    janela = pygame.display.set_mode(tamanho, RESIZABLE)
    janela.fill((255, 192, 203))
    fundo_padrao(janela,tamanho)
    return janela

def fundo_padrao(janela,tamanho):
    janela.fill((255, 192, 203))
    oni = pygame.image.load('oni.png')
    base = int((int(tamanho[0]) + int(tamanho[1]))/2)
    oni = pygame.transform.scale(oni, (int(base/13), int(base/10)))
    janela.blit(oni, (360,240))
