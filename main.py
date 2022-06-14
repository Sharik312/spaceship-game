import pygame, os
pygame.font.init()
pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (30, 255, 65)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

SC_WIDTH, SC_LENGTH = 1800, 1100
WIN = pygame.display.set_mode((SC_WIDTH, SC_LENGTH))
pygame.display.set_caption("Spaceship Game!")

BORDER = pygame.Rect(SC_WIDTH//2 - 5, 0, 10, SC_LENGTH)

HEALTH_FONT = pygame.font.SysFont('comicsans', 80)
WINNER_FONT = pygame.font.SysFont('comicsans', 200)

FPS = 60
SHIP_WIDTH, SHIP_LENGTH = 110, 80
VEL = 8
BULLET_VEL = 18
MAX_BULLETS = 3

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", 'spaceship_red.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SHIP_WIDTH, SHIP_LENGTH)), 90)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SHIP_WIDTH, SHIP_LENGTH)), 270)


SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (SC_WIDTH, SC_LENGTH))



def draw_window(red, yellow, red_bullets, yellow_bullets, red_hp, yellow_hp):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_hp_text = HEALTH_FONT.render("Health: " + str(red_hp), 1, WHITE)
    yellow_hp_text = HEALTH_FONT.render("Health: " + str(yellow_hp), 1, WHITE)
    WIN.blit(red_hp_text, (SC_WIDTH-red_hp_text.get_width() - 10, 10))
    WIN.blit(yellow_hp_text, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

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


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > SC_WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (SC_WIDTH/2 - draw_text.get_width() /
                         2, SC_LENGTH/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    red = pygame.Rect(SC_WIDTH-100, SC_LENGTH/2, SHIP_WIDTH, SHIP_LENGTH)
    yellow  = pygame.Rect(100,  SC_LENGTH/2, SHIP_WIDTH, SHIP_LENGTH)

    red_bullets = []
    yellow_bullets = []
    red_hp = 8
    yellow_hp = 8
    winner_text = ""
    score = 0

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 + 4, 20, 10)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 + 4, 20, 10)
                    red_bullets.append(bullet)

            if event.type == RED_HIT:
                red_hp -= 1

            if event.type == YELLOW_HIT:
                yellow_hp -= 1

        if red_hp <= 0:
            winner_text = "Yellow Wins!"
            score += 1
        if yellow_hp <= 0:
            winner_text = "Red Wins!"
            score -= 1
        if winner_text != "":
            draw_winner(winner_text)
            break

        
        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets, red_hp, yellow_hp)
        
    
    main()

if __name__ == "__main__":
    main()



if score > 0:
    print(f"Yello Wins by {score}!")
if score < 0:
    print(f"Yello Wins by {score}!")
else:
    print("Tie!")