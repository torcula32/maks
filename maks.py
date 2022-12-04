import pygame
import sys
from settings import Settings


class Maks:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        self.bkg_image = pygame.image.load(self.settings.bkg_image)
        self.bkg_image_rect = self.bkg_image.get_rect()
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self._update_screen()
            self._check_events()
            self.clock.tick(30)

    def _update_screen(self):
        self.screen.fill(self.settings.bkg_color)
        self.screen.blit(self.bkg_image, self.bkg_image_rect)
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    game = Maks()
    game.run()
