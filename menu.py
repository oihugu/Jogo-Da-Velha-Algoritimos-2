import pygame
import compartilhados
from pygame.locals import RESIZABLE


altura, largura = 1000,600

pygame.init()
pygame.display.set_caption("Jogo da Velha")
janela = pygame.display.set_mode((altura, largura))
compartilhados.tela_vazia(janela)


continuar = True



while continuar:
        for event in pygame.event.get(): #pega os eventos
            if event.type == pygame.QUIT: #sair do jogo, esta aqui pois funciona em todas as telas
                continuar = False

            elif event.type == pygame.VIDEORESIZE:
                altura, largura = event.size
                compartilhados.tela_vazia(janela)

            elif event.type == pygame.KEYDOWN:
                pass
                    
        
        pygame.display.flip()