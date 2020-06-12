import pygame
import compartilhados
#import sqlite3


def main(janela):
    compartilhados.tela_vazia(janela)
    largura, altura = pygame.display.get_surface().get_size()
    base = (largura + altura)//2
    font = pygame.font.Font('visual/kashima.ttf', base//14)
    text = font.render("Ranking", True, (0, 0, 0))
    text_width, text_height = font.size("txt")
    janela.blit(text,
        (largura//20 * 6 - text_height,altura//20 + text_height//2))
 #   connection = sqlite3.connect('db/jogadores.db')
  #  cursor = connection.cursor()
   # cursor.execute('''CREATE TABLE players
             (nome, potuacao, data)''')
