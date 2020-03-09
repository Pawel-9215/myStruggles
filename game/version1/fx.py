import pyglet
import random
from random import randint

class ParticleFX():

   #x_pos = 0
   #y_pos = 0
   #life = 2

   def __init__(self, x, y, life=4, count=40, speed=180):
      self.x_pos = x
      self.y_pos = y
      self.life = life
      self.dead = False
      self.count = count
      self.speed = speed
      pyglet.clock.schedule_once(self.die, self.life)
      self.particles = self.generate_particles()
      self.vectors = self.generate_vectors()
      self.clock = 1
      self.particle_color = [185,197,220]

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

   def delete(self):
      del self

   def update(self, dt):
      self.clock += 1
      if self.speed >= 5:
         self.speed -= 1
      for i in range(self.count):
        self.particles[i][0] += self.vectors[i][0]*randint(self.speed-3, self.speed+3)*dt
        self.particles[i][1] += self.vectors[i][1]*randint(self.speed-3, self.speed+3)*dt

      if min(self.particle_color) > 2:
         self.particle_color[0] -= 1
         self.particle_color[1] -= 1
         #self.particle_color[2] -= 1

      #self.draw()

      

   def draw(self):
      coords = []
      colors = []
      for particle in self.particles:
         coords.append(int(particle[0]))
         coords.append(int(particle[1]))
         colors.extend(self.particle_color)
      #print(coords)

      
      pyglet.graphics.draw(len(self.particles), pyglet.gl.GL_POINTS, ('v2i', coords), ('c3B', colors))
      pass

