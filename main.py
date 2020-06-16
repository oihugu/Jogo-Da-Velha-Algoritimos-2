import pygame
import compartilhados
import ranking
import jogo
import menu
from pygame.locals import RESIZABLE


altura, largura = 1200,500

pygame.init()
pygame.display.set_caption("Jogo da Velha")
janela = pygame.display.set_mode((altura, largura))
menu.main(janela)

compartilhados.gerar_icone(janela)

User = compartilhados.User
continuar = True


while continuar:
    for event in pygame.event.get(): #pega os eventos
        if event.type == pygame.QUIT:
            continuar = False

        elif event.type == pygame.VIDEORESIZE:
            altura, largura = event.size
            #compartilhados.tela_vazia(janela)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                pagina_atual = ranking
                User.na_pagina_menu = False
                User.na_pagina_ranking = True
                ranking.main(janela)
            if event.key == pygame.K_j:
                pagina_atual = jogo
                User.na_pagina_menu = False
                User.na_pagina_jogo = True
                jogo.main(janela)
            if event.key == pygame.K_m:
                pagina_atual = jogo
                User.na_pagina_menu = True
                User.na_pagina_jogo = False
                User.na_pagina_ranking = False
                menu.main(janela)

                    
        
        pygame.display.flip()