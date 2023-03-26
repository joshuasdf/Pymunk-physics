import pymunk
import pygame
import pymunk.pygame_util
import random


class objects:

  def __init__(self, space):
    self.space = space
    self.radius = 20
    self.dfb = 50
    self.dir = 0
    self.direction = 1
  
  def border(self, width, height):
    pts = [(self.dfb, self.dfb), (width-self.dfb, self.dfb), (width-self.dfb, height-self.dfb), (self.dfb, height-self.dfb)]
    for i in range(4):
      seg = pymunk.Segment(self.space.static_body, pts[i], pts[(i+1)%4], 2)
      seg.elasticity = 1
      # seg.friciton = 1
      self.space.add(seg)
  
  def add_ball(self, pos):
    mass = 100
    body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, self.radius, (0, 0)))
    body.position = pos
    shape = pymunk.Circle(body, self.radius, (0, 0))
    shape.elasticity = 1
    # shape.friction = 1
    shape.color = (random.randint(1, 255), random.randint(1, 255),
                   random.randint(1, 255), random.randint(0, 255))
    self.space.add(body, shape)
    return shape

  def line(self, mouse_pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = mouse_pos
    l = pymunk.Segment(body, (-100, 0), (100, 0), 2)
    # l.friction = 1
    l.elasticity = 1

    body.angle += self.dir

    self.space.add(body, l)
    return l

  def find_dir(self):
    if self.direction == 1:
      self.dir = 0
    if self.direction == 2:
      self.dir = 2.356194495
    if self.direction == 3:
      self.dir = 0.785398165
    if self.direction == 4:
      self.dir = 1.57079633