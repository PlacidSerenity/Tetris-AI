from typing import Iterator
import pygame
import random

class BoardTiles:
    EMPTY = 0
    O = 1
    I = 2
    S = 3
    Z = 4
    L = 5
    J = 6
    T = 7

BoardColours = {
    BoardTiles.EMPTY: (0, 0, 0),
    BoardTiles.O: (227, 159, 2),
    BoardTiles.I: (15, 155, 215),
    BoardTiles.S: (89, 177, 1),
    BoardTiles.Z: (215, 15, 55),
    BoardTiles.L: (113, 45, 1),
    BoardTiles.J: (33, 65, 198),
    BoardTiles.T: (175, 41, 138)
}

def bag() -> Iterator[int]:
    bag = [BoardTiles.O, BoardTiles.I, BoardTiles.S, BoardTiles.Z, BoardTiles.L, BoardTiles.J, BoardTiles.T]
    piece = 7
    while True:
        if piece == 7:
            random.shuffle(bag)
            piece = 0
        yield bag[piece]
        piece += 1

class Board:
    WIDTH = 10
    HEIGHT = 20

    def __init__(self, display: pygame.surface.Surface):
        self.display = display
        l = [BoardTiles.EMPTY] * Board.WIDTH
        self.board = [l[:] for _ in range(Board.HEIGHT)]
        self.cell_length = 25

        self.current_piece = BoardTiles.EMPTY
    
    def loop(self):
        for i in range(Board.HEIGHT):
            for j in range(Board.WIDTH):
                pygame.draw.rect(self.display, BoardColours[self.board[i][j]],
                    pygame.Rect(self.cell_length * j, self.cell_length * i, self.cell_length * (j + 1), self.cell_length * (i + 1))
                )
    
    def process_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            pass
