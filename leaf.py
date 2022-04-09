import pygame
from pygame.sprite import Sprite

arr_image = [pygame.image.load('images/leaf_1.png'), pygame.image.load('images/leaf_2.png'), pygame.image.load('images/leaf_3.png'), pygame.image.load('images/leaf_4.png')]

class Leaf(Sprite):
    def __init__(self, ai_set, screen, x, stage = 0):
        super(Leaf, self).__init__()
        self.screen = screen
        self.stage = stage
        if self.stage == 8:
            self.image = arr_image[-1] 
        else:    
            self.image = arr_image[0] 
        self.rect = arr_image[-1].get_rect()
        self.rect.centerx, self.rect.centery = x
    
    def update(self):
        if self.stage == 8:
            self.image = arr_image[-1]
        else:    
            self.stage = self.stage + 1
            if self.stage < 4: 
                self.image = arr_image[self.stage]
            else:             
                self.image = arr_image[7 - self.stage]

    def blitme(self):
        self.screen.blit(self.image, self.rect)