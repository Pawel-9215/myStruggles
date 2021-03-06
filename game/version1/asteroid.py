import pyglet
import resources, physicalobject
import random
from random import randint
import fx

class Asteroid(physicalobject.PhysicalObject):
   def __init__(self, *args, **kwargs):
      super(Asteroid, self).__init__(resources.asteroid_big_image, *args, **kwargs)
      self.rotate_speed = random.random() * 100.0 - 50.0


   def handle_collision_with(self, other_object):
      super(Asteroid, self).handle_collision_with(other_object)
      if self.dead:
         resources.expl_sound.play()
         explosion = fx.ParticleFX(self.x, self.y, count=int(50*self.scale))
         self.new_fx.append(explosion)

      if self.dead and self.scale > 0.25:
         num_asteroids = random.randint(2, 4)
         for i in range(num_asteroids):
            #print("adding asteroid")
            new_asteroid = Asteroid(x = self.x, y = self.y, batch=self.batch)
            new_asteroid.rotation = random.randint(0, 360)
            new_asteroid.velocity_x = (random.random()*randint(-1, 1) * 40 + self.velocity_x)
            new_asteroid.velocity_y = (random.random()*randint(-1, 1) * 70 + self.velocity_y)
            new_asteroid.scale = self.scale * 0.5
            self.new_objects.append(new_asteroid)

   def update(self, dt):
      super(Asteroid, self).update(dt)
      self.rotation += self.rotate_speed * dt