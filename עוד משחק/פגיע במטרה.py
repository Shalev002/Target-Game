from pickle import TRUE
import random
from turtle import pos
import pygame, sys

score = 0

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound('C:/Users/salav/Downloads/סתם דברים/עוד משחק/תמונות/gunshot.mp3')
        pygame.mask.from_surface(self.image)
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('C:/Users/salav/Downloads/סתם דברים/עוד משחק/תמונות/BG.png')
pygame.mouse.set_visible(False)

crosshair = Crosshair('C:/Users/salav/Downloads/סתם דברים/עוד משחק/תמונות/MOUSE.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

target_group = pygame.sprite.Group()


time = 0


while True:

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()
    
    time += 0.5
    if time > 10:
        for target in range(1):
            new_target = Target('C:/Users/salav/Downloads/סתם דברים/עוד משחק/תמונות/target.png', random.randrange(0,screen_width), random.randrange(0,screen_height))   
            target_group.add(new_target)
        time = 0

    pygame.display.flip()
    screen.blit(background,(0,0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)
    