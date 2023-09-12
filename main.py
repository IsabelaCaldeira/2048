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

colors = {0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
          'light text': (249, 246, 242),
          'dark text': (119, 118, 101),
          'other': (0, 0, 0),
          'bg': (187, 173, 160)}
          

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