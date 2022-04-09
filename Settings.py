import pygame
import random

#GREEN = (0, 200, 64)
LIGHT_BLUE = (64, 128, 255)
BLACK = (0, 0, 0)
GREY = (192, 192, 192)
WIDTH = 1200
HEIGH = 800

class Settings():
 #Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        #Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = WIDTH
        self.screen_height = HEIGH
        self.step_x = self.screen_width/10
        self.step_y = self.screen_height/8
        self.rect_info = pygame.Rect(0, 0, self.screen_width, self.step_y)
        self.rect_game = pygame.Rect(0, self.step_y, self.screen_width, self.screen_height)
        self.bg_color = (LIGHT_BLUE)
        self.info_color = (GREY)
        self.black = BLACK
        self.count_life = 3
        self.Flag_Frog = True
        self.Flag_Fly = True
        self.sound_jump = pygame.mixer.Sound('sound/jump.mp3')
        self.frog_right = pygame.image.load('images/frog_right.png')
        self.fly_right = pygame.image.load('images/fly_right.png')
        self.start_frog = random.randint(20, 89)
        self.start_fly = random.randint(20, 89)
        self.count_fly = 0

    def set_fly(self):
        self.count_fly = self.count_fly + 1
        self.Flag_Fly = True

    def set_frog(self):
        self.count_life = self.count_life - 1
        self.Flag_Frog = True

    def start_position(self):
        self.start_frog = random.randint(20, 89)
        self.start_fly = random.randint(20, 89)
