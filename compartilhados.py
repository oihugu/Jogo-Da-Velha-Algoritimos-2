import pygame

def tela_vazia(janela):
    janela.fill((255, 192, 203))
    largura, altura = pygame.display.get_surface().get_size()
    ##galhos
    ofuda = pygame.image.load(r'visual/ofuda.png')
    ofuda_tamanho= (400//3, 1185//3)
    ofuda_transformado = pygame.transform.scale(ofuda, ofuda_tamanho)
    posicao_relativa = (largura -  ofuda_tamanho[0]//0.75, altura//2 - ofuda_tamanho[1]//2)
    janela.blit(ofuda_transformado, posicao_relativa)
    ##arvore
    arvore = pygame.image.load(r'visual/arvore.png')
    arvore_tamanho= (417//2, 532//2)
    arvore_transformado = pygame.transform.scale(arvore, arvore_tamanho)
    posicao_relativa = (0, altura- arvore_tamanho[1] + 10)
    janela.blit(arvore_transformado, posicao_relativa)