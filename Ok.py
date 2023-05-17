import pygame
import time
import random
from CONSTANTS import *
from functions import *

pygame.init()

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Люти пон')
font_style = pygame.font.SysFont(None, 50)
game_close = False
game_over = False

sleeping_time = 0.09
stop = False
snake_List = []
x1 = 300
y1 = 200
n = 1
x1_change = 0
y1_change = 0
clock = pygame.time.Clock()
new_food = True
new_food1 = True
new_food2 = True
last = None
while not game_over:
    if new_food:
        foodx, foody = create_new_food(snake_List)
        new_food = False
    if new_food1:
        foodx1, foody1 = create_new_food(snake_List)
        new_food1 = False
    if new_food2:
        foodx2, foody2 = create_new_food(snake_List)
        new_food2 = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            message(font_style, dis, 'ХНЫК', 355, 270, red)
            pygame.display.update()
            time.sleep(1)
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if last == pygame.K_RIGHT:
                    continue
                last = pygame.K_LEFT
                x1_change = -snake_block
                y1_change = 0
                stop = False
            elif event.key == pygame.K_RIGHT:
                if last == pygame.K_LEFT:
                    continue
                last = pygame.K_RIGHT
                x1_change = snake_block
                y1_change = 0
                stop = False
            elif event.key == pygame.K_UP:
                if last == pygame.K_DOWN:
                    continue
                last = pygame.K_UP
                y1_change = -snake_block
                x1_change = 0
                stop = False
            elif event.key == pygame.K_DOWN:
                if last == pygame.K_UP:
                    continue
                last = pygame.K_DOWN
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
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block], border_radius=5)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, blue, [foodx1, foody1, snake_block, snake_block])
        pygame.draw.rect(dis, blue, [foodx2, foody2, snake_block, snake_block])
        if x1 == foodx and y1 == foody:
            new_food = True
            n += 1
            sleeping_time += 0.003
        if x1 == foodx1 and y1 == foody1:
            new_food1 = True
            n += 1
            sleeping_time += 0.003
        if x1 == foodx2 and y1 == foody2:
            new_food2 = True
            n += 1
            sleeping_time += 0.003
    else:
        if x1 == -snake_block:
            x1 = dis_width - snake_block
            x1_change = -snake_block
        if x1 == dis_width:
            x1 = 0
            x1_change = snake_block
        if y1 == -snake_block:
            y1 = dis_height - snake_block
            y1_change = -snake_block
        if y1 == dis_height:
            y1 = 0
            y1_change = snake_block
    message(font_style, dis, f'Количество очков - {n}', col=green)
    snake_List.append((x1, y1))
    if len(snake_List) > n:
        del snake_List[0]
    for x in snake_List[:-1]:
        if x == (x1, y1):
            msg_gameover(font_style, dis)
            game_over = True
    draw_snake(snake_List, dis)
    pygame.display.update()
    clock.tick(30)
    time.sleep(sleeping_time)

pygame.quit()
quit()
