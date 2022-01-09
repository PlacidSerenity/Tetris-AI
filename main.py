import pygame
import board

pygame.init()

sizes = width, height = 800, 600
display = pygame.display.set_mode(sizes)

b = board.Board(display)
b.board[0][0] = board.BoardTiles.T
b.board[0][1] = board.BoardTiles.T
b.board[0][2] = board.BoardTiles.T
b.board[1][1] = board.BoardTiles.T

print(b.board)

running = True
while running:
    display.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            b.process_event(event)
    b.loop()
    pygame.display.flip()

pygame.quit()
