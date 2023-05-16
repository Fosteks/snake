import pygame
import time
import random
from CONSTANTS import *
from functions import *

pygame.init()

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Люти пон')
font_style = pygame.font.SysFont(None, 50)

game_over = False
stop = False
snake_List = []

x1 = 350
y1 = 250
n = 1
x1_change = 0
y1_change = 0
clock = pygame.time.Clock()

foodx = random.randint(0, dis_width - snake_block)
foody = random.randint(0, dis_height - snake_block)
new_food = True

while not game_over:
    if new_food:
        foodx = random.randint(0, (dis_width - snake_block) // snake_block) * snake_block
        foody = random.randint(0, (dis_height - snake_block) // snake_block) * snake_block
        new_food = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            message(font_style, dis, 'ХНЫК', 355, 270, red)
            pygame.display.update()
            time.sleep(1)
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
                stop = False
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
                stop = False
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
                stop = False
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
                stop = False
            elif event.key == pygame.K_SPACE:
                stop = True
    if not stop:
        x1 += x1_change
        y1 += y1_change
    if check_pos(x1, y1):
        dis.fill(white)
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        if x1 == foodx and y1 == foody:
            new_food = True
            n += 1
    else:
        msg_gameover(font_style, dis)
        game_over = True
    message(font_style, dis, f'Количество очков - {n}', col=green)
    snake_List.append((x1, y1))
    if len(snake_List) > n:
        del snake_List[0]
    for x in snake_List[:-1]:
        if x == (x1, y1):
            game_close = True
    our_snake(snake_List, dis)
    pygame.display.update()
    clock.tick(30)
    time.sleep(0.1)

pygame.quit()
quit()