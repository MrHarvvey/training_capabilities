import random
import itertools
enemy_list = [[9,2]]
WIDTH = 900
enemy_size = 40

def drop_enemies(enemy_list):
    for _ in itertools.repeat(None, 10):
        x_pos = random.randint(30, 800)
        y_pos = 30
        enemy_list.append([x_pos, y_pos])

print(drop_enemies(enemy_list))
print(enemy_list)