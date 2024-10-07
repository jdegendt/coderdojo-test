import pygame
import math
import config

bullet_image = None


def load_image(image):
  global bullet_image
  bullet_scale = 0.075
  bullet_w = int(image.get_width() * bullet_scale)
  bullet_h = int(image.get_height() * bullet_scale)
  bullet_image = pygame.transform.scale(image, (bullet_w, bullet_h))


class Bullet(pygame.sprite.Sprite):

  def __init__(self, x, y, angle):
    pygame.sprite.Sprite.__init__(self)
    self.image = bullet_image
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.speed = 10
    self.angle = math.radians(angle)  # converteer graden naar radialen
    self.dx = math.cos(self.angle) * self.speed
    self.dy = -(math.sin(self.angle) * self.speed)

  def update(self):
    #check if bullet has gone off the screen
    if self.rect.right < 0 or self.rect.left > config.SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > config.SCREEN_HEIGHT:
      self.kill()
    #move bullet
    self.rect.x += self.dx
    self.rect.y += self.dy
