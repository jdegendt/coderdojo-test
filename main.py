# v3.0

import pygame
import math
from castle import Castle
import bullet
import config

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption('Castle Defender')

# Klok
clock = pygame.time.Clock()

# Achtergrond
bg = pygame.image.load('img/bg.png').convert_alpha()

# Kogel
bullet_img = pygame.image.load('img/bullet.png').convert_alpha()
bullet.load_image(bullet_img)
bullet_group = pygame.sprite.Group()

# Maak een kasteel
castle_pos_x = config.SCREEN_WIDTH - 250
castle_pos_y = config.SCREEN_HEIGHT - 300
castle_scale = 0.2
castle_img_100 = pygame.image.load('img/castle/castle_100.png').convert_alpha()
castle = Castle(castle_img_100, castle_pos_x, castle_pos_y, castle_scale,
                bullet_group)

# Game Loop
run = True
while run:
  clock.tick(config.FPS)

  # Teken achtergrond
  screen.blit(bg, (0, 0))
  # Teken kasteel
  castle.draw(screen)
  castle.shoot()

  # Teken kogels
  bullet_group.update()
  bullet_group.draw(screen)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()

