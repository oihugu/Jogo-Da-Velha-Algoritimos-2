import pygame
import compartilhados
import sqlite3


def main(janela, User):
    compartilhados.tela_vazia(janela)
    largura, altura = pygame.display.get_surface().get_size()
    base = (largura + altura)//2
    font = pygame.font.Font('visual/kashima.ttf', base//14)
    text = font.render("Ranking", True, (0, 0, 0))
    text_width, text_height = font.size("Ranking")
    janela.blit(text,
        (largura//20 * 6 - text_height,altura//20 + text_height//2))
    connection = sqlite3.connect('jogadores.db')
    cursor = connection.cursor()
    playes_list = []
    for row in cursor.execute('SELECT * FROM players ORDER BY potuacao'):
        playes_list.append(list(row))
    
    frame = 0

    while User.na_pagina_ranking:
        if frame == 0:
            if len(playes_list) >= 10:
                for registro in range(0, 10):
                    print(playes_list[registro])
            else:
                for registro in range(0,len(playes_list)):
                    font = pygame.font.Font('visual/kashima.ttf', base//25)
                    text = font.render(playes_list[registro][0], True, (0, 0, 0))
                    text_width, text_height = font.size(playes_list[registro][0])
                    janela.blit(text,
                (largura//20 * 7 - text_height, (altura//20 * (len(playes_list) - registro)) + text_height//2 + altura/6))

                for registro in range(0,len(playes_list)):
                    font = pygame.font.Font('visual/kashima.ttf', base//25)
                    text = font.render(playes_list[registro][1], True, (0, 0, 0))
                    text_width, text_height = font.size(playes_list[registro][1])
                    janela.blit(text,
                (largura//20 * 10 - text_height, (altura//20 * (len(playes_list) - registro)) + text_height//2 + altura/6))

                for registro in range(0,len(playes_list)):
                    font = pygame.font.Font('visual/kashima.ttf', base//25)
                    text = font.render(playes_list[registro][2], True, (0, 0, 0))
                    text_width, text_height = font.size(playes_list[registro][2])
                    janela.blit(text,
                (largura//20 * 13 - text_height, (altura//20 * (len(playes_list) - registro)) + text_height//2 + altura/6))
            pygame.display.flip()
        for event in pygame.event.get(): 
            if event.type== pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    User.na_pagina_menu = True
                    User.na_pagina_ranking = False
    return User