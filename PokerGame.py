import pygame, random, sys, os, platform, pickle, time, os.path, shutil, re
from pygame.locals import *
# MODULES

#DEFINING SCREEN
zoom = 1.3
Info = pygame.display.Info()
WIDTH = int(Info.current_w / zoom)
WIDTH = int(Info.current_h / zoom)
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#STARTING LOOP
while True:
	#DISPLAYING EVERTHING
	pygame.draw.rect(screen, (255,255,255), (0,0,WIDTH,HEIGHT))
	#FLIPING
	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

