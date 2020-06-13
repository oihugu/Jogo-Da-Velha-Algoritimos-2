import pygame

def tela_vazia(janela):
    BLACK = (0, 0, 0)
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
    pygame.display.flip()
    ##menu
    menu = pygame.draw.rect(janela, BLACK, (320, 60, 550, 350), 3)
    ##título
    largura, altura = pygame.display.get_surface().get_size()
    base = (largura + altura)//2
    font = pygame.font.Font('visual/kashima.ttf', base//14)
    text = font.render("Jogo da Velha", True, (0, 0, 0))
    text_width, text_height = font.size("Jogo da Velha")
    janela.blit(text,
        (largura//15 * 6 - text_height,altura//10 + text_height//2))
    ##opção - jogar
    largura, altura = pygame.display.get_surface().get_size()
    base = (largura + altura)//2
    font = pygame.font.Font('visual/kashima.ttf', base//14)
    text = font.render("Jogar", True, (0, 0, 0))
    text_width, text_height = font.size("Jogar")
    janela.blit(text,
        (largura//12.3 *6 - text_height,altura//5 + text_height//1))
    ##opção - creditos
    largura, altura = pygame.display.get_surface().get_size()
    base = (largura + altura)//2
    font = pygame.font.Font('visual/kashima.ttf', base//14)
    text = font.render("Creditos", True, (0, 0, 0))
    text_width, text_height = font.size("Creditos")
    janela.blit(text,
        (largura//13.2 *6 - text_height,altura//2 + text_height//1))
    ##opção - ranking
    largura, altura = pygame.display.get_surface().get_size()
    base = (largura + altura)//2
    font = pygame.font.Font('visual/kashima.ttf', base//14)
    text = font.render("Ranking", True, (0, 0, 0))
    text_width, text_height = font.size("Ranking")
    janela.blit(text,
        (largura//13 *6 - text_height,altura//2.9 + text_height//1))

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