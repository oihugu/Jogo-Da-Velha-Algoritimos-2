import pygame, sys
import compartilhados
from pygame.locals import*
import menu
import sqlite3
import datetime





def  main(janela, User):
	class jogo_all:
		def __init__(self):
			self.jogadorBola = True
			self.jogadorXis = False
			self.contadorPontosBola = 0
			self.contadorPontosXis = 0
			self.casas = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
			self.contJogadas = 0
			self.nome_x = 'Jogador X'
			self.nome_O ='Jogador O'
			self.active = False
			self.active_o = False

	jogo_all = jogo_all()
	compartilhados.tela_vazia(janela)
	#compartilhados.area_trabalhavel(janela)
	#compartilhados.area_trabalhavel_y(janela)
	largura, altura = pygame.display.get_surface().get_size()
	
	contador = 0 
	saiu_do_jogo = False
	while User.na_pagina_jogo:
		if contador == 0:
			jogo_all,terminou, comecou, saiu_do_jogo = a(jogo_all, False, True, janela, contador, saiu_do_jogo)
			contador += 1
		else:
			jogo_all,terminou, comecou, saiu_do_jogo = a(jogo_all, terminou, comecou, janela, contador, saiu_do_jogo)
			contador += 1
		if saiu_do_jogo:
			connection = sqlite3.connect('jogadores.db')
			cursor = connection.cursor()
			querry = f'INSERT INTO players(nome, potuacao, data) VALUES(\'{jogo_all.nome_x}\', \'{jogo_all.contadorPontosXis}\', \'{datetime.date.today()}\'), (\'{jogo_all.nome_O}\', \'{jogo_all.contadorPontosBola}\', \'{datetime.date.today()}\');'
			cursor.execute(querry)
			connection.commit()
			connection.close()
			User.na_pagina_menu = True
			User.na_pagina_jogo = False
			return User
			



def a(jogo_all, terminou,comecou, tela, frame, saiu_do_jogo):
	desvio = 250
	desvio_y = 50
	xis = pygame.image.load('visual/sakura2.png')
	bola = pygame.image.load('visual/oni2.png')

	text = pygame.font.Font('visual/kashima.ttf', 32)

	aviso = pygame.Surface((0,0))
	pontosJogadorXis = text.render(f"{jogo_all.nome_x} = " +str(jogo_all.contadorPontosXis), True, (0,0,0))
	pontosJogadorBola = text.render(f"{jogo_all.nome_O} = " +str(jogo_all.contadorPontosBola), True, (0,0,0))


	posX = -50
	posY = -50


	posicoes = [(desvio + 80,desvio_y + 45),(desvio + 250,desvio_y + 45),(desvio + 430,desvio_y + 45),
				(desvio + 80,desvio_y + 180),(desvio + 250,desvio_y + 180),(desvio + 430,desvio_y + 180),
				(desvio + 80,desvio_y + 325),(desvio + 250,desvio_y + 325),(desvio + 430,desvio_y + 325)]

	jogada = True


	for event in pygame.event.get(): 
		if event.type==QUIT:
			sys.exit()
		
		
		posX = pygame.mouse.get_pos()[0]
		posY = pygame.mouse.get_pos()[1]
		
	
		teclas  = pygame.key.get_pressed()
	
		if terminou == False and comecou == True:
			if ((posX >= desvio + 81 and posX <= desvio + 195) and (posY >= desvio_y + 50 and posY <= desvio_y + 144)):	
				if jogo_all.casas[0] == -1:
					if (pygame.mouse.get_pressed()[0] or teclas[K_LEFT]) and jogo_all.jogadorBola == True:
						jogo_all.casas[0] = 0

						jogo_all.jogadorBola = False
						jogo_all.jogadorXis = True
						jogo_all.contJogadas+=1
						
					elif pygame.mouse.get_pressed()[2] and jogo_all.jogadorXis == True:
						jogo_all.casas[0] = 1
						jogo_all.jogadorBola = True
						jogo_all.jogadorXis = False
						jogo_all.contJogadas +=1
						

			if ((posX >= desvio + 203 and posX <= desvio + 398) and (posY >= desvio_y + 50 and posY <= desvio_y + 144)):	
				if jogo_all.casas[1] == -1:
					if pygame.mouse.get_pressed()[0] and jogo_all.jogadorBola == True:
						jogo_all.casas[1] = 0
						jogo_all.jogadorBola = False
						jogo_all.jogadorXis = True
						jogo_all.contJogadas+=1
						
					elif pygame.mouse.get_pressed()[2] and jogo_all.jogadorXis == True:
						jogo_all.casas[1] = 1
						jogo_all.jogadorBola = True
						jogo_all.jogadorXis = False
						jogo_all.contJogadas +=1
											
					
			if ((posX >= desvio + 404 and posX <= desvio + 531) and (posY >= desvio_y + 50 and posY <= desvio_y + 144)):	
				if jogo_all.casas[2] == -1:
					if pygame.mouse.get_pressed()[0] and jogo_all.jogadorBola == True:
						jogo_all.casas[2] = 0
						jogo_all.jogadorBola = False
						jogo_all.jogadorXis = True
						jogo_all.contJogadas+=1
						
					elif pygame.mouse.get_pressed()[2] and jogo_all.jogadorXis == True:
						jogo_all.casas[2] = 1
						jogo_all.jogadorBola = True
						jogo_all.jogadorXis = False
						jogo_all.contJogadas +=1
						

			if ((posX >= desvio + 81 and posX <= desvio + 195) and (posY >= desvio_y + 153 and posY <= desvio_y + 295)):	
				if jogo_all.casas[3] == -1:
					if pygame.mouse.get_pressed()[0] and jogo_all.jogadorBola == True:
						jogo_all.casas[3] = 0
						jogo_all.jogadorBola = False
						jogo_all.jogadorXis = True
						jogo_all.contJogadas+=1
						
					elif pygame.mouse.get_pressed()[2] and jogo_all.jogadorXis == True:
						jogo_all.casas[3] = 1
						jogo_all.jogadorBola = True
						jogo_all.jogadorXis = False
						jogo_all.contJogadas +=1
						


			if ((posX >= desvio + 203 and posX <= desvio + 398) and (posY >= desvio_y + 153 and posY <= desvio_y + 295)):	
				if jogo_all.casas[4] == -1:
					if pygame.mouse.get_pressed()[0] and jogo_all.jogadorBola == True:
						jogo_all.casas[4] = 0
						jogo_all.jogadorBola = False
						jogo_all.jogadorXis = True
						jogo_all.contJogadas+=1
						
					elif pygame.mouse.get_pressed()[2] and jogo_all.jogadorXis == True:
						jogo_all.casas[4] = 1
						jogo_all.jogadorBola = True
						jogo_all.jogadorXis = False
						jogo_all.contJogadas +=1
						

			if ((posX >= desvio + 404 and posX <= desvio + 531) and (posY >= desvio_y + 153 and posY <= desvio_y + 295)):	
				if jogo_all.casas[5] == -1:
					if pygame.mouse.get_pressed()[0] and jogo_all.jogadorBola == True:
						jogo_all.casas[5] = 0
						jogo_all.jogadorBola = False
						jogo_all.jogadorXis = True
						jogo_all.contJogadas+=1
						
					elif pygame.mouse.get_pressed()[2] and jogo_all.jogadorXis == True:
						jogo_all.casas[5] = 1
						jogo_all.jogadorBola = True
						jogo_all.jogadorXis = False
						jogo_all.contJogadas +=1
						

			if ((posX >= desvio + 81 and posX <= desvio + 195) and (posY >= desvio_y + 304 and posY <= desvio_y + 420)):	
				if jogo_all.casas[6] == -1:
					if pygame.mouse.get_pressed()[0] and jogo_all.jogadorBola == True:
						jogo_all.casas[6] = 0
						jogo_all.jogadorBola = False
						jogo_all.jogadorXis = True
						jogo_all.contJogadas +=1
						
					elif pygame.mouse.get_pressed()[2] and jogo_all.jogadorXis == True:
						jogo_all.casas[6] = 1
						jogo_all.jogadorBola = True
						jogo_all.jogadorXis = False
						jogo_all.contJogadas +=1
						

			if ((posX >= desvio + 203 and posX <= desvio + 398) and (posY >= desvio_y + 304 and posY <= desvio_y + 420)):	
				if jogo_all.casas[7] == -1:
					if pygame.mouse.get_pressed()[0] and jogo_all.jogadorBola == True:
						jogo_all.casas[7] = 0
						jogo_all.jogadorBola = False
						jogo_all.jogadorXis = True
						jogo_all.contJogadas +=1
						
					elif pygame.mouse.get_pressed()[2] and jogo_all.jogadorXis == True:
						jogo_all.casas[7] = 1
						jogo_all.jogadorBola = True
						jogo_all.jogadorXis = False
						jogo_all.contJogadas +=1
						

			if ((posX >= desvio + 404 and posX <= desvio + 531) and (posY >= desvio_y + 304 and posY <= desvio_y + 420)):	
				if jogo_all.casas[8] == -1:
					if pygame.mouse.get_pressed()[0] and jogo_all.jogadorBola == True:
						jogo_all.casas[8] = 0
						jogo_all.jogadorBola = False
						jogo_all.jogadorXis = True
						jogo_all.contJogadas +=1
						
					elif pygame.mouse.get_pressed()[2] and jogo_all.jogadorXis == True:
						jogo_all.casas[8] = 1
						jogo_all.jogadorBola = True
						jogo_all.jogadorXis = False
						jogo_all.contJogadas +=1
			#REGRA DE NEGOCIO
			if (jogo_all.casas[0] == 1 and jogo_all.casas[1] == 1 and jogo_all.casas[2] == 1) or (jogo_all.casas[3] == 1 and jogo_all.casas[4] == 1 and jogo_all.casas[5] == 1) or (jogo_all.casas[6] == 1 and jogo_all.casas[7] == 1 and jogo_all.casas[8] == 1) or (jogo_all.casas[0] == 1 and jogo_all.casas[3] == 1 and jogo_all.casas[6] == 1) or (jogo_all.casas[1] == 1 and jogo_all.casas[4] == 1 and jogo_all.casas[7] == 1) or (jogo_all.casas[2] == 1 and jogo_all.casas[5] == 1 and jogo_all.casas[8] == 1) or (jogo_all.casas[0] == 1 and jogo_all.casas[4] == 1 and jogo_all.casas[8] == 1) or (jogo_all.casas[2] == 1 and jogo_all.casas[4] == 1 and jogo_all.casas[6] == 1):
				aviso = text.render(f"{jogo_all.nome_x} Ganhou ", True, (0, 0, 0))
				terminou = True
				comecou=False
				jogo_all.contadorPontosXis +=1
				pontosJogadorXis = text.render(f"{jogo_all.nome_x} = " +str(jogo_all.contadorPontosXis), True, (0,0,0))
				pontosJogadorBola = text.render(f"{jogo_all.nome_O} = " +str(jogo_all.contadorPontosBola), True, (0,0,0))
	
				
			
			
			elif (jogo_all.casas[0] == 0 and jogo_all.casas[1] == 0 and jogo_all.casas[2] == 0) or (jogo_all.casas[3] == 0 and jogo_all.casas[4] == 0 and jogo_all.casas[5] == 0) or (jogo_all.casas[6] == 0 and jogo_all.casas[7] == 0 and jogo_all.casas[8] == 0) or (jogo_all.casas[0] == 0 and jogo_all.casas[3] == 0 and jogo_all.casas[6] == 0) or (jogo_all.casas[1] == 0 and jogo_all.casas[4] == 0 and jogo_all.casas[7] == 0) or (jogo_all.casas[2] == 0 and jogo_all.casas[5] == 0 and jogo_all.casas[8] == 0) or (jogo_all.casas[0] == 0 and jogo_all.casas[4] == 0 and jogo_all.casas[8] == 0) or (jogo_all.casas[2] == 0 and jogo_all.casas[4] == 0 and jogo_all.casas[6] == 0):
					aviso = text.render(f"{jogo_all.nome_O} Ganhou ", True, (0, 0, 0))
					terminou = True
					comecou=False
					jogo_all.contadorPontosBola +=1
					pontosJogadorXis = text.render(f"{jogo_all.nome_x} = "+str(jogo_all.contadorPontosXis), True, (0,0,0))
					pontosJogadorBola = text.render(f"{jogo_all.nome_O} = "+str(jogo_all.contadorPontosBola), True, (0,0,0))					
					
			elif jogo_all.contJogadas >= 9:
					aviso = text.render("Empate", True, (0, 0, 0))
					terminou = True
					terminou = True
					comecou=False
		


		J_x = pontosJogadorXis.get_rect().move((desvio + 440,10))
		if J_x.collidepoint(pygame.mouse.get_pos()):
			if pygame.mouse.get_pressed()[0]:
				jogo_all.active = not jogo_all.active
		else:
			jogo_all.active = False
		if event.type == pygame.KEYDOWN and jogo_all.active:
			if event.key == pygame.K_RETURN:
				jogo_all.active = False
			elif event.key == pygame.K_BACKSPACE:
				jogo_all.nome_x = jogo_all.nome_x[:-1]
			else:
				jogo_all.nome_x += event.unicode
			J_x = pontosJogadorXis.get_rect().move((desvio + 440,10))

		J_o = pontosJogadorBola.get_rect().move((desvio + 10,10))
		if J_o.collidepoint(pygame.mouse.get_pos()):
			if pygame.mouse.get_pressed()[0]:
				print('ativado')
				jogo_all.active_o = not jogo_all.active_o
		else:
			jogo_all.active_o = False
		if event.type == pygame.KEYDOWN and jogo_all.active_o:
			if event.key == pygame.K_RETURN:
				jogo_all.active_o = False
			elif event.key == pygame.K_BACKSPACE:
				jogo_all.nome_O = jogo_all.nome_O[:-1]
			else:
				jogo_all.nome_O += event.unicode

		
	
		
	
	if comecou==False:
		novoJogo = text.render("Reiniciar", True, (0,0,0))
		novoJogoRect = novoJogo.get_rect().move(desvio + 10,30)
		sair_sprite = text.render("Sair", True, (0,0,0))
		sair = sair_sprite.get_rect().move(desvio + 440,30)
	
	elif comecou==True:
		novoJogo = pygame.Surface((0,0))
		sair_sprite = pygame.Surface((0,0))
		pontosJogadorBola = text.render(f"{jogo_all.nome_O} = " +str(jogo_all.contadorPontosBola), True, (0,0,0))
		pontosJogadorXis = text.render(f"{jogo_all.nome_x} = " +str(jogo_all.contadorPontosXis), True, (0,0,0))	
	novoJogoRect = novoJogo.get_rect().move(desvio + 10,30)
	sair = sair_sprite.get_rect().move(desvio + 440,30)
		
	if novoJogoRect.collidepoint(pygame.mouse.get_pos()) and terminou!=False:
		novoJogo = text.render("Reiniciar", True, (255,0,0))
		if pygame.mouse.get_pressed()[0]:
			comecou=True
			terminou=False
			jogo_all.contJogadas=0
			jogo_all.casas = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
			aviso = pygame.Surface((0,0))
	if sair.collidepoint(pygame.mouse.get_pos()) and terminou!=False:
		sair_sprite = text.render("Sair", True, (255,0,0))
		if pygame.mouse.get_pressed()[0]:
			saiu_do_jogo = True
	
	if frame % 60 == 0:
		compartilhados.tela_vazia(tela)


	tela.blit(aviso,(desvio + 230,30))
	tela.blit(novoJogo,(desvio + 10,30))
	tela.blit(sair_sprite,(desvio + 440,30))
	tela.blit(pontosJogadorBola,(desvio + 10,10))
	tela.blit(pontosJogadorXis,(desvio + 440,10))
	pygame.draw.line(tela,(0,0,0),(desvio + 200, desvio_y + 50),(desvio + 200,desvio_y + 420),5)
	pygame.draw.line(tela,(0,0,0),(desvio + 400,desvio_y + 50),(desvio + 400,desvio_y + 420),5)
	pygame.draw.line(tela,(0,0,0),(desvio + 80,desvio_y + 150),(desvio + 530,desvio_y + 150),5)
	pygame.draw.line(tela,(0,0,0),(desvio + 80,desvio_y + 300),(desvio + 530,desvio_y + 300),5)
	
	
	
	for i in range(len(jogo_all.casas)):
		if jogo_all.casas[i] == 0:
			tela.blit(bola,(posicoes[i]))
					
		elif jogo_all.casas[i] == 1:
			tela.blit(xis,(posicoes[i]))

	if frame%60 == 0:
		pygame.display.flip()    

	return jogo_all,terminou,comecou,saiu_do_jogo