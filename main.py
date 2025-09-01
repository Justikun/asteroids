import pygame

from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    # Game Loop
    while True:
        # Close Button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = pygame.time.Clock().tick(60) / 1000
        screen.fill("#000000")

        player.draw(screen)

        pygame.display.flip()
    # End Game Loop



    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
