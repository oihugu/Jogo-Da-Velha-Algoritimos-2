import pygame
import compartilhados
import ranking
import jogo
from pygame.locals import RESIZABLE

def main(janela, User):
    BLACK = (0, 0, 0)
    ##título
    largura, altura = pygame.display.get_surface().get_size()
    base = (largura + altura)//2
    font = pygame.font.Font('visual/kashima.ttf', base//14)
    text = font.render("Jogo da Velha", True, (0, 0, 0))
    text_width, text_height = font.size("Jogo da Velha")
    ##opção - jogar
    text_jogar = font.render("Jogar", True, (0, 0, 0))
    text_jogar_width, text_jogar_height = font.size("Jogar")
    ##opção - creditos
    text_creditos = font.render("Creditos", True, (0, 0, 0))
    text_creditos_width, text_creditos_height = font.size("Creditos")
    
    ##opção - ranking
    text_ranking = font.render("Ranking", True, (0, 0, 0))
    text_ranking_width, text_ranking_height = font.size("Ranking")
    frame = 0
    while User.na_pagina_menu:
        if frame % 60 == 0:
            compartilhados.tela_vazia(janela)
            janela.blit(text,
                (largura//15 * 6 - text_height,altura//10 + text_height//2))
            janela.blit(text_jogar,
                (largura//12.3 *6 - text_jogar_height,altura//5 + text_jogar_height//1))
            janela.blit(text_creditos,
                (largura//13.2 *6 - text_creditos_height,altura//2 + text_creditos_height//1))
            janela.blit(text_ranking,
                (largura//13 *6 - text_ranking_height,altura//2.9 + text_ranking_height//1))
        
        for event in pygame.event.get(): 
            if event.type== pygame.QUIT:
                sys.exit()
            jogar = text_jogar.get_rect().move((largura//12.3 *6 - text_jogar_height,altura//5 + text_jogar_height//1))
            if jogar.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    User.na_pagina_jogo = True
                    User.na_pagina_menu = False
                    jogo.main(janela, User)
            rank = text_ranking.get_rect().move((largura//13 *6 - text_ranking_height,altura//2.9 + text_ranking_height//1))
            if rank.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    User.na_pagina_ranking = True
                    User.na_pagina_menu = False
                    ranking.main(janela, User)
            credit = text_creditos.get_rect().move((largura//13.2 *6 - text_creditos_height,altura//2 + text_creditos_height//1))
            if credit.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    #COLOCAR LINK PARA MAIN DE CREDITOS AQUI
                    print('creditos')
                    pass

        frame += 1
        pygame.display.flip()