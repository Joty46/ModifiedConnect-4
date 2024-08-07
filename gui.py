import pygame
import button
import subprocess
from subprocess import call
#import connect

#create display window
# SCREEN_HEIGHT = 500
# SCREEN_WIDTH = 800



screen = pygame.display.set_mode((800, 450))
boardImg = pygame.image.load('main_page.png')
screen.blit(boardImg, (0, 0))

# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

#load button images
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()

#create button instances
start_button = button.Button(100, 250, start_img, 0.45)
exit_button = button.Button(100, 350, exit_img, 0.5)





#game loop
run = True
while run:

	

	if start_button.draw(screen):
		print('START')
		call(["python", "connect.py"])

		
		
		
		# action = connect
        
	if exit_button.draw(screen):
		print('EXIT')
		pygame.quit()

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False
		

	pygame.display.update()

pygame.quit()