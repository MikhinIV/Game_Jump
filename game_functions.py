import sys
import pygame
import random
#from frog import Frog
from leaf import Leaf

def update_info(screen, ai_set, count_frog):
    step = 30
    screen.fill(ai_set.info_color, ai_set.rect_info)
    rect_frog_info = ai_set.frog_right.get_rect()
    rect_frog_info.centery = ai_set.rect_info.centery
    rect_frog_info.left = step
    for i in range(count_frog):
        screen.blit(ai_set.frog_right, rect_frog_info)
        rect_frog_info.left = rect_frog_info.right + step

    rect_fly_info = ai_set.fly_right.get_rect()
    rect_fly_info.centerx = ai_set.rect_info.centerx
    rect_fly_info.centery = ai_set.rect_info.centery
    screen.blit(ai_set.fly_right, rect_fly_info)

    rect_fly_info.left = rect_fly_info.right + step
    font = pygame.font.Font(None, 72)
    text1 = font.render(str(ai_set.count_fly), 1, (180, 0, 0))
    screen.blit(text1, rect_fly_info)    
    pygame.display.update(ai_set.rect_info)

def update_screen(screen, ai_set, frog, leafs, fly):
    screen.fill(ai_set.bg_color, ai_set.rect_game)
    for leaf in leafs.sprites():
        leaf.blitme()
    fly.blitme()
    frog.blitme()
    pygame.display.update(ai_set.rect_game)
#    pygame.display.flip()    

def generate_position(leafs, step_x, step_y):
    while True:
        Flag = True
        pos = random.randint(20, 89)
        position_x, position_y = calc_position(step_x, step_y, pos)
        for leaf in leafs.copy():
            if leaf.rect.centerx == position_x and leaf.rect.centery == position_y:
                Flag = False
        if Flag:
            return (position_x, position_y)

def calc_position(step_x, step_y, pos):
    position_x = pos % 10 * step_x + step_x/2
    position_y = pos // 10 * step_y - step_y/2
    return (position_x, position_y)            

def start_leaf(leafs, ai_set, screen):
    leafs.add(Leaf(ai_set, screen, calc_position(ai_set.step_x, ai_set.step_y, ai_set.start_frog), 8))        
    leafs.add(Leaf(ai_set, screen, calc_position(ai_set.step_x, ai_set.step_y, ai_set.start_fly), 8))        

def update_leafs(leafs, ai_set, screen, frog):
    for leaf in leafs.copy():
        if leaf.stage == 7:
            leafs.remove(leaf)
            if not pygame.sprite.spritecollideany(frog, leafs):
                ai_set.Flag_Frog = False    
        else:
            leaf.update()
    leafs.add(Leaf(ai_set, screen, generate_position(leafs, ai_set.step_x, ai_set.step_y)))        
    leafs.add(Leaf(ai_set, screen, generate_position(leafs, ai_set.step_x, ai_set.step_y)))        
    leafs.add(Leaf(ai_set, screen, generate_position(leafs, ai_set.step_x, ai_set.step_y)))        
    leafs.add(Leaf(ai_set, screen, generate_position(leafs, ai_set.step_x, ai_set.step_y)))        

def kill_frog(frog, ai_set, screen, sound):
    sound.play()
    ai_set.set_frog()
    for i in range(50, 0, -15):
        pygame.draw.circle(screen, ai_set.bg_color, (frog.rect.centerx , frog.rect.centery), 50)
        pygame.draw.circle(screen, ai_set.black, (frog.rect.centerx , frog.rect.centery), i, 3)
        pygame.display.update()         
        pygame.time.wait(500)
        pygame.event.clear()

def kill_fly(frog, fly, ai_set, screen, sound):
    sound.play()
    ai_set.set_fly() 
    pygame.time.wait(500)
    pygame.event.clear()


def check_events(frog, ai_set, leafs, screen, fly):
#Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.USEREVENT:
            update_leafs(leafs, ai_set, screen, frog)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if frog.rect.centerx + ai_set.step_x < ai_set.screen_width:
                    frog.update(ai_set.step_x, 0, 'RIGHT')
            if event.key == pygame.K_LEFT:
                if frog.rect.centerx - ai_set.step_x > 0:
                    frog.update(-ai_set.step_x, 0, 'LEFT')               
            if event.key == pygame.K_UP:
                if frog.rect.centery - ai_set.step_y > 0:
                    frog.update(0, - ai_set.step_y, frog.direction)                    
            if event.key == pygame.K_DOWN:
                if frog.rect.centery + ai_set.step_y < ai_set.screen_height:
                    frog.update(0, ai_set.step_y, frog.direction)
            ai_set.sound_jump.play()                            
            if not pygame.sprite.spritecollideany(frog, leafs):
                ai_set.Flag_Frog = False
            if frog.rect.colliderect(fly.rect):
                ai_set.Flag_Fly = False
