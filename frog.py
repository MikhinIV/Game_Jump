import pygame

class Frog():
    def __init__(self, screen, position):
        self.screen = screen
        # Загрузка изображения и получение прямоугольника.
        self.image_right = pygame.image.load('images/frog_right.png')
        self.image_left = pygame.image.load('images/frog_left.png')
        self.image_direction = self.image_right
        self.rect = self.image_direction.get_rect()
#        self.screen_rect = screen.get_rect()
        self.rect.centerx, self.rect.centery = position  
        self.direction = 'RIGHT'

    def blitme(self):
        self.screen.blit(self.image_direction, self.rect)

    def update(self, x, y, direction):
        self.rect.centerx = self.rect.centerx + x
        self.rect.centery = self.rect.centery + y
        if direction != self.direction:
            self.direction = direction
            if direction == 'LEFT':
                self.image_direction = self.image_left
            else:
                self.image_direction = self.image_right

