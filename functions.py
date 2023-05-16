import pygame
import time
from CONSTANTS import *


def message(font_style, dis, msg, x=0, y=0, col=black):
    mesg = font_style.render(msg, True, col)
    dis.blit(mesg, [x, y])


def msg_gameover(font_style, dis):
    message(font_style, dis, 'GAME OVER', 330, 270)
    pygame.display.update()
    time.sleep(2)


def check_pos(x, y):
    if x == -10 or y == -10 or x == dis_width or y == dis_height:
        return False
    else:
        return True


def our_snake(snake_list, dis):
    pygame.draw.rect(dis, black, [snake_list[0][0], snake_list[0][1], snake_block, snake_block])
    for x in snake_list[:-1]:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
