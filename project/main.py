import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import pygame
import project

#
#
#Importante o comando sys vai servir para podermos chamar todos os modulos dentro da pasta projects
#
#
janela = project.menu.tela.iniciar_pygame()
continuar = True
pagina_atual = project.menu

while continuar:
        for event in pygame.event.get(): #pega os eventos
            if event.type == pygame.QUIT: #sair do jogo, esta aqui pois funciona em todas as telas
                continuar = False

            elif event.type == pygame.KEYDOWN:
                if event.key in pagina_atual.controles.definidos.keys(): #Procura a key na classe controles da pagina atual
                    #IMPORTANTE
                    #A tecla esta sendo chamada em ASCII
                    pagina_atual.controles.definidos[event.key](janela)
        
        pygame.display.flip()

