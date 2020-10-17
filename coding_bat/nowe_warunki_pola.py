import pygame
import sys
import random
import math
pygame.init()

WIDTH = 800
HEIGHT = 600

kolor_zawodnika = (255, 0, 5)


screen = pygame.display.set_mode((WIDTH, HEIGHT))

enemy_size = 20
clock = pygame.time.Clock()
player_xy = [400, 540]
player_size = 30
game_over = False
background_color = (0, 0, 0)
blue = (122, 255, 2)
enemy_size = 30
enemy_xy = [random.randint(30, (WIDTH - enemy_size)), enemy_size]

enemy_list = [enemy_xy]
speed = 10

def drop_enemies(enemy_list):
    if len(enemy_list) < 10:
        x_pos = random.randint(30, WIDTH - enemy_size)
        y_pos = 30
        enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
    for enemy_xy in enemy_list:
        pygame.draw.circle(screen, blue, (enemy_xy[0], enemy_xy[1]), enemy_size)

def update_enemy_pos(enemy_list):
    for idx, enemy in enumerate(enemy_list):
        if enemy_xy[1] >= 0 and enemy_xy[1] < HEIGHT:
            enemy_xy[1] += speed
        else:
            enemy_list.pop(idx)

def def_collision(player_xy, enemy_xy):
    p_x = player_xy[0]
    p_y = player_xy[1]
    e_x = enemy_xy[0]
    e_y = enemy_xy[1]
    if (enemy_size + player_size) >= math.sqrt((e_x - p_x)**2 + (e_y - p_y)**2):
        return False

while not game_over:
    clock.tick(20)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_xy[0] -= player_size
            elif event.key == pygame.K_RIGHT:
                player_xy[0] += player_size
    if def_collision(player_xy, enemy_xy) == False:
        game_over = True
    screen.fill(background_color)
    drop_enemies(enemy_list)
    update_enemy_pos(enemy_list)
    draw_enemies(enemy_list)

    pygame.draw.circle(screen, blue, (enemy_xy[0], enemy_xy[1]), enemy_size)
    pygame.draw.circle(screen, kolor_zawodnika, (player_xy[0], player_xy[1]), player_size)

    pygame.display.update()
