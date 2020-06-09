import pygame

def iniciar_pygame():
    pygame.init()
    janela = pygame.display.set_mode((720,480))
    pygame.display.set_caption("Jogo da Velha")
    janela.fill((255, 192, 203))
    
    return janela