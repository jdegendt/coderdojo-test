import pygame
import math
from bullet import Bullet


class Castle():

  def __init__(self, image100, x, y, castle_scale, bullet_group):
    self.health = 1000
    self.max_health = self.health
    self.fired = False
    castle_width = int(image100.get_width() * castle_scale)
    castle_height = int(image100.get_height() * castle_scale)
    self.image100 = pygame.transform.scale(image100,
                                           (castle_width, castle_height))

    self.rect = self.image100.get_rect()
    self.rect.x = x
    self.rect.y = y

    self.bullet_group = bullet_group

  def shoot(self):
    pos = pygame.mouse.get_pos()
    x_dist = pos[0] - self.rect.midleft[0]
    y_dist = -(pos[1] - self.rect.midleft[1])
    self.angle = math.degrees(math.atan2(y_dist, x_dist))
    #get mouseclick
    if pygame.mouse.get_pressed()[0] and self.fired == False:
      self.fired = True
      bullet = Bullet(self.rect.midleft[0], self.rect.midleft[1], self.angle)
      self.bullet_group.add(bullet)
      print("Clicked at " + str(pos[0]) + ", " + str(pos[1]))
    #reset mouseclick
    if pygame.mouse.get_pressed()[0] == False:
      self.fired = False

  def draw(self, screen):
    self.image = self.image100
    screen.blit(self.image, self.rect)
