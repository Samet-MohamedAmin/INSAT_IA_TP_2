#! /bin/python3

import pygame
from pieces import chess

import time


        
def main(final_result):
    gridSize = 64

    board = chess.Board(gridSize)

    display = pygame.display.set_mode((600, 600))

    board.draw()
    pygame.Surface.blit(display, board.image, (0, 0))
    pygame.display.update()

    i = 1
    while True:
        n = 0.2
        time.sleep(n)
        if i < len(final_result) - 1:
                board.result = final_result[i]
                print(final_result[i])
                if(len(final_result[i]) >= len(final_result[i + 1])):
                        print('*-'*10+'[ROLLBACK]'+'-*'*10)
                        time.sleep(n)
                i += 1

        board.update()

        pygame.Surface.fill(display, (128, 128, 128))

        board.draw()

        # pygame.draw.rect(display, (128, 128, 128), [209, 109, 582, 582], 0)
        pygame.Surface.blit(display, board.image, (45, 45))

        pygame.display.update()


if __name__ == "__main__":
    main([])