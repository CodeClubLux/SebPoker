#!/usr/bin/env python3
import pygame, random, sys, os, platform, pickle, time, os.path, shutil, re
from pygame.locals import *
pygame.init()
# MODULES

#DEFINING SCREEN
zoom = 1.3
Info = pygame.display.Info()
WIDTH = int(Info.current_w / zoom)
HEIGHT = int(Info.current_h / zoom)
screen = pygame.display.set_mode((WIDTH,HEIGHT))

def ScreenText(screen,text="TEXT GOES HERE",var="var",X=0,Y=0,color=(0,0,0),size=25,Letter = "monospace"):
    myfont = pygame.font.SysFont(Letter, size, True)
    var = myfont.render(text, 25, color)
    screen.blit(var, (X, Y))



class Poker:
	def __init__(self):
		self.PCards = []
		self.SCards = []
	def Change(self,C1=False,C2=False,C3=False,C4=False,C5=False):
		self.SCards = []
		if C1 == True:
			self.SCards.append(random.randint(1,14))
		else:
			self.SCards.append(self.PCards[0])
		if C2 == True:
			self.SCards.append(random.randint(1,14))
		else:
			self.SCards.append(self.PCards[1])
		if C3 == True:
			self.SCards.append(random.randint(1,14))
		else:
			self.SCards.append(self.PCards[2])
		if C4 == True:
			self.SCards.append(random.randint(1,14))
		else:
			self.SCards.append(self.PCards[3])
		if C5 == True:
			self.SCards.append(random.randint(1,14))
		else:
			self.SCards.append(self.PCards[4])
		self.PCards = self.SCards

	def Shuffle(self):
		self.PCards = []
		for _ in range (1,6):
			self.PCards.append(random.randint(1,14))
	def Blit(self):
		for runs in range(0,5):
			if Face != 2:
				pygame.draw.rect(screen, (200,200,200), (runs*200+50, HEIGHT-250, 140, 300))
			if Face == 2 or Face == 4:
				if Ch1 == True:
					if runs == 0:
						pygame.draw.rect(screen, (255,40,40), (runs*200+50, HEIGHT-250, 140, 300))
				if Ch1 == False:
					if runs == 0:
						pygame.draw.rect(screen, (200,200,200), (runs*200+50, HEIGHT-250, 140, 300))
				if Ch2 == True:
					if runs == 1:
						pygame.draw.rect(screen, (255,40,40), (runs*200+50, HEIGHT-250, 140, 300))
				if Ch2 == False:
					if runs == 1:
						pygame.draw.rect(screen, (200,200,200), (runs*200+50, HEIGHT-250, 140, 300))
				if Ch3 == True:
					if runs == 2:
						pygame.draw.rect(screen, (255,40,40), (runs*200+50, HEIGHT-250, 140, 300))
				if Ch3 == False:
					if runs == 2:
						pygame.draw.rect(screen, (200,200,200), (runs*200+50, HEIGHT-250, 140, 300))
				if Ch4 == True:
					if runs == 3:
						pygame.draw.rect(screen, (255,40,40), (runs*200+50, HEIGHT-250, 140, 300))
				if Ch4 == False:
					if runs == 3:
						pygame.draw.rect(screen, (200,200,200), (runs*200+50, HEIGHT-250, 140, 300))
				if Ch5 == True:
					if runs == 4:
						pygame.draw.rect(screen, (255,40,40), (runs*200+50, HEIGHT-250, 140, 300))
				if Ch5 == False:
					if runs == 4:
						pygame.draw.rect(screen, (200,200,200), (runs*200+50, HEIGHT-250, 140, 300))

			if self.PCards[runs] == 11:
				ScreenText(screen, "J", "J", runs*200+65, HEIGHT-175, (0,0,0), 100)
			if self.PCards[runs] == 12:
				ScreenText(screen, "Q", "Q", runs*200+65, HEIGHT-175, (0,0,0), 100)
			if self.PCards[runs] == 13:
				ScreenText(screen, "K", "K", runs*200+65, HEIGHT-175, (0,0,0), 100)
			if self.PCards[runs] == 14:
				ScreenText(screen, "A", "A", runs*200+65, HEIGHT-175, (0,0,0), 100)
			else:
				if not self.PCards[runs] == 11:
					if not self.PCards[runs] == 12:
						if not self.PCards[runs] == 13:
							if not self.PCards[runs] == 14:
								ScreenText(screen, str(self.PCards[runs]), str(self.PCards[runs]), runs*200+65, HEIGHT-175, (0,0,0), 100)



Game = Poker()
Coins = 99

DMon = 0

#MAKING CARDS
Game.Shuffle()

#defining other variables
Face = 1
#STARTING LOOP
Ch1 = False
Ch2 = False
Ch3 = False
Ch4 = False
Ch5 = False
while True:
	#DISPLAYING EVERTHING

	#Background
	pygame.draw.rect(screen, (255,255,255), (0,0,WIDTH,HEIGHT))

	#Bliting the cards
	Game.Blit()

	#Images and Objects

	#Face 1
	if Face == 1:
		pygame.draw.rect(screen, (200,200,200), (WIDTH-110, 50, 100, 60))
		pygame.draw.rect(screen, (200,200,200), (WIDTH-110, 120, 100, 60))
		pygame.draw.rect(screen, (200,200,200), (WIDTH-110, 200, 100, 60))

	if Face == 2:
		pygame.draw.rect(screen, (200,200,200), (WIDTH-110, 50, 100, 60))

	if Face == 3:
		pygame.draw.rect(screen, (200,200,200), (WIDTH-110, 50, 100, 60))
		pygame.draw.rect(screen, (200,200,200), (WIDTH-110, 120, 100, 60))
		pygame.draw.rect(screen, (200,200,200), (WIDTH-110, 200, 100, 60))
	if Face == 4:
		pygame.draw.rect(screen, (200,200,200), (WIDTH-110, 50, 100, 60))


	#Text
	#Face 1
	if Face == 1:
		ScreenText(screen,"How much do you bet?","betq",50,30,(0,0,0),40)

		ScreenText(screen,"More","More",WIDTH-110,60,(255,0,0),40)
		ScreenText(screen,"Less","Less",WIDTH-110,130,(255,0,0),40)
		ScreenText(screen,"Bet","Accept Bet",WIDTH-110,200,(255,0,0),50)
		ScreenText(screen,"You will bet: " + str(DMon),"Bet",WIDTH-370,270,(255,0,0),40)
	if Face == 2:
		ScreenText(screen,"Which cards do you want to replace?","betq",50,30,(0,0,0),40)
		ScreenText(screen,"Replace","Replace",WIDTH-110,65,(255,0,0),20)
	if Face == 3:
		ScreenText(screen,"How much do you bet?","betq",50,30,(0,0,0),40)
		ScreenText(screen,"More","More",WIDTH-110,60,(255,0,0),40)
		ScreenText(screen,"Less","Less",WIDTH-110,130,(255,0,0),40)
		ScreenText(screen,"Bet","Accept Bet",WIDTH-110,200,(255,0,0),50)
		ScreenText(screen,"You will bet: " + str(DMon),"Bet",WIDTH-370,270,(255,0,0),40)
	if Face == 4:
		ScreenText(screen,"Which cards do you use?","betq",50,30,(0,0,0),40)
		ScreenText(screen,"Use","Use",WIDTH-110,65,(255,0,0),20)
		#Identify cards

	#Coins
	ScreenText(screen,"Coins: "+str(Coins),"Money",WIDTH-250,0,(255,0,0),40)

	#Mouse action



	#FLIPING
	pygame.display.flip()

	#Keyboard Mouse event checker
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			MouseX = pygame.mouse.get_pos()[0]
			MouseY = pygame.mouse.get_pos()[1]
			#print(HEIGHT)
			#print(str(MouseY) + "and" + str(MouseX))
			if Face == 1 or Face == 3:
				#Face 1 More button
				if MouseX > WIDTH-110 and MouseY > 50 and MouseX < WIDTH-10 and MouseY < 110:
					if DMon < Coins:
						DMon = DMon + 1
				#Face 1 Less button
				if MouseX > WIDTH-110 and MouseY > 120 and MouseX < WIDTH-10 and MouseY < 180:
					if DMon > 0:
						DMon = DMon - 1
				#Face 1 Bet button
				if MouseX > WIDTH-110 and MouseY > 200 and MouseX < WIDTH-10 and MouseY < 260:
					if Face == 1:
						Face = 2
					if Face == 3:
						Face = 4
					Coins = Coins - DMon
			if Face == 2 or Face == 4:
				if MouseX > 50 and MouseY > 340 and MouseX < 190 and MouseY < HEIGHT:
					if Ch1 == False:
						Ch1 = True
					else:
						Ch1 = False
				if MouseX > 250 and MouseY > 340 and MouseX < 390 and MouseY < HEIGHT:
					if Ch2 == False:
						Ch2 = True
					else:
						Ch2 = False
				if MouseX > 450 and MouseY > 340 and MouseX < 590 and MouseY < HEIGHT:
					if Ch3 == False:
						Ch3 = True
					else:
						Ch3 = False
				if MouseX > 650 and MouseY > 340 and MouseX < 790 and MouseY < HEIGHT:
					if Ch4 == False:
						Ch4 = True
					else:
						Ch4 = False
				if MouseX > 850 and MouseY > 340 and MouseX < 990 and MouseY < HEIGHT:
					if Ch5 == False:
						Ch5 = True
					else:
						Ch5 = False
				if MouseX > WIDTH-110 and MouseY > 50 and MouseX < WIDTH-10 and MouseY < 110:
					Game.Change(Ch1,Ch2,Ch3,Ch4,Ch5)
					Game.Blit()
					time.sleep(1)
					Face = 3
					Ch1 = False
					Ch2 = False
					Ch3 = False
					Ch4 = False
					Ch5 = False
			if Face == 4:
				if MouseX > WIDTH-110 and MouseY > 50 and MouseX < WIDTH-10 and MouseY < 110:
					Face = 5