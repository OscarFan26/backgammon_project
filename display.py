import sys

import pygame

pygame.init()
pygame.display.set_caption('智能五子棋')
screen = pygame.display.set_mode((1080, 900))
screen.fill((255, 255, 255))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw_board(screen):
    MARGIN = 30
    """ Draw the board """
    for i in range(1, 16):
        """ The horizontal lines """
        pygame.draw.line(screen, BLACK, (MARGIN, i * 55 - MARGIN), (MARGIN + 14 * 55, i * 55 - MARGIN), width=5)
        """ The vertical lines """
        pygame.draw.line(screen, BLACK, (MARGIN + (i - 1) * 55, 55 - MARGIN), (MARGIN + (i - 1) * 55, 15 * 55 - MARGIN),
                         width=5)
    """ Add the texts """
    font = pygame.font.SysFont('Arial', 30)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
    """ Render a ~ o on the screen (horizontal) """
    for x in range(15):
        foreach = font.render(letters[x], True, BLACK)
        pos = foreach.get_rect()
        pos.center = (MARGIN + x * 55, 16 * 55 - MARGIN - 20)
        screen.blit(foreach, pos)
    """ Now render 1 ~ 15 on the screen (vertical) """
    for y in range(15):
        foreach = font.render(numbers[y], True, BLACK)
        pos = foreach.get_rect()
        pos.center = (MARGIN + 15 * 55 - 20, (y+1) * 55 - MARGIN)
        screen.blit(foreach, pos)

    # TODO draw_board(): add the dots
# TODO draw_chess(chess_x: int, chess_y: int, color: str)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    draw_board(screen)
    pygame.display.flip()
