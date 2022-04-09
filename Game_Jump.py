import pygame
from Settings import Settings
from frog import Frog
from fly import Fly
from pygame.sprite import Group
import game_functions as gf

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_set = Settings()
    screen = pygame.display.set_mode((ai_set.screen_width, ai_set.screen_height))
    
    pygame.display.set_caption("Cross a river")
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    sound_kill_frog = pygame.mixer.Sound('sound/kill_frog.mp3')
    sound_kill_fly =  pygame.mixer.Sound('sound/gulp.mp3')
    while  ai_set.count_life > 0:
        gf.update_info(screen, ai_set, ai_set.count_life)
        ai_set.start_position()
        frog = Frog(screen, gf.calc_position(ai_set.step_x, ai_set.step_y, ai_set.start_frog))
        fly = Fly(screen, gf.calc_position(ai_set.step_x, ai_set.step_y, ai_set.start_fly))
        leafs = Group()
        gf.start_leaf(leafs, ai_set, screen)
        while ai_set.Flag_Frog and ai_set.Flag_Fly:
            # Отслеживание событий клавиатуры и мыши.
            gf.check_events(frog, ai_set, leafs, screen, fly)
            gf.update_screen(screen, ai_set, frog, leafs, fly)
        if not ai_set.Flag_Frog:
            gf.kill_frog(frog, ai_set, screen,sound_kill_frog)            
        
        if not ai_set.Flag_Fly:
            gf.kill_fly(frog, fly, ai_set, screen, sound_kill_fly)            
        
while True:
    run_game()
