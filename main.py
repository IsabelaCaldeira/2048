import pygame 
import random
pygame.init()

#Initial set up
WIDTH = 400
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')

font = pygame.font.Font('freesansbold.ttf', 24)

timer = pygame.time.Clock()
fps = 60

#Main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill("gray")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()
pygame.quit()