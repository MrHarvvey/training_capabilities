import pygame
import sys
import random
import math
pygame.init()

WIDTH = 800
HEIGHT = 600

kolor_zawodnika = (255, 0, 5)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
myFont =pygame.font.SysFont("jakakolwiek", 34, bold=True)
enemy_size = 20
clock = pygame.time.Clock()
player_xy = [400, 540]
player_size = 30
game_over = False
background_color = (31, 71, 232)
blue = (122, 255, 122)
enemy_size = 30
enemy_xy = [random.randint(30, (WIDTH - enemy_size)), enemy_size]
yelow = (229, 255 ,55)
enemy_list = [enemy_xy]
speed = 5
score = 0
level = 1

def set_level(score, speed):
    if score < 20 :
        speed = 15
    elif score < 40:
        speed = 20
    elif score < 60:
        speed = 30
    return speed
def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) <= 10 and delay < 0.3:
        x_pos = random.randint(30, WIDTH - enemy_size)
        y_pos = 30
        enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
    for enemy_xy in enemy_list:
        pygame.draw.circle(screen, blue, (enemy_xy[0], enemy_xy[1]), enemy_size)

def update_enemy_pos(enemy_list, score):
    for idx, enemy_xy in enumerate(enemy_list):
        if enemy_xy[1] >= 0 and enemy_xy[1] <= (HEIGHT + 50):
            enemy_xy[1] += speed
        else:
            enemy_list.pop(idx)
            score += 1
    return score

def def_collision(player_xy, enemy_xy):
    p_x = player_xy[0]
    p_y = player_xy[1]
    e_x = enemy_xy[0]
    e_y = enemy_xy[1]
    if (enemy_size + player_size) >= math.sqrt((e_x - p_x)**2 + (e_y - p_y)**2):
        return False

def collision_detect(enemy_list, player_pos):
    for position in enemy_list:
        if def_collision(player_pos, position) == False:
            return True


while not game_over:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_xy[0] -= player_size
            elif event.key == pygame.K_RIGHT:
                player_xy[0] += player_size
    if def_collision(player_xy, enemy_xy) == False:
        game_over = True
    speed = set_level(score, speed)
    if score < 20 :
        level = 1
    elif score < 40:
        level = 2
    elif score < 60:
        level = 3
    screen.fill(background_color)
    drop_enemies(enemy_list)
    draw_enemies(enemy_list)
    score = update_enemy_pos(enemy_list, score)

    if collision_detect(enemy_list, player_xy) == True:
        game_over = True

    text = "Wynik: " + str(score)
    text2 = "Level: " + str(level)
    label2 = myFont.render(text2, 1 , yelow)
    label = myFont.render(text, 1 , yelow)
    screen.blit(label, (WIDTH - 200, HEIGHT - 40))
    screen.blit(label2, (WIDTH - 200, HEIGHT - 100))
    pygame.draw.circle(screen, blue, (enemy_xy[0], enemy_xy[1]), enemy_size)
    pygame.draw.circle(screen, kolor_zawodnika, (player_xy[0], player_xy[1]), player_size)

    pygame.display.update()
