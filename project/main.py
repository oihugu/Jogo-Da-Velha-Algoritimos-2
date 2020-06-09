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
                if event.key in dir(pagina_atual.main.controles): #Procura a key na classe controles da pagina atual
                    evento = event.type
                    resultado_do_return = getattr(pagina_atual.main.controles, evento)() #chama o evento
        
        pygame.display.flip()

