import time
from pieces import queen
import colors

import pygame



def mouseOver(rect):
    m = pygame.mouse.get_pos()
    if rect[0] < m[0] < rect[0] + rect[2]:
        if rect[1] < m[1] < rect[1] + rect[3]:
            return True
    return False



class Board:

    class Space:
        def __init__(self, color):
            self.color = color
            self.contents = None

    def __init__(self, gridSize):
        self.result = []
        self.pieces = []
        self.gridSize = gridSize
        self.image = pygame.image.load('pieces/img/board.png')
        self.SELECT_FLAG = False

    def getMouse(self):
        m = pygame.mouse.get_pos()
        x = int((m[0] - 45) / self.gridSize)
        y = int((m[1] - 45) / self.gridSize)

        return [x, y]

    def update(self):
        self.pieces = [queen.Queen([i-1, index], colors.COLORS[index]) for index, i in enumerate(self.result[:8])]
        for event in pygame.event.get():
            # Exit when exit button is pushed
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            return

    def draw(self):
        #squareWidth = 4
        squareWidth = 0

        # Reset the board image
        self.image = pygame.image.load('pieces/img/board.png')
        # -------------------------
        # Draw red squares around all the spaces onto the board image
        for piece in self.pieces:
            piece.findSpaces(self.pieces)
            if True:  # piece.active:
                for square in piece.moveSquares:
                    rect = [square[0] * self.gridSize,
                            square[1] * self.gridSize,
                            self.gridSize,
                            self.gridSize]

                    # Draw the square
                    pygame.draw.rect(self.image, piece.color,
                                     rect, squareWidth)
                
                # Draw the current position
                rect = [piece.location[0] * self.gridSize,
                        piece.location[1] * self.gridSize,
                            self.gridSize,
                            self.gridSize]

                pygame.draw.rect(self.image, piece.color,
                                     rect, squareWidth)

        # -------------------------
        # Draw the pieces
        for piece in self.pieces:

            # If the piece hasn't been captured
            if not piece.captured:
                # Find it's location and draw it's image
                loc = [piece.location[0] * self.gridSize,
                       piece.location[1] * self.gridSize]
                pygame.Surface.blit(self.image, piece.image, loc)


display = pygame.display.set_mode((600, 600))


if __name__ == '__main__':
    display = pygame.display.set_mode((600, 600))
