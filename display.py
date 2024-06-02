import sys

import pygame

pygame.init()
pygame.display.set_caption('智能五子棋')
screen = pygame.display.set_mode((1080, 900))
screen.fill((255, 255, 255))

MARGIN = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
numbers.reverse()


def draw_board(screen: pygame.Surface) -> None:
    """ function draw_board(): `draws` the board """
    """ Let the chessboard's color be orange (this is the background, so it must be blit first) """
    pygame.draw.rect(screen, (248, 209, 130),
                     (MARGIN, 55 - MARGIN, 14 * 55, 15 * 55 - MARGIN - 25))  # I somehow made it!
    """ Draw the board """
    for i in range(1, 16):
        """ The horizontal lines """
        pygame.draw.line(screen, BLACK, (MARGIN, i * 55 - MARGIN), (MARGIN + 14 * 55, i * 55 - MARGIN), width=3)
        """ The vertical lines """
        pygame.draw.line(screen, BLACK, (MARGIN + (i - 1) * 55, 55 - MARGIN), (MARGIN + (i - 1) * 55, 15 * 55 - MARGIN),
                         width=3)
    """ Add the texts """
    font = pygame.font.SysFont('Arial', 30)
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
        pos.center = (MARGIN + 15 * 55 - 20, (y + 1) * 55 - MARGIN)
        screen.blit(foreach, pos)
    """ Add the dots at d12 l12 d4 l4 h8 """
    pygame.draw.circle(screen, BLACK, (MARGIN + 3 * 55, 4 * 55 - MARGIN), 5, 0)
    pygame.draw.circle(screen, BLACK, (MARGIN + 11 * 55, 4 * 55 - MARGIN), 5, 0)
    pygame.draw.circle(screen, BLACK, (MARGIN + 3 * 55, 12 * 55 - MARGIN), 5, 0)
    pygame.draw.circle(screen, BLACK, (MARGIN + 11 * 55, 12 * 55 - MARGIN), 5, 0)
    pygame.draw.circle(screen, BLACK, (MARGIN + 7 * 55, 8 * 55 - MARGIN), 5, 0)
    print("Draw board complete. display.draw_board()")


def draw_chess(screen: pygame.Surface, position: tuple[int, int], color: str) -> None:
    dest = WHITE if color == "white" else BLACK
    center = (MARGIN + (position[0] - 1) * 55, (16 - position[1]) * 55 - MARGIN)
    pygame.draw.circle(screen, dest, center, 20, 0)


def convert_position(compound_expr: str) -> tuple[int, int]:
    """
        function convert_position(): To convert position expr like "d7" into a tuple[int, int] format
        e.g.: draw_chess(screen, convert_position("d7"), "white")
    """
    x = compound_expr[0]
    y = compound_expr[1:]
    return letters.index(x) + 1, int(y)


draw_board(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    pygame.display.flip()
