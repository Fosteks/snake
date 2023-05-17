from random import randint
import pygame
from CONSTANTS import *


def message(font_style, dis, msg, x=0, y=0, col=black):
    mesg = font_style.render(msg, True, col)
    dis.blit(mesg, [x, y])


def msg_gameover(font_style, dis):
    message(font_style, dis, 'GAME OVER', 330, 270)
    pygame.display.update()
    time.sleep(2)


def check_pos(x, y):
    if x == -snake_block or y == -snake_block or x == dis_width or y == dis_height:
        return False
    else:
        return True


def draw_snake(snake_list, dis):
    pygame.draw.rect(dis, black, [snake_list[0][0], snake_list[0][1], snake_block, snake_block], border_radius=5)
    for x in snake_list[:-1]:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block], border_radius=5)


def create_new_food(snake_list):
    while True:
        foodx = randint(0, (dis_width - snake_block) // snake_block) * snake_block
        foody = randint(0, (dis_height - snake_block) // snake_block) * snake_block
        if not (foodx, foody) in snake_list:
            return foodx, foody
