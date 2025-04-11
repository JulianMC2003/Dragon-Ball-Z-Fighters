import pygame
from fighter import Fighter

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dragon Ball Fighter")

clock = pygame.time.Clock()
FPS = 60

RED = (255, 0, 0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

intro_count = 0
last_count_update = pygame.time.get_ticks()
score = [0, 0]
round_over = False
ROUND_OVER_COOLDOWN = 2000

GOKU_SIZE = 93
GOKU_SCALE = 4
GOKU_OFFSET = [40, 20]
GOKU_DATA = [GOKU_SIZE, GOKU_SCALE, GOKU_OFFSET]
VEGETA_SIZE = 92
VEGETA_SCALE = 4
VEGETA_OFFSET = [27, 20]
VEGETA_DATA =[VEGETA_SIZE, VEGETA_SCALE, VEGETA_OFFSET]
background = pygame.image.load("/Users/Code/HACK110/Dragon_Ball/assets/images/background/background.jpg").convert_alpha()

goku_sheet = pygame.image.load("/Users/Code/HACK110/Dragon_Ball/assets/images/sprites/goku.png").convert_alpha()
vegeta_sheet = pygame.image.load("/Users/Code/HACK110/Dragon_Ball/assets/images/sprites/vegeta.png").convert_alpha()

victory_img = pygame.image.load("/Users/Code/HACK110/Dragon_Ball/assets/images/icons/victory.jpeg").convert_alpha()

GOKU_ANIMATION_STEPS = [4, 2, 4, 10, 3, 1, 2, ]
VEGETA_ANIMATION_STEPS = [8, 2, 4, 10, 4, 1, 1]


def draw_background():
    scaled_bg = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

def draw_health(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 5, y - 5, 410, 40 ))
    pygame.draw.rect(screen, RED, (x, y, 400, 30 ))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

fighter_1 = Fighter(1, 200, 310, False, GOKU_DATA, goku_sheet, GOKU_ANIMATION_STEPS)
fighter_2 = Fighter(2, 700, 310, True, VEGETA_DATA, vegeta_sheet, VEGETA_ANIMATION_STEPS)

run = True
while run:
    
    clock.tick(FPS)
    draw_background()

    draw_health(fighter_1.health, 20, 20)
    draw_health(fighter_2.health, 580, 20)

    if intro_count <= 0:
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, False)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, False)
    if (pygame.time.get_ticks() - last_count_update) >= 1000:
        intro_count -= 1
        last_count_update = pygame.time.get_ticks()

    fighter_1.update()
    fighter_2.update()

    fighter_1.draw(screen)
    fighter_2.draw(screen)

    if round_over == False:
        if fighter_1.alive == False:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif fighter_2.alive == False:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
    else:
        screen.blit(victory_img, (360, 150))
        if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
            round_over = False
            intro_count = 3
            fighter_1 = Fighter(1, 200, 310, False, GOKU_DATA, goku_sheet, GOKU_ANIMATION_STEPS)
            fighter_2 = Fighter(2, 700, 310, True, VEGETA_DATA, vegeta_sheet, VEGETA_ANIMATION_STEPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
