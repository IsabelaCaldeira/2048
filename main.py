import pygame 
import random
pygame.init()

#Initial set up
WIDTH = 400
HEIGHT = 500
screen = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption('2048')

font = pygame.font.Font('freesanbold.ttf', 24)

timer = pygame.time.Clock()
fps = 60
