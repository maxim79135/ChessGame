import pygame
import os
# from piece import Bishop
from board import Board

board = pygame.transform.scale(pygame.image.load(os.path.join("img", "board_alt.png")), (750, 750))
rect = (113, 113, 525, 525)


def redraw_gameWindow():
    global win
    win.blit(board, (0, 0))
    bo.draw(win, bo.board)
    pygame.display.update()


def click(pos):
    """
    :return: pos (x, y) in range 0-7 0-7
    """
    x = pos[0]
    y = pos[1]
    if rect[0] < x < rect[0] + rect[2]:
        if rect[1] < y < rect[1] + rect[3]:
            divX = x - rect[0]
            divY = y - rect[1]
            i = int(divX / (rect[2] / 8))
            j = int(divY / (rect[3] / 8))
            return i, j
    return None, None


def main():
    global bo
    bo = Board(8, 8)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(10)
        redraw_gameWindow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                i, j = click(pos)
                if i is not None and j is not None:
                    bo.select(i, j)


width = 750
height = 750
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess Game")
main()
