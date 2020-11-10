import pygame
import items
import armor
import weapons
import chest
import gauntlets
import greaves
import helmet
#
pygame.init()

win = pygame.display.set_mode((600,600))

pygame.display.set_caption("RPG")

x = 400
y = 500
w = 50
h = 50
d = 10

run = True
while run: 
  pygame.time.delay(100)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  
  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_DOWN]:
    y += d
  if keys[pygame.K_UP]:
    y -= d
  if keys[pygame.K_RIGHT]:
    x += d
  if keys[pygame.K_LEFT]:
    x -= d

  win.fill((0,0,0))
  pygame.draw.rect(win, (0,0,225),(x,y,w,h))
  pygame.display.update()

pygame.quit()
