import pygame
import compartilhados
import ranking
from pygame.locals import RESIZABLE


altura, largura = 1200,500

pygame.init()
pygame.display.set_caption("Jogo da Velha")
janela = pygame.display.set_mode((altura, largura))
compartilhados.tela_vazia(janela)

User = compartilhados.User
continuar = True


while continuar:
    for event in pygame.event.get(): #pega os eventos
        if event.type == pygame.QUIT:
            continuar = False

        elif event.type == pygame.VIDEORESIZE:
            altura, largura = event.size
            compartilhados.tela_vazia(janela)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                pagina_atual = ranking
                User.na_pagina_menu = False
                User.na_pagina_ranking = True
                ranking.main(janela)
                    
        
        pygame.display.flip()