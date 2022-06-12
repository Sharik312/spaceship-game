import pygame, os
pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (30, 255, 65)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

FPS = 60
SHIP_WIDTH, SHIP_LENGTH = 55, 40


YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", 'spaceship_red.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SHIP_WIDTH, SHIP_LENGTH)), 90)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SHIP_WIDTH, SHIP_LENGTH)), 270)

 
SC_WIDTH, SC_LENGTH = 900, 500
WIN = pygame.display.set_mode((SC_WIDTH, SC_LENGTH))
pygame.display.set_caption("Spaceship Game!")


def draw_window(red, yellow):
    WIN.fill(GREEN)

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    pygame.display.update()
            


def main():
    red = pygame.Rect(SC_WIDTH-100, SC_LENGTH/2, SHIP_WIDTH, SHIP_LENGTH)
    yellow  = pygame.Rect(100,  SC_LENGTH/2, SHIP_WIDTH, SHIP_LENGTH)

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_window(red, yellow)
    
    pygame.quit()

if __name__ == "__main__":
    main()
