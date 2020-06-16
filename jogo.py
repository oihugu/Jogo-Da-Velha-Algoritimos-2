import pygame
import compartilhados

def  main(janela):
    compartilhados.tela_vazia(janela)
    #compartilhados.area_trabalhavel(janela)
    #compartilhados.area_trabalhavel_y(janela)
    largura, altura = pygame.display.get_surface().get_size()
    pygame.draw.rect(janela,    
    (0,0,0),
    [largura//20 * 9 ,(((altura//20)*4)), 5,altura - altura//3])
    pygame.draw.rect(janela,    
    (0,0,0),
    [largura//20 * 11 ,(((altura//20)*4)), 5,altura - altura//3])
    pygame.draw.rect(janela,    
        (0,0,0),
        [largura//4 + largura//7,altura//20 * 8, altura//2,5])
    pygame.draw.rect(janela,    
        (0,0,0),
        [largura//4 + largura//7,altura//20 * 12, altura//2,5])
    
    