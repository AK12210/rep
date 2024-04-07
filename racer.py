import pygame
import sys
from pygame.locals import *
import random
import time


pygame.init()


FPS = 60
FramePerSec = pygame.time.Clock()


BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

      def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

# Creating a class for coin
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

      def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
       # if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       # if pressed_keys[K_DOWN]:
            # self.rect.move_ip(0,5)

        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)


P1 = Player()
E1 = Enemy()
C1 = Coin()
b = 0
# Create sprite group for coins
coins = pygame.sprite.Group()
coins.add(C1)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
 

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 

while True:
       
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              # Spawn coin again after it was removed
              if b >= 1:
                    all_sprites.add(C1)
                    b = 0
        if game_score % 30 == 0 and game_score != 0:  # Increase speed after every 30 coins collected
            SPEED += 2
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(WHITE)

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    game_score_text = game_score_fonts.render(f'Score: {game_score}', True, (0, 0, 0))
    DISPLAYSURF.blit(game_score_text, game_score_rect)
    if pygame.sprite.spritecollideany(P1, coins):
          sc = int(random.randint(1, 3))  # Generating random weights of coins
          game_score += sc
          C1.kill()
    if pygame.sprite.spritecollideany(C1, enemies):
            C1.kill()
            b += 1    
    if pygame.sprite.spritecollideany(P1, enemies):
          DISPLAYSURF.fill(RED)
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
    pygame.display.update()
    FramePerSec.tick(FPS)
