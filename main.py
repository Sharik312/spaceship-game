import pygame, os
pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (30, 255, 65)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

SC_WIDTH, SC_LENGTH = 900, 500
WIN = pygame.display.set_mode((SC_WIDTH, SC_LENGTH))
pygame.display.set_caption("Spaceship Game!")

BORDER = pygame.Rect(SC_WIDTH/2 - 5, 0, 10, SC_LENGTH)

FPS = 60
SHIP_WIDTH, SHIP_LENGTH = 55, 40
VEL = 5


YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", 'spaceship_red.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SHIP_WIDTH, SHIP_LENGTH)), 90)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SHIP_WIDTH, SHIP_LENGTH)), 270)

 



def draw_window(red, yellow):
    WIN.fill(GREEN)
    pygame.draw.rect(WIN, BLACK, BORDER)

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    pygame.display.update()
            

def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + red.width + VEL < SC_WIDTH:
        red.x += VEL
    if keys_pressed[pygame.K_DOWN] and red.y - VEL + red.height < SC_LENGTH-25:
        red.y += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL


def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + yellow.width + VEL < BORDER.x:
        yellow.x += VEL
    if keys_pressed[pygame.K_s] and yellow.y - VEL + yellow.height < SC_LENGTH-25:
        yellow.y += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL


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
        
        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red )
        
        draw_window(red, yellow)
        
    
    pygame.quit()

if __name__ == "__main__":
    main()
