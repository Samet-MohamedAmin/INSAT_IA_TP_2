#! /bin/python3

import pygame
from pieces import chess

import time

display = pygame.display.set_mode((600, 600))

        
def main(final_result):
    gridSize = 64

    board = chess.Board(gridSize)

    board.draw()
    pygame.Surface.blit(display, board.image, (0, 0))
    pygame.display.update()

    i = 1
    while True:
        time.sleep(0.4)
        if i < len(final_result):
                board.result = final_result[i]
                print(final_result[i])
                if(len(final_result[i]) >= len(final_result[i + 1])):
                        print('*-'*10+'[ROLLBACK]'+'-*'*10)
                        time.sleep(0.8)
                i += 1

        board.update()

        pygame.Surface.fill(display, (128, 128, 128))

        board.draw()

        # pygame.draw.rect(display, (128, 128, 128), [209, 109, 582, 582], 0)
        pygame.Surface.blit(display, board.image, (45, 45))

        pygame.display.update()


if __name__ == "__main__":
    main([])