import pyglet 
import resources 
import physicalobject

class Bullet(physicalobject.PhysicalObject):
   # bah bah
   def __init__(self, *args, **kwargs):
      super(Bullet, self).__init__(resources.bullet_image, *args, **kwargs)
      pyglet.clock.schedule_once(self.die, 1.0)
      self.is_bullet = True
      
   def die(self, dt):
      self.dead = True