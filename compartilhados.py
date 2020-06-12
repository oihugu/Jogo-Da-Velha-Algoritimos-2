import pygame

def tela_vazia(janela):
    janela.fill((255, 192, 203))
    largura, altura = pygame.display.get_surface().get_size()
    ##ofuda
    ofuda = pygame.image.load(r'visual/ofuda.png')
    ofuda_tamanho= (400//3, 1185//3)
    ofuda_transformado = pygame.transform.scale(ofuda, ofuda_tamanho)
    posicao_relativa = (largura -  ofuda_tamanho[0]//0.75, altura//2 - ofuda_tamanho[1]//2)
    janela.blit(ofuda_transformado, posicao_relativa)

    pygame.draw.rect(janela,
    (0,0,0),
    [largura -  ofuda_tamanho[0]//3,altura//2 - ofuda_tamanho[1]//2,5,ofuda_tamanho[1]])
    pygame.draw.rect(janela,
    (0,0,0),
    [largura - ofuda_tamanho[0] - ofuda_tamanho[0]//3 ,altura//2 - ofuda_tamanho[1]//2,5,ofuda_tamanho[1]])
    pygame.draw.rect(janela,
    (0,0,0),
    [largura - ofuda_tamanho[0] - ofuda_tamanho[0]//3 ,altura//2 - ofuda_tamanho[1]//2,ofuda_tamanho[0],5])
    pygame.draw.rect(janela,    
    (0,0,0),
    [largura - ofuda_tamanho[0] - ofuda_tamanho[0]//3 ,altura//2 + ofuda_tamanho[1]//2 - 4,ofuda_tamanho[0],5])
    ##arvore
    arvore = pygame.image.load(r'visual/arvore.png')
    arvore_tamanho= (417//2, 532//2)
    arvore_transformado = pygame.transform.scale(arvore, arvore_tamanho)
    posicao_relativa = (0, altura- arvore_tamanho[1] + 10)
    janela.blit(arvore_transformado, posicao_relativa)

class User:
    def __init__(self):
        self.na_pagina_menu = True
        self.na_pagina_ranking = False
        self.na_pagina_jogo = False
        self.pontuacao = 0


def area_trabalhavel(janela):
    largura, altura = pygame.display.get_surface().get_size()
    pygame.draw.rect(janela,    
    (0,0,200),
    [largura//20 * 7 ,altura//2, 5,altura])
    pygame.draw.rect(janela,    
    (0,0,200),
    [largura//20 * 13 ,altura//2, 5,altura])