from pygame.locals import *
import pygame
    
windowWidth = 800
windowHeight = 600


pygame.init()
surface = pygame.display.set_mode((windowWidth, windowHeight), pygame.HWSURFACE)
surface.fill((0,0,0))
snake_image = pygame.image.load("snake.png").convert()
rabbit_image = pygame.image.load("rabbit.png").convert()

surface.blit(snake_image,(100,100)) 
surface.blit(rabbit_image,(200,200))
pygame.display.flip()

while( True ):
	pygame.event.pump()
	keys = pygame.key.get_pressed() 

	# if (keys[K_RIGHT]):
	# 	moveRight()

	# if (keys[K_LEFT]):
	# 	moveLeft()

	# if (keys[K_UP]):
	# 	moveUp()

	# if (keys[K_DOWN]):
	# 	moveDown()

	if (keys[K_ESCAPE]):
		break

