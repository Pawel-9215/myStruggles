import pyglet
import random
from random import randint

class ParticleFX():

   #x_pos = 0
   #y_pos = 0
   #life = 2

   def __init__(self, x, y, life=2, count=10, speed=6):
      self.x_pos = x
      self.y_pos = y
      self.life = life
      self.dead = False
      self.count = count
      pyglet.clock.schedule_once(self.die, self.life)
      self.particles = self.generate_particles()
      self.vectors = self.generate_vectors()

   def generate_particles(self):
      particles = []
      for i in range(self.count):
         particles.append([self.x_pos, self.y_pos])
      return particles

   def generate_vectors(self):
      vectors = []
      for i in range(self.count):
         vectors.append([random.random(), random.random()])
      return vectors



   def die(self, dt):
      self.dead = True

   def update(self, dt):
     



      pass

   def draw(self):
      coords = []
      for particle in self.particles:
         coords.append(particle[0])
         coords.append(particle[1])

      
      pyglet.graphics.draw(len(self.particles), pyglet.gl.GL_POINTS, ('v2i', tuple(coords)))
      pass