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

#Drawing the background for the board
def draw_board():
    pygame.draw.rect(screen,(200, 200, 200) [0 ,0, 400, 400], 0, 10)
    pass

#Drawing the numbers(objects)
def draw_pieces():
    pass

#Adding new numbers randomly
def spawn_pieces():
    pass

#Main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill("gray")
    
    draw_board()
    draw_pieces()
    spawn_pieces()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()
pygame.quit()