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

class Poker:
	def __init__(self):
		self.PCards = []
	def Cards(self):
		def Shuffel(self):
			self.PCards = []
			for _ in range (1,6):
				self.PCards.append(random.randint(1,14))
		def Blit(self):
			for runs in range(0,5):
				pygame.draw.rect(screen, (255,255,255), (runs*100, 100, 50, 50))


Game = Poker()
#STARTING LOOP
while True:
	#DISPLAYING EVERTHING
	pygame.draw.rect(screen, (0,0,0), (0,0,WIDTH,HEIGHT))
	Game.Cards.Blit()
	#FLIPING
	pygame.display.flip()

	#Keyboard event checker
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()


