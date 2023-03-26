import pygame
import pymunk
import pymunk.pygame_util
import sys
import math
from object import objects

pygame.init()
pygame.font.init()

WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

WIDTH, HEIGHT = WIN.get_size()
print(WIDTH, HEIGHT)

pygame.display.set_caption("balls")

space = pymunk.Space()
space.gravity = (0, 300)

white = (255, 255, 255)
gray = (211, 211, 211)
black = (0, 0, 0)

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 15)

ob = objects(space)


def main():
  # check if the user is currently placing a block
  # placing = False

  FPS = 60
  balls = []
  lines = []
  draw_options = pymunk.pygame_util.DrawOptions(WIN)
  ob.border(WIDTH, HEIGHT)

  while True:
    pos = pygame.mouse.get_pos()
    WIN.fill(white)

    text = font.render(f'FPS: {math.floor(clock.get_fps())}', True, black)
    dir_font = font.render(f'{ob.direction}', True, black)

    balls_to_remove = []
    lines_to_remove = []

    ob.find_dir()

    for event in pygame.event.get():
      if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        sys.exit()

      elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:

        line_shape = ob.line(pos)
        lines.append(line_shape)

      elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
        if line_shape in lines:
          lines_to_remove.append(line_shape)

      elif event.type == pygame.MOUSEBUTTONDOWN:

        ball_shape = ob.add_ball(pos)
        balls.append(ball_shape)

      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        for ball in balls:
          balls_to_remove.append(ball)

      if event.type == pygame.KEYDOWN and event.key == pygame.K_RSHIFT:
        for l in lines:
          lines_to_remove.append(l)

      if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
        if ob.direction != 4:
          ob.direction += 1
        else:
          ob.direction = 1

    for ball in balls:
      if ball.body.position.y > HEIGHT + ob.radius or ball.body.position.y - ob.dfb <= 0:
        balls_to_remove.append(ball)

    for ball in balls_to_remove:
      space.remove(ball, ball.body)
      balls.remove(ball)

    for l in lines_to_remove:
      space.remove(l, l.body)
      lines.remove(l)

    WIN.blit(text, (ob.dfb + 5, ob.dfb + 5))
    WIN.blit(dir_font, (WIDTH-ob.dfb-ob.dfb, ob.dfb+5))
    
    space.debug_draw(draw_options)

    space.step(1 / FPS)

    pygame.display.flip()
    clock.tick(FPS)


if __name__ == '__main__':
  main()
