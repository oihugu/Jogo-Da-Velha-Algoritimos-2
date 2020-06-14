import pygame
import compartilhados
import ranking
import jogo
from pygame.locals import RESIZABLE

def tela_menu(janela):
    compartilhados.tela_vazia(janela)
    BLACK = (0, 0, 0)
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
